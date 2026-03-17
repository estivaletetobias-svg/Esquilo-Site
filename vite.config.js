import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        florianopolis: resolve(__dirname, 'personal-trainer-florianopolis/index.html'),
      },
    },
  },
});
