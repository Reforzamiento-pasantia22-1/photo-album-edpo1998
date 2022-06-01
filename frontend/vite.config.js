import { defineConfig,loadEnv } from 'vite'
import react from '@vitejs/plugin-react'



export default ({ mode }) => {
    process.env = {...process.env, ...loadEnv(mode, process.cwd())};

    return defineConfig({
      plugins: [react()],
      define: {
        'process.env.VITE_BACKEND_ADDR': JSON.stringify(process.env.VITE_BACKEND_ADDR),
      }
    });
}