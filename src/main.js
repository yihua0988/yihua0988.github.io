import { createApp } from 'vue'
import App from './App.vue'

// 建立 Vue 實體並掛載到 index.html 的 #app 區塊上
const app = createApp(App)
app.mount('#app')