import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import { readFileSync, existsSync } from 'fs';

const pkg = JSON.parse(readFileSync('./package.json', 'utf-8'));

// Single source of truth: VERSION-Datei im Repo-Wurzel.
let APP_VERSION = pkg.version;
if (existsSync('../VERSION')) {
  APP_VERSION = readFileSync('../VERSION', 'utf-8').trim();
}

const BACKEND = process.env.VITE_BACKEND || 'http://127.0.0.1:8200';

export default defineConfig({
  plugins: [svelte()],
  define: {
    __APP_VERSION__: JSON.stringify(APP_VERSION),
  },
  server: {
    host: '127.0.0.1',
    port: 5184,
    strictPort: false,
    proxy: {
      '/api': {
        target: BACKEND,
        changeOrigin: true,
      },
    },
  },
  build: {
    outDir: 'dist',
    sourcemap: false,
  },
});
