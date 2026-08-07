import { createClient, type User } from '@supabase/supabase-js';
import type { CloudAdminUser, UserProfile, UserProgressState } from '../game/types';

const url = import.meta.env.VITE_SUPABASE_URL?.trim();
const publishableKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY?.trim()
  || import.meta.env.VITE_SUPABASE_ANON_KEY?.trim();

export const cloudEnabled = Boolean(url && publishableKey);

/** Canonical app URL used for auth email redirects (confirmation + password reset). */
export const APP_REDIRECT_URL = typeof window !== 'undefined'
  ? `${window.location.origin}${import.meta.env.BASE_URL}`
  : 'https://lareesahu.github.io/gramlingo/';

const client = cloudEnabled
  ? createClient(url!, publishableKey!, {
      auth: { persistSession: true, autoRefreshToken: true },
    })
  : null;

export interface CloudIdentity {
  profile: UserProfile;
  state: UserProgressState | null;
  isAdmin: boolean;
}

/** Typed auth failure with a user-facing message and a stable machine code. */
export class CloudAuthError extends Error {
  code: string;
  userMessage: string;

  constructor(code: string, userMessage: string) {
    super(userMessage);
    this.name = 'CloudAuthError';
    this.code = code;
    this.userMessage = userMessage;
  }
}

/** Map a Supabase auth error to a stable code + friendly message. */
export function describeAuthError(err: unknown): { code: string | null; message: string } {
  const code = (err as { code?: string })?.code || (err as { error_code?: string })?.error_code || '';
  const msg = (err as { message?: string })?.message || (err as { msg?: string })?.msg || '';
  const lower = `${code} ${msg}`.toLowerCase();

  if (lower.includes('invalid_credentials') || lower.includes('invalid login credentials')) {
    return { code: 'invalid_credentials', message: "That password isn't right for this account. Use 'Forgot password?' to reset it." };
  }
  if (lower.includes('email_not_confirmed') || lower.includes('email not confirmed')) {
    return { code: 'email_not_confirmed', message: "This email isn't confirmed yet. Check your inbox (and spam) for the confirmation link, or resend it below." };
  }
  if (lower.includes('user_already_exists') || lower.includes('user already registered') || lower.includes('user_already_registered')) {
    return { code: 'user_already_exists', message: "An account already exists for this email. Try the correct password or use 'Forgot password?'." };
  }
  if (lower.includes('over_email_send_rate_limit') || lower.includes('email rate limit exceeded')) {
    return { code: 'rate_limited', message: 'Too many emails sent. Wait a few minutes and try again.' };
  }
  if (lower.includes('over_request_rate_limit') || lower.includes('over_rate_limit') || lower.includes('rate limit')) {
    return { code: 'rate_limited', message: 'Too many attempts. Wait a few minutes and try again.' };
  }
  if (lower.includes('weak_password')) {
    return { code: 'weak_password', message: 'Password must be at least 6 characters.' };
  }
  if (lower.includes('validation_failed') || lower.includes('signup_disabled') || lower.includes('provider_disabled')) {
    return { code: 'validation_failed', message: 'This email or password is not accepted. Try a different email or a stronger password.' };
  }
  return { code: code || null, message: 'Something went wrong. Please try again.' };
}

function toCloudAuthError(err: unknown): CloudAuthError {
  const { code, message } = describeAuthError(err);
  return new CloudAuthError(code || 'unknown', message);
}

function requireClient() {
  if (!client) throw new Error('Cloud sync is not configured.');
  return client;
}

function emptyState(): UserProgressState {
  return {
    activeModuleId: null,
    activePhaseId: null,
    activeQuestionIndex: 0,
    progress: [],
    errorLog: [],
  };
}

function usernameFromUser(user: User) {
  const metadataName = user.user_metadata?.username;
  return typeof metadataName === 'string' && metadataName.trim()
    ? metadataName.trim()
    : (user.email?.split('@')[0] || 'learner');
}

async function loadIdentity(user: User): Promise<CloudIdentity> {
  const supabase = requireClient();
  const fallbackUsername = usernameFromUser(user);
  const { data: existingProfile, error: profileReadError } = await supabase
    .from('profiles')
    .select('id, username, created_at')
    .eq('id', user.id)
    .maybeSingle();
  if (profileReadError) throw profileReadError;

  let username = existingProfile?.username || fallbackUsername;
  let createdAt = existingProfile?.created_at || user.created_at;
  if (!existingProfile) {
    const { data: inserted, error: insertError } = await supabase
      .from('profiles')
      .insert({ id: user.id, username })
      .select('username, created_at')
      .single();
    if (insertError) throw insertError;
    username = inserted.username;
    createdAt = inserted.created_at;
  }

  const { data: progressRow, error: progressError } = await supabase
    .from('progress_state')
    .select('data')
    .eq('user_id', user.id)
    .maybeSingle();
  if (progressError) throw progressError;

  return {
    profile: {
      id: user.id,
      email: user.email,
      username,
      pin: null,
      createdAt,
    },
    state: progressRow?.data ? { ...emptyState(), ...progressRow.data } : null,
    isAdmin: user.app_metadata?.role === 'admin',
  };
}

/**
 * Sign in with email + password. Throws CloudAuthError with a user-facing
 * message on any failure. Never falls back to creating an account — signup
 * is a separate, explicit flow.
 */
export async function signIn(email: string, password: string): Promise<CloudIdentity> {
  const supabase = requireClient();
  const { data, error } = await supabase.auth.signInWithPassword({ email, password });
  if (error) throw toCloudAuthError(error);
  return loadIdentity(data.user);
}

/**
 * Create a brand-new account (email + password). Returns null when the
 * project requires email confirmation and the account is awaiting it —
 * callers should route the user to a "check your email" step.
 */
export async function createAccount(email: string, password: string, name?: string): Promise<CloudIdentity | null> {
  const supabase = requireClient();
  const displayName = name?.trim() || email.split('@')[0];
  const { data, error } = await supabase.auth.signUp({
    email,
    password,
    options: { data: { username: displayName } },
  });
  if (error) throw toCloudAuthError(error);
  if (!data.user || !data.session) return null; // confirmation email required
  return loadIdentity(data.user);
}

/** Send a password-reset email. Recovery link lands back on the app. */
export async function requestCloudPasswordReset(email: string): Promise<void> {
  const supabase = requireClient();
  const { error } = await supabase.auth.resetPasswordForEmail(email, {
    redirectTo: APP_REDIRECT_URL,
  });
  if (error) throw toCloudAuthError(error);
}

/** Resend the sign-up confirmation email for an unconfirmed account. */
export async function resendCloudConfirmation(email: string): Promise<void> {
  const supabase = requireClient();
  const { error } = await supabase.auth.resend({
    type: 'signup',
    email,
    options: { emailRedirectTo: APP_REDIRECT_URL },
  });
  if (error) throw toCloudAuthError(error);
}

/** Set a new password during the recovery flow (recovery session must be active). */
export async function updateCloudPassword(newPassword: string): Promise<void> {
  const supabase = requireClient();
  const { error } = await supabase.auth.updateUser({ password: newPassword });
  if (error) throw toCloudAuthError(error);
}

/**
 * True when the page was opened via a Supabase recovery link (#type=recovery).
 * Captured at module scope because supabase-js strips `type=recovery` from the
 * URL hash asynchronously on init — a live check alone would miss it.
 */
const INITIAL_URL_HASH = typeof window !== 'undefined' ? window.location.hash : '';
export function hasRecoveryToken(): boolean {
  return /[#&]type=recovery/.test(INITIAL_URL_HASH) || /[#&]type=recovery/.test(window.location.hash);
}

/** Strip the recovery/access token hash from the address bar after processing. */
export function clearRecoveryHash(): void {
  if (typeof window === 'undefined') return;
  try {
    window.history.replaceState(null, '', window.location.pathname + window.location.search);
  } catch {
    // history API unavailable (rare) — ignore
  }
}

export async function restoreCloudIdentity(): Promise<CloudIdentity | null> {
  if (!client) return null;
  const { data, error } = await client.auth.getUser();
  if (error || !data.user) return null;
  return loadIdentity(data.user);
}

export async function signOutCloud() {
  if (!client) return;
  const { error } = await client.auth.signOut();
  if (error) throw error;
}

export async function syncCloudState(userId: string, state: UserProgressState) {
  const supabase = requireClient();
  const { error } = await supabase.from('progress_state').upsert({
    user_id: userId,
    data: state,
    updated_at: new Date().toISOString(),
  }, { onConflict: 'user_id' });
  if (error) throw error;
}

export async function fetchCloudAdminUsers(): Promise<CloudAdminUser[]> {
  const supabase = requireClient();
  const [profilesResult, progressResult] = await Promise.all([
    supabase.from('profiles').select('id, username, created_at').order('created_at'),
    supabase.from('progress_state').select('user_id, data, updated_at'),
  ]);
  if (profilesResult.error) throw profilesResult.error;
  if (progressResult.error) throw progressResult.error;

  const progressByUser = new Map(progressResult.data.map((row) => [row.user_id, row]));
  return profilesResult.data.map((profile) => {
    const row = progressByUser.get(profile.id);
    return {
      id: profile.id,
      username: profile.username,
      createdAt: profile.created_at,
      updatedAt: row?.updated_at || profile.created_at,
      state: row?.data ? { ...emptyState(), ...row.data } : emptyState(),
    };
  });
}
