<template>
  <section id="slash-services">
    <div class="section-title reveal">
      <h2>跨域職能整合</h2>
    </div>
    <div class="slash-header reveal delay-100">
      <h3>📌 從底層機電到全端架構</h3>
      <p>將多領域的實務淬鍊，轉化為現代化系統開發與維運的強大養分</p>
    </div>
    
    <div class="slash-grid">
      <div class="cyber-card tech-card reveal delay-100">
        <div class="slash-card-content">
          <div class="icon-wrapper">
              <i class="fas fa-laptop-code slash-icon"></i>
          </div>
          <h4>前端與自動化開發</h4>
          <p>
            在現代數位轉型的浪潮中，自動化與資料處理能力是提升核心競爭力的關鍵。我深入鑽研Python程式語言，具備獨立開發高效能自動化腳本的豐富經驗。無論是針對複雜網頁的動態爬蟲技術，還是龐雜數據的抓取、清洗與轉換（ETL工程），皆能透過模組化設計精準實現。
            <br><br>
            此外，我也熟練掌握HTML、CSS、JavaScript及Vue3等現代化前端技術，具備從無到有建構RWD響應式網頁的實戰能力。這種從底層資料庫串接、數據邏輯處理，一路延伸到前端視覺化介面展示的「全端視角」，使我能夠大幅降低跨部門溝通成本，獨立完成具備高實用性與良好使用者體驗的系統開發專案。
          </p>
        </div>
      </div>

      <div class="cyber-card tech-card reveal delay-200">
        <div class="slash-card-content">
          <div class="icon-wrapper">
              <i class="fas fa-tools slash-icon"></i>
          </div>
          <h4>機電整合與底層架構</h4>
          <p>
            擁有「乙級電腦硬體裝修」與「丙級室內配線」等多項國家技術士專業認證，我的技術版圖不僅侷限於純軟體層面的開發，更深耕於實體硬體架構與底層機電系統的維護與整合。在長達七年的實務歷練中，我累積了處理精密硬體故障、機房基礎電力規劃、弱電系統排查以及企業級實體佈線的深厚底蘊。
            <br><br>
            這種「軟硬兼施」的跨域能力，讓我在開發物聯網（IoT）或與底層連動的系統時，能以宏觀的工程師視角，精準評估軟體程式碼在實際硬體設備上的運行限制與效能瓶頸，進而設計出高穩定性、低延遲且具備強大容錯率的跨界整合架構方案。
          </p>
        </div>
      </div>

      <div class="cyber-card tech-card reveal delay-300">
        <div class="slash-card-content">
          <div class="icon-wrapper">
              <i class="fas fa-lightbulb slash-icon"></i>
          </div>
          <h4>發明設計與系統規劃</h4>
          <p>
            於資訊科技碩士班深造期間，我的研究重心從純理論探討轉向高度實用性的「系統發明與專利設計」。結合過去考取的<strong>金融保險證照（產險、壽險）</strong>、<strong>乙種職業安全衛生主管</strong>與消防設備管理資格，我對於「風險移轉、法規合規性及人身安全防護」有著極其嚴謹的評估邏輯。
            <br><br>
            這份背景讓我能將保險實務中的風險邊界概念，完美轉化為系統設計的防錯機制。目前我致力於研發整合型實體系統（如具備獨立備援防護之火警自動通報架構），並能獨立完成專利說明書與技術規格規劃。同時，未來也計畫將此風險管控邏輯延伸至資訊軟體層面，投入開發具備高解釋性的<strong>「規則導向防詐搜尋引擎」</strong>。無論是硬體專利還是軟體架構，皆專注於創造真正能落地應用的產物。
          </p>
        </div>
      </div>

      <div class="cyber-card tech-card reveal delay-100">
        <div class="slash-card-content">
          <div class="icon-wrapper">
              <i class="fas fa-language slash-icon"></i>
          </div>
          <h4>技術除錯與日文檢索</h4>
          <p>
            超過七年的跨領域職場經歷，鍛鍊出我極其敏銳的問題洞察力與抗壓性。面對未知的系統異常或複雜的底層錯誤時，我能迅速釐清問題根源並制定精準的修復策略。
            <br><br>
            更值得一提的是，我具備<strong>JLPT N2</strong>的專業日文能力。這項語言優勢在資訊開發領域是一項強大的隱藏武器，讓我在面對日系原廠設備、特殊的開源專案或是中文資源匱乏的技術難題時，能夠毫無障礙地直接閱讀日本官方技術手冊、日文開發者論壇的討論。這種跨越語言藩籬的資訊獲取能力，大幅拓寬了我的技術視野與解決罕見Bug的效率。
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
#slash-services { padding: 120px 5%; position: relative; z-index: 10; width: 100%; box-sizing: border-box; overflow-x: hidden; }

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

.slash-header { text-align: center; margin-bottom: 50px; }
.slash-header h3 { font-size: 2.2rem; color: #ff9f43; text-shadow: 0 0 10px rgba(253, 126, 20, 0.5); margin-bottom: 12px; font-weight: 900; }
.slash-header p { font-size: 1.3rem; color: var(--text-muted); font-weight: 700; max-width: 800px; margin: 0 auto; }

.slash-grid { 
  display: grid; 
  grid-template-columns: repeat(2, 1fr); 
  gap: 40px; 
  justify-content: center; 
  max-width: 1300px; 
  margin: 0 auto; 
}

.slash-card-content { display: flex; flex-direction: column; align-items: center; height: 100%; }

.icon-wrapper { width: 90px; height: 90px; border-radius: 50%; display: inline-flex; justify-content: center; align-items: center; margin-bottom: 25px; transition: 0.4s var(--spring); background: rgba(0, 0, 0, 0.5); box-shadow: inset 3px 3px 10px rgba(0, 0, 0, 0.8); border: 1px solid rgba(255,255,255,0.05); }
.slash-icon { font-size: 2.8rem; line-height: 1; filter: drop-shadow(0 0 8px currentColor); }

.slash-card-content h4 { font-size: 1.6rem; margin: 0 0 25px; color: #fff; font-weight: 900; text-shadow: 0 2px 4px rgba(0,0,0,0.5); text-align: center; word-break: keep-all; line-height: 1.4;}

.slash-card-content p { 
  color: var(--text-muted); font-size: 1.1rem; margin: 0; line-height: 1.85; 
  font-weight: 600; text-align: justify; letter-spacing: 0.5px;
}
.slash-card-content p strong { color: #fff; font-weight: 800; }

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
  border-radius: 22px; padding: 50px 40px; box-sizing: border-box; 
  transition: all 0.4s var(--spring); position: relative; overflow: hidden;
}

.reveal { opacity: 1; transform: translateY(0); }

/* 📱 手機版完美適配 */
@media (max-width: 992px) {
  .slash-grid { grid-template-columns: 1fr; gap: 30px; }
  .cyber-card { padding: 40px 25px; }
}

@media (max-width: 767px) {
  #slash-services { padding: 60px 15px; }
  .section-title h2 { font-size: 1.6rem; letter-spacing: 1px; }
  .slash-header h3 { font-size: 1.3rem; white-space: nowrap; word-break: keep-all; }
  .slash-header p { font-size: 0.95rem; }
  .slash-grid { display: flex; flex-direction: column; gap: 20px; }
  .cyber-card { width: 100%; padding: 25px 20px; border-radius: 18px; }
  .slash-card-content h4 { font-size: 1.4rem; }
  .slash-card-content p { font-size: 1.05rem; line-height: 1.7; }
}
</style>