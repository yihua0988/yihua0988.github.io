<template>
  <header class="hero-container">
    <!-- 🚀 改為 position: fixed，讓背景留在畫面中，並隨著捲動計算透明度淡出 -->
    <div class="hero-bg-wrapper" :style="{ opacity: heroOpacity, pointerEvents: heroOpacity === 0 ? 'none' : 'auto' }">
      <video ref="heroVideo" class="hero-video" autoplay loop muted playsinline>
        <source src="/cover.mp4" type="video/mp4">
        您的瀏覽器不支援 HTML5 影片。
      </video>
      <div class="hero-overlay"></div>
    </div>

    <!-- 💡 中間這塊卡片維持正常捲動，且 100% 不透明 -->
    <div class="intro-section reveal">
      <div class="legendary-bolt-container">
        <i class="fas fa-bolt hero-bolt-3d" style="font-size: 4.5rem; color: var(--accent-primary); filter: drop-shadow(0 5px 15px rgba(0,123,255,0.4));"></i>
        <span class="bolt-circle circle-blue"></span>
        <span class="bolt-circle circle-green"></span>
        <span class="bolt-circle circle-yellow"></span>
      </div>
      <h1>
        大家好我是洪益華(SAKA)
        <span class="en-sub">Hello, I'm Hung Yi-Hua (Saka)</span>
      </h1>
      <p>
        僑光科大 資訊科技碩士班｜7年實戰經驗：全端開發、系統與機電整合
        <span class="en-desc">
          M.S. in IT, OCU | 7+ Years Exp | Full-Stack Dev & System Integration
        </span>
      </p>
      <div class="btn-group">
        <a href="#slash-services" class="btn-tech smooth-scroll"><i class="fas fa-chevron-down"></i>瀏覽服務內容</a>
        <a href="#" class="btn-tech btn-tech-filled" @click.prevent="copyEmail"><i class="fas fa-envelope"></i>直接聯繫我</a>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const heroVideo = ref(null)
const heroOpacity = ref(1)

const handleScroll = () => {
  const scrollY = window.scrollY
  const heroHeight = window.innerHeight
  
  // 計算透明度：當捲動超過一個螢幕高度時，背景完全淡出 (opacity 降為 0)
  let opacity = 1 - (scrollY / heroHeight)
  if (opacity < 0) opacity = 0
  if (opacity > 1) opacity = 1
  
  heroOpacity.value = opacity
}

onMounted(() => {
  if (heroVideo.value) {
    heroVideo.value.muted = true
    const playPromise = heroVideo.value.play()
    if (playPromise !== undefined) {
      playPromise.then(() => {
        console.log("✔ 影片已自動開始播放")
      }).catch(error => {
        console.log("❌ 自動播放被攔截，正在嘗試點擊/觸碰後喚醒")
        window.addEventListener('touchstart', function() { heroVideo.value.play() }, { once: true }) 
      })
    }
  }

  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

const copyEmail = () => {
  navigator.clipboard.writeText("yihua0988@gmail.com").then(() => {
    alert("✉️ Email已複製！正在呼叫信箱 App...")
    setTimeout(() => window.location.href = "mailto:yihua0988@gmail.com", 500)
  }).catch(err => console.error('複製失敗', err))
}
</script>

<style scoped>
/* ===================================================
   🌟 首頁橫幅 (Hero Section) 專屬樣式
=================================================== */
.hero-container {
  position: relative; z-index: 1; width: 100%; min-height: 100vh; display: flex; justify-content: center; align-items: center; 
  overflow: hidden; padding: 20px; box-sizing: border-box;
}

/* 🚀 關鍵修改：改為 position: fixed，讓背景定格在視窗中，並支援平滑淡出 */
.hero-bg-wrapper {
  position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
  z-index: 0;
  transition: opacity 0.1s ease-out;
}

.hero-video { 
  position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
  object-fit: cover; transform: translateZ(0); will-change: transform;
}
.hero-overlay {
  position: absolute; top: 0; left: 0; width: 100%; height: 100%;
  background: linear-gradient(to bottom, rgba(6,11,25,0.7), #060b19); 
}

/* 中間的自我介紹卡片維持正常文件流，不透明 */
.intro-section {
  position: relative; z-index: 2; width: 100%; max-width: 800px;
  background: rgba(10, 15, 30, 0.85); 
  border-radius: 35px; border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 40px rgba(0, 123, 255, 0.2), inset 0 0 20px rgba(255,255,255,0.05);
  display: flex; flex-direction: column; justify-content: center; align-items: center;
  text-align: center; padding: 60px 40px; box-sizing: border-box; transform: translateZ(0); 
  opacity: 1 !important;
}

.intro-section h1 { font-size: clamp(2rem, 3.5vw, 3.5rem); margin: 0 0 10px; font-weight: 900; letter-spacing: 2px; color: #fff; line-height: 1.2; text-shadow: 0 0 15px rgba(0, 123, 255, 0.8); }
.intro-section h1 .en-sub { display: block; font-size: 0.35em; color: var(--accent-secondary); letter-spacing: 2px; margin-top: 10px; font-weight: 800; text-shadow: 0 0 10px rgba(32,201,151,0.5);}
.intro-section p { font-size: clamp(1.1rem, 1.3vw, 1.3rem); color: var(--text-muted); font-weight: 800; max-width: 90%; margin: 0 auto 30px; line-height: 1.8; }
.intro-section p .en-desc { display: block; font-size: 0.8em; color: var(--accent-primary); margin-top: 10px; font-weight: 900; }

.btn-group { display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; margin-top: 15px; }
.btn-tech { padding: 15px 40px; border-radius: 50px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; font-size: 1.1rem; background: rgba(0, 0, 0, 0.5); color: var(--accent-secondary); border: 1px solid var(--accent-secondary); box-shadow: 0 0 10px rgba(32, 201, 151, 0.2); transition: 0.4s var(--spring); display: inline-flex; align-items: center; gap: 10px; cursor: pointer; }
.btn-tech:hover { transform: translateY(-5px); box-shadow: 0 0 20px rgba(32, 201, 151, 0.6), inset 0 0 10px rgba(32,201,151,0.2); background: rgba(32,201,151,0.1); }
.btn-tech-filled { background: var(--accent-primary); color: #fff; border: 1px solid var(--accent-primary); box-shadow: 0 0 15px rgba(0,123,255,0.4); }
.btn-tech-filled:hover { background: #0056b3; box-shadow: 0 0 25px rgba(0,123,255,0.8), inset 0 0 10px rgba(255,255,255,0.2); color: #fff;}

/* 🌟 閃電與 3D 圓環特效 */
@keyframes spin3D { 0% { transform: rotateY(0deg) translateZ(0); } 100% { transform: rotateY(360deg) translateZ(0); } }
.hero-bolt-3d { display: inline-block; animation: spin3D 3s linear infinite; will-change: transform; -webkit-backface-visibility: visible; backface-visibility: visible; }
.legendary-bolt-container { position: relative; display: flex; justify-content: center; align-items: center; width: 180px; height: 180px; margin-bottom: 25px; perspective: 1000px; transform: rotateX(20deg); transform-style: preserve-3d; }
.legendary-bolt-container i { position: relative; z-index: 5; margin-bottom: 0 !important; }
.bolt-circle { position: absolute; border-radius: 50%; top: 50%; left: 50%; will-change: transform; transform-style: flat; outline: 1px solid transparent; -webkit-backface-visibility: visible; backface-visibility: visible; }

@keyframes spinCirclesY { 0% { transform: rotateY(0deg) translateZ(0); } 100% { transform: rotateY(360deg) translateZ(0); } }
.circle-blue { width: 100px; height: 100px; margin-top: -50px; margin-left: -50px; border: 8px solid rgba(255, 235, 59, 0.8); box-shadow: 0 0 15px rgba(255, 235, 59, 0.5); animation: spinCirclesY 6s linear infinite; }
.circle-green { width: 135px; height: 135px; margin-top: -67.5px; margin-left: -67.5px; border: 6px solid rgba(32, 201, 151, 0.8); box-shadow: 0 0 15px rgba(32, 201, 151, 0.5); animation: spinCirclesY 11s linear infinite; }
.circle-yellow { width: 170px; height: 170px; margin-top: -85px; margin-left: -85px; border: 4px solid rgba(0, 123, 255, 0.8); box-shadow: 0 0 15px rgba(0, 123, 255, 0.5); animation: spinCirclesY 8s linear infinite; }

.reveal { opacity: 1; transform: translateY(0); }

@media (max-width: 767px) {
  .hero-container { padding: 20px; }
  .intro-section { width: 100%; padding: 40px 20px; border-radius: 25px; backdrop-filter: blur(8px) saturate(120%); }
  .intro-section h1 { font-size: 1.8rem; }
  .intro-section p { font-size: 1rem; margin-bottom: 15px !important; }
  .btn-group { flex-direction: column; gap: 12px; width: 100%; }
  .btn-tech { width: 100% !important; justify-content: center; padding: 14px 20px !important; font-size: 1rem !important; box-sizing: border-box; }
}
</style>