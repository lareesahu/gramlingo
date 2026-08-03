import { createClient, type User } from '@supabase/supabase-js';
import type { CloudAdminUser, UserProfile, UserProgressState } from '../game/types';

const url = import.meta.env.VITE_SUPABASE_URL?.trim();
const publishableKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY?.trim()
  || import.meta.env.VITE_SUPABASE_ANON_KEY?.trim();

export const cloudEnabled = Boolean(url && publishableKey);

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

export async function signInOrCreate(email: string, password: string): Promise<CloudIdentity> {
  const supabase = requireClient();
  const signedIn = await supabase.auth.signInWithPassword({ email, password });
  if (signedIn.data.user) return loadIdentity(signedIn.data.user);

  const signedUp = await supabase.auth.signUp({
    email,
    password,
    options: { data: { username: email.split('@')[0] } },
  });
  if (signedUp.error) throw signedUp.error;
  if (!signedUp.data.user || !signedUp.data.session) {
    throw new Error('Check your email to confirm the new account, then log in.');
  }
  return loadIdentity(signedUp.data.user);
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
