/* ═══════════════════════════════════════════════
   GRAMLINGO — Supabase Sync Layer
   Online storage so admin can see ALL users across devices.
   ═══════════════════════════════════════════════ */

import { createClient } from '@supabase/supabase-js';
import type { AppState, UserProfile } from '../game/types';

const SUPABASE_URL = import.meta.env.VITE_SUPABASE_URL as string;
const SUPABASE_ANON_KEY = import.meta.env.VITE_SUPABASE_ANON_KEY as string;

let supabase: ReturnType<typeof createClient> | null = null;

function getClient() {
  if (!SUPABASE_URL || !SUPABASE_ANON_KEY) return null;
  if (!supabase) {
    supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
  }
  return supabase;
}

export function isSupabaseAvailable(): boolean {
  return !!(SUPABASE_URL && SUPABASE_ANON_KEY);
}

/** Upsert one user's full state to Supabase */
export async function syncUserProgress(username: string, state: Partial<AppState>): Promise<void> {
  const client = getClient();
  if (!client) return;

  const payload = {
    username,
    data: {
      progress: state.progress || [],
      errorLog: state.errorLog || [],
      moduleLocks: state.moduleLocks || {},
      language: state.language || 'en',
      activeModuleId: state.activeModuleId || null,
      activePhaseId: state.activePhaseId || null,
      activeQuestionIndex: state.activeQuestionIndex || 0,
      updatedAt: new Date().toISOString(),
    },
    updated_at: new Date().toISOString(),
  };

  try {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    await (client as any).from('gramlingo_progress').upsert(payload, {
      onConflict: 'username',
    });
  } catch (err) {
    console.warn('Supabase sync failed (non-critical):', err);
  }
}

/** Fetch ALL users' progress from Supabase (for admin) */
export async function fetchAllProgress(): Promise<Array<{ username: string; data: any; updated_at: string }>> {
  const client = getClient();
  if (!client) return [];

  try {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const { data, error } = await (client as any)
      .from('gramlingo_progress')
      .select('*')
      .order('updated_at', { ascending: false });

    if (error) throw error;
    return data || [];
  } catch (err) {
    console.warn('Supabase fetch failed:', err);
    return [];
  }
}

/** Sync a user profile creation to Supabase */
export async function syncUserProfile(user: UserProfile): Promise<void> {
  const client = getClient();
  if (!client) return;

  try {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    await (client as any).from('gramlingo_users').upsert(
      {
        username: user.username,
        created_at: user.createdAt || new Date().toISOString(),
        updated_at: new Date().toISOString(),
      },
      { onConflict: 'username' }
    );
  } catch (err) {
    console.warn('Supabase user sync failed:', err);
  }
}

/** Fetch all registered users from Supabase */
export async function fetchAllUsers(): Promise<UserProfile[]> {
  const client = getClient();
  if (!client) return [];

  try {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const { data, error } = await (client as any)
      .from('gramlingo_users')
      .select('*')
      .order('created_at', { ascending: true });

    if (error) throw error;
    return (data || []).map((d: any) => ({
      username: d.username,
      pin: null,
      createdAt: d.created_at,
    }));
  } catch (err) {
    console.warn('Supabase user fetch failed:', err);
    return [];
  }
}
