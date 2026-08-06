import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: '/gramlingo/',
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
  },
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: './src/test-setup.ts',
    include: ['src/**/*.test.{ts,tsx}'],
    css: true,
  },
});
