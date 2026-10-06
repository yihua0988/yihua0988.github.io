<script setup>
// 🚨 關鍵：必須在這裡「匯入」元件，Vue 才會認得它！
import Background from './components/Background.vue'
import Hero from './components/Hero.vue'
import Services from './components/Services.vue'
import Projects from './components/Projects.vue'
import Skills from './components/Skills.vue'
import Experience from './components/Experience.vue'
import Credentials from './components/Credentials.vue'
import Footer from './components/Footer.vue'

// 💡 等你以後建好了 Hero.vue，就再加一行： import Hero from './components/Hero.vue'
</script>

<template>
  <main>
    <Background />
    <Hero />
    <Services />	
    <Projects />
    <Skills />
    <Experience />
    <Credentials />
    <Footer />
  </main>
</template>

<style>
/* 🌟 全域變數與基礎設定 (注意這裡不能加 scoped，這是要套用到全站的) */
:root {
  --bg-main: #060b19;        
  --card-bg: rgba(17, 24, 43, 0.85); 
  --accent-primary: #007bff; 
  --accent-secondary: #20c997; 
  --accent-tertiary: #fd7e14;  
  --accent-purple: #b55fe6;  
  --text-bright: #ffffff;      
  --text-muted: #94a3b8;       
  --spring: cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

html, body {
  margin: 0; 
  padding: 0;
  background-color: var(--bg-main); /* 宇宙黑底色 */
  color: var(--text-bright);
  font-family: 'Noto Sans TC', sans-serif;
  line-height: 1.8; 
  overflow-x: hidden; 
  font-size: 18px;
}

a { text-decoration: none; color: inherit; transition: 0.4s var(--spring); }
ul { list-style: none; padding: 0; margin: 0; }
</style>