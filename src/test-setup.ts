import '@testing-library/jest-dom';
import { vi } from 'vitest';

vi.stubEnv('VITE_SUPABASE_URL', '');
vi.stubEnv('VITE_SUPABASE_PUBLISHABLE_KEY', '');
vi.stubEnv('VITE_SUPABASE_ANON_KEY', '');

// Skip the first-launch intro slideshow in tests so screen tests reach the app.
localStorage.setItem('gramlingo_intro_seen_v1', '1');
