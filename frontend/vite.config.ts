import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import { readFileSync, existsSync } from 'fs';

const pkg = JSON.parse(readFileSync('./package.json', 'utf-8'));

// Single source of truth: VERSION-Datei. Dev-Modus liegt sie eine
// Ebene über frontend/, im Docker-Build wird sie in den Build-Context
// kopiert und liegt direkt neben package.json.
let APP_VERSION = pkg.version;
for (const pfad of ['../VERSION', './VERSION']) {
  if (existsSync(pfad)) {
    APP_VERSION = readFileSync(pfad, 'utf-8').trim();
    break;
  }
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
