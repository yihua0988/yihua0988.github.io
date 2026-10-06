<template>
  <section id="slash-services">
    <div class="section-title reveal">
      <h2>跨域職能整合</h2>
    </div>
    <div class="slash-header reveal delay-100">
      <h3>📌從底層機電到全端架構</h3>
      <p>將多領域的實務淬鍊，轉化為現代化系統開發與維運的強大養分</p>
    </div>
    
    <div class="slash-grid">
      <!-- 卡片 1：前端與自動化 (紫) -->
      <div class="cyber-card tech-card reveal delay-100">
        <div class="slash-card-content">
          <div class="icon-wrapper">
              <i class="fas fa-laptop-code slash-icon"></i>
          </div>
          <h4>💻前端與自動化開發</h4>
          <p>運用Python進行自動化腳本開發與數據清洗(ETL)，並熟練掌握HTML/CSS打造響應式網頁，具備從資料處理到前端視覺展示的完整實作能力。</p>
        </div>
      </div>

      <!-- 卡片 2：機電整合 (綠) -->
      <div class="cyber-card tech-card reveal delay-200">
        <div class="slash-card-content">
          <div class="icon-wrapper">
              <i class="fas fa-tools slash-icon"></i>
          </div>
          <h4>🔌機電整合與邊緣運算</h4>
          <p>具備<strong>乙級硬體裝修</strong>與<strong>室內配線</strong>證照。不僅精通軟體，更能處理電腦硬體、底層機房電力、網路佈線。</p>
        </div>
      </div>

      <!-- 卡片 3：風險演算 (橘) -->
      <div class="cyber-card tech-card reveal delay-300">
        <div class="slash-card-content">
          <div class="icon-wrapper">
              <i class="fas fa-balance-scale slash-icon"></i>
          </div>
          <h4>⚖️風險演算與架構設計</h4>
          <p>將過去處理複雜保險條款與風險邊界的嚴謹邏輯，完美轉化為程式設計。目前正應用於碩士研究中高解釋性的「規則導向防詐引擎」。</p>
        </div>
      </div>

      <!-- 卡片 4：實戰歷練 (藍) -->
      <div class="cyber-card tech-card reveal delay-100">
        <div class="slash-card-content">
          <div class="icon-wrapper">
              <i class="fas fa-globe slash-icon"></i>
          </div>
          <h4>🌐實戰歷練與雙語優勢</h4>
          <p>擁有7年設施維運與第一線問題排除的實務歷練。結合 <strong>JLPT N2</strong>日文檢定認證，能研讀原廠技術文件或資源。</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// 跨域職能區塊結構單純，暫無互動邏輯
</script>

<style scoped>
.section-title { text-align: center; margin-bottom: 80px; }
.section-title h2 {
  font-size: 3rem; font-weight: 900; letter-spacing: 3px; display: inline-block; position: relative; 
  color: #fff; line-height: 1.3; text-shadow: 0 0 15px rgba(0, 123, 255, 0.7); 
}
.section-title h2::after {
  content: ''; width: 80px; height: 4px; background: var(--accent-primary);
  position: absolute; bottom: -20px; left: 50%; transform: translateX(-50%); border-radius: 5px;
  box-shadow: 0 0 10px var(--accent-primary);
}

#slash-services { padding: 120px 8%; position: relative; z-index: 10; }
.slash-header { text-align: center; margin-bottom: 60px; }
.slash-header h3 { font-size: 2.2rem; color: #ff9f43; text-shadow: 0 0 10px rgba(253, 126, 20, 0.5); margin-bottom: 15px; font-weight: 900;}
.slash-header p { font-size: 1.3rem; color: var(--text-muted); font-weight: 700;}

.slash-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 40px; justify-content: center; max-width: 1200px; margin: 0 auto; }
.slash-card-content { text-align: center; height: 100%; }
.icon-wrapper { width: 90px; height: 90px; border-radius: 50%; display: inline-flex; justify-content: center; align-items: center; margin-bottom: 25px; transition: 0.4s var(--spring); background: rgba(0, 0, 0, 0.5); box-shadow: inset 3px 3px 10px rgba(0, 0, 0, 0.8); border: 1px solid rgba(255,255,255,0.05); }
.slash-icon { font-size: 2.8rem; line-height: 1; filter: drop-shadow(0 0 8px currentColor); }
.slash-card-content h4 { font-size: 1.5rem; margin: 0 0 15px; color: #fff; font-weight: 900; text-shadow: 0 2px 4px rgba(0,0,0,0.5);}
.slash-card-content p { color: var(--text-muted); font-size: 1.15rem; margin: 0; line-height: 1.7; font-weight: 600;}

/* 四張卡片獨立邊框與發光色彩 */
.slash-grid .cyber-card:nth-of-type(1) { border: 1px solid var(--accent-purple); box-shadow: 0 0 15px rgba(181, 95, 230, 0.15); }
.slash-grid .cyber-card:nth-of-type(1) .slash-icon { color: var(--accent-purple); }
.slash-grid .cyber-card:nth-of-type(1):hover { transform: translateY(-10px); box-shadow: 0 0 30px rgba(181, 95, 230, 0.6), inset 0 0 15px rgba(181, 95, 230, 0.2); }

.slash-grid .cyber-card:nth-of-type(2) { border: 1px solid var(--accent-secondary); box-shadow: 0 0 15px rgba(32, 201, 151, 0.15); }
.slash-grid .cyber-card:nth-of-type(2) .slash-icon { color: var(--accent-secondary); }
.slash-grid .cyber-card:nth-of-type(2):hover { transform: translateY(-10px); box-shadow: 0 0 30px rgba(32, 201, 151, 0.6), inset 0 0 15px rgba(32, 201, 151, 0.2); }

.slash-grid .cyber-card:nth-of-type(3) { border: 1px solid var(--accent-tertiary); box-shadow: 0 0 15px rgba(253, 126, 20, 0.15); }
.slash-grid .cyber-card:nth-of-type(3) .slash-icon { color: var(--accent-tertiary); }
.slash-grid .cyber-card:nth-of-type(3):hover { transform: translateY(-10px); box-shadow: 0 0 30px rgba(253, 126, 20, 0.6), inset 0 0 15px rgba(253, 126, 20, 0.2); }

.slash-grid .cyber-card:nth-of-type(4) { border: 1px solid var(--accent-primary); box-shadow: 0 0 15px rgba(0, 123, 255, 0.15); }
.slash-grid .cyber-card:nth-of-type(4) .slash-icon { color: var(--accent-primary); }
.slash-grid .cyber-card:nth-of-type(4):hover { transform: translateY(-10px); box-shadow: 0 0 30px rgba(0, 123, 255, 0.6), inset 0 0 15px rgba(0, 123, 255, 0.2); }

.cyber-card {
  background: rgba(17, 24, 43, 0.95); 
  border-radius: 22px; padding: 40px 30px; box-sizing: border-box;
  transition: all 0.4s var(--spring); position: relative; overflow: hidden;
}
.reveal { opacity: 1; transform: translateY(0); }

@media (max-width: 767px) {
  .slash-grid { display: block !important; width: 100% !important; }
  .cyber-card { width: auto !important; margin: 0 8px 30px 8px !important; padding: 30px 20px !important; }
}
</style>