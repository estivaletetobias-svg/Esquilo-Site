import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        metodo: resolve(__dirname, 'metodo.html'),
        emagrecimento: resolve(__dirname, 'emagrecimento.html'),
        avaliacao: resolve(__dirname, 'avaliacao.html'),
        servicos: resolve(__dirname, 'servicos.html'),
        conteudos: resolve(__dirname, 'conteudos.html'),
        ebooks: resolve(__dirname, 'ebooks.html'),
        depoimentos: resolve(__dirname, 'depoimentos.html'),
        contato: resolve(__dirname, 'contato.html'),
        florianopolis: resolve(__dirname, 'personal-trainer-florianopolis/index.html'),
        protocolo_anna: resolve(__dirname, 'protocolo-anna.html'),
      },
    },
  },
});
