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
    port: 4180,
    timeout: 30000,
    reuseExistingServer: false,
  },
});
