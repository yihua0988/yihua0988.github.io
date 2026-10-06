<template>
  <footer>
    <div class="logo" style="margin-bottom: 25px; font-size:2rem; color:#fff; font-weight: 900; letter-spacing: 2px;">洪益華個人技能分享</div>
    <div class="footer-social">
      <div id="btn-email-footer" @click="copyEmail" style="margin-bottom: 25px; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 12px;">
        <i class="fas fa-envelope" style="color:#fff; font-size: 1.6rem;"></i>
        <span style="color:#fff; font-size: 1.3rem; border-bottom: 2px dashed rgba(255,255,255,0.4); padding-bottom: 2px;">yihua0988@gmail.com</span>
      </div>
      <br>
      <a href="https://github.com/yihua0988" target="_blank" rel="noopener noreferrer">
        <i class="fab fa-github" style="font-size: 3.2rem;"></i>
      </a>
    </div>
    <div style="display: flex; justify-content: center; width: 100%;">
      <p style="margin-top: 40px; font-size: 1.1rem;">
        &copy;2026洪益華版權所有
      </p>
    </div>
  </footer>

  <!-- 🌟 全域 Toast 提示框 -->
  <div id="toast-notification" :class="{ show: toast.show }">
    {{ toast.message }}
  </div>

  <!-- 🌟 懸浮按鈕：回到頂部 -->
  <button id="back-to-top" class="btn-back-to-top" title="回到最上面" @click="scrollToTop">
    <i class="fas fa-arrow-up"></i>
  </button>

  <!-- 🌟 懸浮按鈕：分享個人網站 -->
  <button id="btn-copy-url" class="fab-copy-url" title="複製並分享網站" @click="copyUrl">
    <i class="fas fa-share-nodes"></i> 分享個人網站
  </button>
</template>

<script setup>
import { ref } from 'vue'

const toast = ref({
  show: false,
  message: ''
})

const showToast = (msg) => {
  toast.value.message = msg
  toast.value.show = true
  setTimeout(() => {
    toast.value.show = false
  }, 3000)
}

const copyEmail = () => {
  navigator.clipboard.writeText("yihua0988@gmail.com").then(() => {
    showToast("✉️ Email已複製！正在呼叫信箱 App...")
    setTimeout(() => window.location.href = "mailto:yihua0988@gmail.com", 1500)
  }).catch(err => console.error('複製失敗', err))
}

const copyUrl = () => {
  navigator.clipboard.writeText(window.location.href).then(() => {
    showToast("✅ 已複製網址，歡迎分享！")
  }).catch(err => console.error('複製失敗', err))
}

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}
</script>

<style scoped>
footer { background: rgba(6, 11, 25, 0.95); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border-top: 1px solid rgba(0, 123, 255, 0.2); box-shadow: 0 -10px 30px rgba(0, 123, 255, 0.1); position: relative; z-index: 10; color: #94a3b8; padding: 80px 0 60px; text-align: center; }
.footer-social a { color: #fff; font-size: 2.8rem; margin: 0 20px; transition: 0.4s var(--spring); display: inline-block; filter: drop-shadow(0 0 5px rgba(255,255,255,0.3));}
.footer-social a:hover { color: var(--accent-primary); transform: translateY(-8px) scale(1.1); filter: drop-shadow(0 0 15px var(--accent-primary));}
footer p { font-size: 1.1rem; margin-top: 40px; font-weight: 700;}

#toast-notification { visibility: hidden; min-width: 280px; background-color: rgba(10,15,30,0.95); color: var(--accent-secondary); text-align: center; font-weight: 900; border-radius: 5px; padding: 15px 30px; position: fixed; z-index: 2000; left: 50%; bottom: 30px; border: 1px solid var(--accent-secondary); transform: translateX(-50%) translateY(20px); font-size: 1.1rem; opacity: 0; transition: 0.4s var(--spring); box-shadow: 0 0 20px rgba(32,201,151,0.4); }
#toast-notification.show { visibility: visible; opacity: 1; transform: translateX(-50%) translateY(-20px); }

.btn-back-to-top, .fab-copy-url {
    position: fixed; bottom: 30px; background: var(--accent-primary); color: white;
    border: 1px solid rgba(255,255,255,0.2); cursor: pointer; z-index: 9999; transition: 0.4s var(--spring);
    box-shadow: 0 0 15px rgba(0, 123, 255, 0.4);
}
.btn-back-to-top { left: 30px; width: 65px; height: 65px; border-radius: 50%; font-size: 1.6rem; display: flex; justify-content: center; align-items: center;}
.fab-copy-url { right: 30px; padding: 0 25px; height: 55px; border-radius: 50px; font-size: 0.95rem; font-weight: 800; display: flex; align-items: center; gap: 8px;}
.btn-back-to-top:hover, .fab-copy-url:hover { transform: translateY(-5px); box-shadow: 0 0 25px rgba(0, 123, 255, 0.8); background: #0056b3; }

@media (max-width: 767px) {
  .fab-copy-url { bottom: 20px; right: 20px; padding: 0 16px; height: 42px; font-size: 0.75rem; }
  .btn-back-to-top { bottom: 20px; left: 20px; width: 50px; height: 50px; font-size: 1.2rem; }
}
@media (max-width: 380px) {
  .fab-copy-url { bottom: 12px !important; right: 12px !important; height: 36px !important; padding: 0 12px !important; font-size: 0.7rem !important; }
  .btn-back-to-top { bottom: 12px !important; left: 12px !important; width: 40px !important; height: 40px !important; font-size: 1.1rem !important; }
}
</style>