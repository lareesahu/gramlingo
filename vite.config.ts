import { defineConfig, type Plugin } from 'vitest/config';
import react from '@vitejs/plugin-react';
import fs from 'node:fs';
import path from 'node:path';

/**
 * GitHub Pages SPA fallback: after build, copy dist/index.html → dist/404.html.
 * Pages serves 404.html for any unmatched path, so deep links like /app or
 * /app/lesson boot the app with the original pathname intact and the router
 * resolves the right screen (instead of a raw 404).
 */
function spa404Fallback(): Plugin {
  return {
    name: 'spa-404-fallback',
    apply: 'build',
    closeBundle() {
      const dist = 'dist';
      const src = path.join(dist, 'index.html');
      const dst = path.join(dist, '404.html');
      if (fs.existsSync(src)) {
        fs.copyFileSync(src, dst);
        console.log('[spa-404-fallback] wrote dist/404.html');
      }
    },
  };
}

export default defineConfig({
  plugins: [react(), spa404Fallback()],
  base: './',
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
