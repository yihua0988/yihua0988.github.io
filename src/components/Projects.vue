<template>
  <section id="projects">
    <div class="section-title reveal">
      <h2>實作專案與技術分析<br>PROJECTS & ANALYSIS</h2>
    </div>
    
    <div class="project-grid">
      <!-- 🚀 v-for 迴圈生成卡片 -->
      <div 
        v-for="(project, index) in projectList" 
        :key="index" 
        class="cyber-card tech-card reveal" 
        :class="`delay-${(index + 1) * 100}`"
      >
        <div class="project-card-content">
          <i :class="[project.icon, 'card-icon']"></i>
          
          <h3>{{ project.title }}</h3>
          
          <!-- v-html 允許我們把原本帶有 <strong> 的字串渲染成 HTML -->
          <p v-html="project.description"></p>
          
          <!-- 更新預告小提示 (只有設定了 updateHint 才會出現) -->
          <p v-if="project.updateHint" class="update-hint" style="font-size: 0.85rem; opacity: 0.85; margin-top: -8px; margin-bottom: 15px;">
            <i class="fas fa-sync fa-spin" style="margin-right: 5px;"></i> {{ project.updateHint }}
          </p>

          <div class="tags">
            <span v-for="(tag, tagIndex) in project.tags" :key="tagIndex">
              {{ tag }}
            </span>
          </div>
          
          <a :href="project.link" target="_blank" rel="noopener noreferrer">
            {{ project.btnText }} <i class="fas" :class="project.btnIcon"></i>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

// 🚀 將你原本寫死在 HTML 的專案資料，整理成這個 Vue 陣列
const projectList = ref([
  {
    icon: 'fas fa-user-shield',
    title: '詐騙防制數據專案',
    description: '運用 Python 針對政府 Opendata 進行 ETL 數據清洗。前端全面改以 <strong>JS 動態數據視覺化</strong> 技術自主渲染互動式圖表，取代傳統套裝軟體。目前正進行後端架構擴充，規劃串接<strong>第二組 Supabase SQL 資料庫</strong>，以強化專案的結構化數據管理與深度整合。',
    updateHint: '系統架構升級中，預計 115 年 11 月釋出更新',
    tags: ['Python ETL', 'JS 動態數據視覺化', 'Supabase SQL'],
    link: 'https://yihua0988.github.io/-2025-7-29-/',
    btnText: '觀看當前版本 (CURRENT DEMO)',
    btnIcon: 'fa-arrow-right'
  },
  {
    icon: 'fas fa-gamepad',
    title: 'Vanilla JS 響應式遊戲與效能控制',
    description: '完全不依賴遊戲引擎，純粹使用 <strong>Vanilla JS</strong> 與 Canvas 打造的 <strong>RWD 響應式網頁遊戲</strong>。除了完美適應各式螢幕尺寸，這個專案最大的技術亮點在於<strong>「動態效能分流」</strong>：特別撰寫了底層偵測機制，讓低資源的行動裝置載入輕量模式以確保穩定的 60FPS 流暢度，而桌上型電腦則解除限制全速渲染。這是一次對 JS 畫面更新、RWD 佈局與底層效能控制的深度實作驗證。',
    updateHint: null, // 沒有預告就不會顯示
    tags: ['Vanilla JS', 'RWD 響應式', 'Canvas 渲染', '動態效能優化'],
    link: 'https://yihua0988.github.io/1150527game/',
    btnText: '開始遊玩 (PLAY GAME)',
    btnIcon: 'fa-play'
  },
  {
    icon: 'fas fa-cart-shopping',
    title: '活力購物網 - 響應式電商前端',
    description: '具備質感的響應式電子商務平台。採用 Bootstrap 5 進行格線佈局，並透過原生 JavaScript 深度串接 <strong>Supabase SQL 資料庫</strong>。專案核心聚焦於建構<strong>完整的電商購物車邏輯</strong>，從商品選購、狀態管理到結帳拋單，完美實現前後端資料同步，支援訂單狀態即時渲染與<strong>前端直接寫入資料庫</strong>的實務應用。',
    updateHint: null,
    tags: ['JavaScript', 'Supabase (BaaS)', 'SQL', 'Bootstrap 5'],
    link: 'https://yihua0988.github.io/1150311JSSQL',
    btnText: '觀看專案實作 (VIEW SITE)',
    btnIcon: 'fa-arrow-right'
  },
  {
    icon: 'fas fa-mobile-alt',
    title: '互動式問答 Android 應用程式',
    description: '使用 MIT App Inventor 2 開發，為一套<strong>可供實體手機直接安裝執行 (APK)</strong> 的 Android 應用程式。系統核心運用 <strong>TinyDB 進行本地資料持久化</strong>以追蹤使用者答題進度與狀態；同時針對測驗情境，深度整合了多媒體邏輯、<strong>影音防作弊機制</strong>，以及震動等<strong>底層硬體控制</strong>，完整展現行動裝置的軟硬體整合開發能力。',
    updateHint: null,
    tags: ['App Inventor 2', 'TinyDB 存儲', 'Android APK'],
    link: 'https://github.com/yihua0988/yihua0988.github.io/tree/main/%E4%BD%9C%E5%93%81%E9%9B%86/apk',
    btnText: '下載 APK 安裝檔 (DOWNLOAD)',
    btnIcon: 'fa-download'
  },
  {
    icon: 'fas fa-hard-hat',
    title: 'AIoT 主動式工安防護系統 (概念架構)',
    description: '以第21屆育秀盃銅獎作品為基礎，針對「工地公安防護」提出的 AIoT 概念性架構。專案核心探討如何整合 <strong>YOLO 影像辨識</strong>與 <strong>MQTT 機電連動</strong>，將傳統被動通報轉化為「主動式實體警報」。目前系統的邊緣運算與防護迴圈仍在<strong>持續優化與概念驗證 (PoC) 階段</strong>，期望未來能完善更嚴密的資安機制。',
    updateHint: null,
    tags: ['AIoT 架構', '機電整合', '概念驗證 (PoC)'],
    link: 'https://yihua0988.github.io/1150402point/',
    btnText: '觀看專案簡報 (VIEW PPT)',
    btnIcon: 'fa-arrow-right'
  }
]);
</script>


<style scoped>
	/* ===================================================
	   🌟 專案區塊外觀與排版
	=================================================== */
	#projects { padding: 120px 8%; position: relative; z-index: 10; }
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

	.project-grid { 
	  display: grid; 
	  grid-template-columns: repeat(2, 1fr); 
	  gap: 50px; 
	  justify-content: center; 
	  max-width: 1200px; 
	  margin: 0 auto; 
	}

	/* 🚨 暫時讓 reveal 顯示 (我們的滾動動畫還沒搬過來，如果不寫這行卡片會隱形) */
	.reveal { opacity: 1; transform: translateY(0); transition: 0.8s var(--spring); }

	/* ===================================================
	   🌟 基礎卡片樣式
	=================================================== */
	.cyber-card {
	  background: rgba(17, 24, 43, 0.95); 
	  border-radius: 22px; padding: 40px 30px; box-sizing: border-box;
	  border: 1px solid rgba(255, 255, 255, 0.08); box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
	  transition: all 0.4s var(--spring); position: relative; overflow: hidden;
	}
	.project-card-content .card-icon { font-size: 4rem; margin-bottom: 25px; filter: drop-shadow(0 0 10px currentColor); transition: 0.4s var(--spring);}
	.project-grid .cyber-card:hover { transform: translateY(-10px); }
	.project-grid .cyber-card:hover .card-icon { transform: scale(1.1) rotate(-5deg); }

	.project-card-content h3 { font-size: 2.2rem; margin-top: 0; margin-bottom: 20px; font-weight: 900; text-shadow: 0 2px 5px rgba(0,0,0,0.8);}
	.project-card-content p { color: var(--text-muted); font-size: 1.15rem; text-align: justify; line-height: 1.9; font-weight: 600;}

	.tags { display: flex; flex-wrap: wrap; justify-content: flex-start; gap: 15px; margin-top: 30px; }
	.tags span { background: rgba(0, 0, 0, 0.5); padding: 8px 18px; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 1px; border-radius: 5px; font-weight: 800; border: 1px solid; transition: 0.2s ease; max-width: 100%; word-break: break-word; white-space: normal; line-height: 1.4; }
	.tags span:hover { color: #fff !important; transform: translateY(-2px); }

	/* 🔗 連結按鈕與點擊特效 */
	.project-card-content a { 
	  font-size: 1.15rem; margin-top: 35px; display: inline-flex; align-items: center; gap: 8px; font-weight: 900; 
	  text-shadow: 0 0 8px currentColor; transition: all 0.15s ease-out; cursor: pointer;
	}
	.project-card-content a:hover { filter: brightness(1.3); transform: translateX(5px); text-shadow: 0 0 15px currentColor;}
	.project-card-content a:active { transform: scale(0.95); filter: brightness(1.5); text-shadow: 0 0 15px currentColor, 0 0 30px currentColor; opacity: 0.8; }

	/* ===================================================
	   🌈 無限循環：五色卡片全自動上色與 Hover 特效
	=================================================== */
	/* 1. 藍色 (Primary) */
	.project-grid .cyber-card:nth-of-type(5n+1) .card-icon,
	.project-grid .cyber-card:nth-of-type(5n+1) h3,
	.project-grid .cyber-card:nth-of-type(5n+1) .update-hint,
	.project-grid .cyber-card:nth-of-type(5n+1) a,
	.project-grid .cyber-card:nth-of-type(5n+1) .tags span { color: var(--accent-primary); }
	.project-grid .cyber-card:nth-of-type(5n+1) .tags span { border-color: var(--accent-primary); }
	.project-grid .cyber-card:nth-of-type(5n+1):hover { border-color: var(--accent-primary); box-shadow: 0 0 30px rgba(0, 123, 255, 0.5), inset 0 0 15px rgba(0, 123, 255, 0.1); }
	.project-grid .cyber-card:nth-of-type(5n+1) .tags span:hover { background: var(--accent-primary); box-shadow: 0 0 15px var(--accent-primary); color: #fff;}

	/* 2. 紫色 (Purple) */
	.project-grid .cyber-card:nth-of-type(5n+2) .card-icon,
	.project-grid .cyber-card:nth-of-type(5n+2) h3,
	.project-grid .cyber-card:nth-of-type(5n+2) a,
	.project-grid .cyber-card:nth-of-type(5n+2) .tags span { color: var(--accent-purple); }
	.project-grid .cyber-card:nth-of-type(5n+2) .tags span { border-color: var(--accent-purple); }
	.project-grid .cyber-card:nth-of-type(5n+2):hover { border-color: var(--accent-purple); box-shadow: 0 0 30px rgba(181, 95, 230, 0.5), inset 0 0 15px rgba(181, 95, 230, 0.1); }
	.project-grid .cyber-card:nth-of-type(5n+2) .tags span:hover { background: var(--accent-purple); box-shadow: 0 0 15px var(--accent-purple); color: #fff;}

	/* 3. 桃紅 (Pink) */
	.project-grid .cyber-card:nth-of-type(5n+3) .card-icon,
	.project-grid .cyber-card:nth-of-type(5n+3) h3,
	.project-grid .cyber-card:nth-of-type(5n+3) a,
	.project-grid .cyber-card:nth-of-type(5n+3) .tags span { color: var(--accent-pink, #ff007f); }
	.project-grid .cyber-card:nth-of-type(5n+3) .tags span { border-color: var(--accent-pink, #ff007f); }
	.project-grid .cyber-card:nth-of-type(5n+3):hover { border-color: var(--accent-pink, #ff007f); box-shadow: 0 0 30px rgba(255, 0, 127, 0.5), inset 0 0 15px rgba(255, 0, 127, 0.1); }
	.project-grid .cyber-card:nth-of-type(5n+3) .tags span:hover { background: var(--accent-pink, #ff007f); box-shadow: 0 0 15px var(--accent-pink, #ff007f); color: #fff;}

	/* 4. 橘色 (Tertiary) */
	.project-grid .cyber-card:nth-of-type(5n+4) .card-icon,
	.project-grid .cyber-card:nth-of-type(5n+4) h3,
	.project-grid .cyber-card:nth-of-type(5n+4) a,
	.project-grid .cyber-card:nth-of-type(5n+4) .tags span { color: var(--accent-tertiary); }
	.project-grid .cyber-card:nth-of-type(5n+4) .tags span { border-color: var(--accent-tertiary); }
	.project-grid .cyber-card:nth-of-type(5n+4):hover { border-color: var(--accent-tertiary); box-shadow: 0 0 30px rgba(253, 126, 20, 0.5), inset 0 0 15px rgba(253, 126, 20, 0.1); }
	.project-grid .cyber-card:nth-of-type(5n+4) .tags span:hover { background: var(--accent-tertiary); box-shadow: 0 0 15px var(--accent-tertiary); color: #fff;}

	/* 5. 綠色 (Secondary) */
	.project-grid .cyber-card:nth-of-type(5n+5) .card-icon,
	.project-grid .cyber-card:nth-of-type(5n+5) h3,
	.project-grid .cyber-card:nth-of-type(5n+5) a,
	.project-grid .cyber-card:nth-of-type(5n+5) .tags span { color: var(--accent-secondary); }
	.project-grid .cyber-card:nth-of-type(5n+5) .tags span { border-color: var(--accent-secondary); }
	.project-grid .cyber-card:nth-of-type(5n+5):hover { border-color: var(--accent-secondary); box-shadow: 0 0 30px rgba(32, 201, 151, 0.5), inset 0 0 15px rgba(32, 201, 151, 0.1); }
	.project-grid .cyber-card:nth-of-type(5n+5) .tags span:hover { background: var(--accent-secondary); box-shadow: 0 0 15px var(--accent-secondary); color: #fff;}

	/* ===================================================
	   📱 RWD 平板與手機版適配
	=================================================== */
	@media (max-width: 1024px) {
	  .project-grid { grid-template-columns: repeat(2, 1fr); gap: 20px; }
	  .cyber-card { padding: 25px; margin: 10px; }
	  .section-title h2 { font-size: 2.2rem; }
	}

	@media (max-width: 767px) {
	  #projects { padding: 60px 15px; }
	  .section-title h2 { font-size: 1.5rem; }
	  .project-grid { display: block; width: 100%; }
	  .cyber-card { width: auto; margin: 0 8px 30px 8px; padding: 30px 20px; }
	  .project-card-content h3 { font-size: 1.4rem; }
	  .project-card-content p { font-size: 1.05rem; }
	}
</style>
