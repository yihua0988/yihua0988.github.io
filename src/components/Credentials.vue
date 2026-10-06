<template>
  <section id="credentials">
    <div class="section-title reveal">
      <h2>專業認證矩陣<br>CREDENTIALS</h2>
    </div>
    <div class="cert-matrix">
      
      <div class="cyber-card cert-node cert-orange reveal delay-100">
        <i class="fas fa-fire-extinguisher cert-icon"></i>
        <h4>防火管理員</h4>
        <p>消防安全認證</p>
      </div>

      <div class="cyber-card cert-node cert-orange reveal delay-200">
        <i class="fas fa-hard-hat cert-icon"></i>
        <h4>乙種職安衛主管</h4>
        <p>職業安全衛生</p>
      </div>

      <div class="cyber-card cert-node cert-blue reveal delay-300">
        <i class="fas fa-microchip cert-icon"></i>
        <h4>乙級電腦硬體裝修</h4>
        <p>國家技術士</p>
      </div>

      <div class="cyber-card cert-node cert-blue reveal delay-100">
        <i class="fas fa-code cert-icon"></i>
        <h4>丙級網頁設計</h4>
        <p>國家技術士</p>
      </div>

      <div class="cyber-card cert-node cert-orange reveal delay-200">
        <i class="fas fa-bolt cert-icon"></i>
        <h4>丙級室內配線</h4>
        <p>國家技術士</p>
      </div>

      <div class="cyber-card cert-node cert-green reveal delay-300">
        <i class="fab fa-python cert-icon"></i>
        <h4>ITS Python</h4>
        <p>程式設計認證</p>
      </div>

      <div class="cyber-card cert-node cert-yellow reveal delay-100">
        <i class="fas fa-file-invoice-dollar cert-icon"></i>
        <h4>金融證照群</h4>
        <p>產/壽/外幣/投資型</p>
      </div>

      <div class="cyber-card cert-node cert-purple reveal delay-200">
        <i class="fas fa-language cert-icon"></i>
        <h4>JLPT N2</h4>
        <p>日本語能力試驗</p>
      </div>

    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
#credentials { padding: 120px 5%; position: relative; z-index: 10; width: 100%; box-sizing: border-box; overflow-x: hidden; }

.section-title { text-align: center; margin-bottom: 60px; width: 100%; }
.section-title h2 {
  font-size: 2.8rem; font-weight: 900; letter-spacing: 2px; display: inline-block; position: relative; 
  color: #fff; line-height: 1.3; text-shadow: 0 0 15px rgba(0, 123, 255, 0.7); 
  white-space: nowrap; /* 🚀 絕對防止斷行 */
}
.section-title h2::after {
  content: ''; width: 80px; height: 4px; background: var(--accent-primary);
  position: absolute; bottom: -15px; left: 50%; transform: translateX(-50%); border-radius: 5px;
  box-shadow: 0 0 10px var(--accent-primary);
}

.cert-matrix { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 30px; max-width: 1200px; margin: 0 auto; }
.cert-node { padding: 35px 20px; text-align: center; display: flex; flex-direction: column; align-items: center; }
.cert-node:hover { transform: translateY(-10px); }
.cert-icon { font-size: 3rem; margin-bottom: 20px; transition: 0.4s var(--spring); filter: drop-shadow(0 0 10px currentColor);}
.cert-node:hover .cert-icon { transform: scale(1.2); }
.cert-node h4 { font-size: 1.3rem; margin: 0 0 8px; color: #fff; font-weight: 900; text-shadow: 0 2px 4px rgba(0,0,0,0.8); }
.cert-node p { font-size: 1rem; color: var(--text-muted); margin: 0; font-weight: 700;}

.cert-orange .cert-icon { color: var(--accent-tertiary); }
.cert-orange:hover { border-color: var(--accent-tertiary); box-shadow: 0 0 25px rgba(253, 126, 20, 0.4), inset 0 0 10px rgba(253, 126, 20, 0.1); }
.cert-blue .cert-icon { color: var(--accent-primary); }
.cert-blue:hover { border-color: var(--accent-primary); box-shadow: 0 0 25px rgba(0, 123, 255, 0.4), inset 0 0 10px rgba(0, 123, 255, 0.1); }
.cert-green .cert-icon { color: var(--accent-secondary); }
.cert-green:hover { border-color: var(--accent-secondary); box-shadow: 0 0 25px rgba(32, 201, 151, 0.4), inset 0 0 10px rgba(32, 201, 151, 0.1); }
.cert-yellow .cert-icon { color: #ffc107; }
.cert-yellow:hover { border-color: #ffc107; box-shadow: 0 0 25px rgba(255, 193, 7, 0.4), inset 0 0 10px rgba(255, 193, 7, 0.1); }
.cert-purple .cert-icon { color: var(--accent-purple); }
.cert-purple:hover { border-color: var(--accent-purple); box-shadow: 0 0 25px rgba(181, 95, 230, 0.4), inset 0 0 10px rgba(181, 95, 230, 0.1); }

.cyber-card {
  background: rgba(17, 24, 43, 0.95); 
  border-radius: 22px; box-sizing: border-box;
  border: 1px solid rgba(255, 255, 255, 0.08); box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
  transition: all 0.4s var(--spring); position: relative; overflow: hidden;
}
.reveal { opacity: 1; transform: translateY(0); }

/* 📱 手機版完美適配 */
@media (max-width: 767px) {
  #credentials { padding: 60px 15px; }
  .section-title h2 { font-size: 1.6rem; letter-spacing: 1px; }
  .cert-matrix { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; }
  .cert-node { width: 100%; padding: 15px 10px; border-radius: 16px; }
  .cert-node .cert-icon { font-size: 2rem; margin-bottom: 12px; }
  .cert-node h4 { font-size: 0.9rem; word-break: keep-all; margin-bottom: 4px; }
  .cert-node p { font-size: 0.75rem; }
}
</style>