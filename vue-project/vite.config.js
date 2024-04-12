import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

const backendPath = '../recipe_maker';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: '/static/vite/',
  server: {
    watch: {
      ignored: [],
      },
    },
  build: {
    manifest: true,
    emptyOutDir: true,
    outDir: backendPath + '/core/static/vite/',
    rollupOptions: {
      input: {
        // vue_movie_edit: "./src/apps/movie_edit/movie_edit.js",
      },
    },
  },
});
