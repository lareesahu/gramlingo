import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './src/e2e',
  fullyParallel: false,
  retries: 1,
  workers: 1,
  reporter: 'list',
  use: {
    baseURL: 'http://localhost:4180/gramlingo',
    trace: 'on-first-retry',
  },
  webServer: {
    command: 'npm run build && npx vite preview --port 4180 --strictPort',
    env: {
      ...process.env,
      VITE_SUPABASE_URL: '',
      VITE_SUPABASE_PUBLISHABLE_KEY: '',
      VITE_SUPABASE_ANON_KEY: '',
    },
    port: 4180,
    timeout: 30000,
    reuseExistingServer: false,
  },
});
