import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import Sitemap from 'vite-plugin-sitemap'	

// https://vite.dev/config/
export default defineConfig({
  base: '/',
  plugins: [
    vue(),
    vueDevTools(),
    Sitemap({
      // 請確認這是你最終的 GitHub Pages 網址
      hostname: 'https://yihua0988.github.io', 
      dynamicRoutes: [
        // -----------------------------------------
        // 1. 來自你的 Vue Router (index.js) 的分頁路由
        // -----------------------------------------
        '/PFvue',
        '/PFvue/fraud-patterns',
        '/PFvue/prevention',
        '/PFvue/anti-deepfake-video',
        '/PFvue/anti-phishing-video',
        '/PFvue/summary',
        '/PFvue/fraud-growth-stats',
        '/PFvue/ai-fraud-news',
        '/PFvue/top-10-frauds',
        '/PFvue/victim-profile',
        '/PFvue/fraud-vulnerabilities',
        '/PFvue/action-plan',
        '/PFvue/anti-investment-video',
        '/PFvue/fraud-interception',
        '/PFvue/anti-fraud-results',
        '/PFvue/one-page-scam',
        '/PFvue/fraud-trends',

        // -----------------------------------------
        // 2. 你額外指定的獨立靜態路徑
        // -----------------------------------------
        '/1150527game/',
        '/1150311JSSQL/',
		'/1150311JSSQL/HTML/products_all.html',
        '/1150402point/'
      ]
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})