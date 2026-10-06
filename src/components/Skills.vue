<template>
  <section id="skills">
    <div class="section-title reveal">
      <h2>核心能力矩陣<br>SKILLS</h2>
    </div>
    <div class="skill-container">
      
      <!-- 左欄：資訊技術與數據 -->
      <div class="skill-col reveal delay-100">
        <h3><i class="fas fa-code"></i>資訊技術與數據</h3>
        
        <div class="cyber-card skill-item skill-python">
          <div class="skill-info">
            <span><i class="fab fa-python"></i>Python爬蟲與資料處理</span>
            <span>Web Scraping/ETL</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item skill-html">
          <div class="skill-info">
            <span><i class="fab fa-html5"></i>網頁前端技術</span>
            <span>HTML/CSS/RWD</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item skill-powerbi">
          <div class="skill-info">
            <span><i class="fas fa-chart-bar"></i>Power BI商業智慧</span>
            <span>數據視覺化</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item skill-sql">
          <div class="skill-info">
            <span><i class="fas fa-database"></i>SQL/資料庫</span>
            <span>資料庫管理</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item skill-git">
          <div class="skill-info">
            <span><i class="fab fa-git-alt"></i>Excel VBA/Git</span>
            <span>自動化/版本控制</span>
          </div>
        </div>
      </div>
      
      <!-- 右欄：硬體維護及軟實力 -->
      <div class="skill-col reveal delay-200">
        <h3><i class="fas fa-server"></i>硬體維護及軟實力</h3>
        
        <div class="cyber-card skill-item skill-gray">
          <div class="skill-info">
            <span><i class="fas fa-microchip"></i>硬體裝修與故障排除</span>
            <span>電腦裝修/維護</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item skill-gray">
          <div class="skill-info">
            <span><i class="fas fa-plug"></i>機電與弱電維護</span>
            <span>網路佈線/設施巡檢</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item skill-red">
          <div class="skill-info">
            <span><i class="fas fa-shield-alt"></i>資安與工安管理</span>
            <span>防火管理員/工安</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item skill-purple">
          <div class="skill-info">
            <span><i class="fas fa-bug"></i>技術故障排查</span>
            <span>錯誤分析/鎖定核心</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item skill-pink">
          <div class="skill-info">
            <span><i class="fas fa-language"></i>日文技術資訊檢索</span>
            <span>JLPT N2/原廠解法</span>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
#skills { padding: 120px 5%; position: relative; z-index: 10; width: 100%; box-sizing: border-box; overflow-x: hidden; }

.section-title { text-align: center; margin-bottom: 60px; width: 100%; }
.section-title h2 {
  font-size: 2.8rem; font-weight: 900; letter-spacing: 2px; display: inline-block; position: relative; 
  color: #fff; line-height: 1.3; text-shadow: 0 0 15px rgba(0, 123, 255, 0.7); 
  white-space: nowrap; /* 🚀 絕對防止中文字垂直斷行 */
}
.section-title h2::after {
  content: ''; width: 80px; height: 4px; background: var(--accent-primary);
  position: absolute; bottom: -15px; left: 50%; transform: translateX(-50%); border-radius: 5px;
  box-shadow: 0 0 10px var(--accent-primary);
}

.skill-container { display: flex; flex-wrap: wrap; gap: 40px; width: 100%; max-width: 1200px; margin: 0 auto; }
.skill-col { flex: 1; min-width: 320px; box-sizing: border-box; } 
.skill-col h3 { font-size: 1.8rem; color: #fff; text-shadow: 0 0 10px rgba(255,255,255,0.5); border-bottom: 2px solid rgba(255,255,255,0.2); padding-bottom: 12px; margin-bottom: 25px; font-weight: 900; white-space: nowrap; }
.skill-col h3 i { margin-right: 12px; font-size: 2.2rem; vertical-align: middle; color: var(--accent-secondary); filter: drop-shadow(0 0 8px var(--accent-secondary));}

.cyber-card {
  background: rgba(17, 24, 43, 0.95); 
  border-radius: 22px; box-sizing: border-box;
  transition: all 0.4s var(--spring); position: relative; overflow: hidden;
}

.skill-item { margin-bottom: 16px; padding: 18px 20px; border-radius: 12px; width: 100%; border: 1px solid rgba(255, 255, 255, 0.08); }
.skill-item:hover { transform: translateX(8px); }

.skill-info { display: flex; justify-content: space-between; align-items: center; font-weight: 800; color: #fff; font-size: 1.05rem; gap: 8px; }
.skill-info i { filter: drop-shadow(0 0 5px currentColor); font-size: 1.6rem; margin-right: 10px; vertical-align: middle; }
.skill-info span:first-child { display: flex; align-items: center; }
.skill-info span:last-child { 
  font-size: 0.85rem; font-weight: 700; background: rgba(0,0,0,0.6); 
  padding: 4px 10px; border-radius: 5px; transition: 0.4s;
  color: var(--text-muted); border: 1px solid rgba(255,255,255,0.1); 
  white-space: nowrap;
}

/* 發光特效 */
.skill-python:hover { border-color: #3776AB; box-shadow: 0 0 20px rgba(55,118,171,0.4); }
.skill-python:hover .skill-info span:last-child { color: #3776AB; border-color: rgba(55,118,171,0.5); }
.skill-python i { color: #3776AB; }

.skill-html:hover { border-color: #E34F26; box-shadow: 0 0 20px rgba(227,79,38,0.4); }
.skill-html:hover .skill-info span:last-child { color: #E34F26; border-color: rgba(227,79,38,0.5); }
.skill-html i { color: #E34F26; }

.skill-powerbi:hover { border-color: #F2C811; box-shadow: 0 0 20px rgba(242,200,17,0.4); }
.skill-powerbi:hover .skill-info span:last-child { color: #F2C811; border-color: rgba(242,200,17,0.5); }
.skill-powerbi i { color: #F2C811; }

.skill-sql:hover { border-color: #336791; box-shadow: 0 0 20px rgba(51,103,145,0.4); }
.skill-sql:hover .skill-info span:last-child { color: #336791; border-color: rgba(51,103,145,0.5); }
.skill-sql i { color: #336791; }

.skill-git:hover { border-color: #F05032; box-shadow: 0 0 20px rgba(240,80,50,0.4); }
.skill-git:hover .skill-info span:last-child { color: #F05032; border-color: rgba(240,80,50,0.5); }
.skill-git i { color: #F05032; }

.skill-gray:hover { border-color: #adb5bd; box-shadow: 0 0 20px rgba(173,181,189,0.4); }
.skill-gray:hover .skill-info span:last-child { color: #adb5bd; border-color: rgba(173,181,189,0.5); }
.skill-gray i { color: #6c757d; }

.skill-red:hover { border-color: #dc3545; box-shadow: 0 0 20px rgba(220,53,69,0.4); }
.skill-red:hover .skill-info span:last-child { color: #dc3545; border-color: rgba(220,53,69,0.5); }
.skill-red i { color: #dc3545; }

.skill-purple:hover { border-color: #b55fe6; box-shadow: 0 0 20px rgba(181,95,230,0.4); }
.skill-purple:hover .skill-info span:last-child { color: #b55fe6; border-color: rgba(181,95,230,0.5); }
.skill-purple i { color: #6f42c1; }

.skill-pink:hover { border-color: #e83e8c; box-shadow: 0 0 20px rgba(232,62,140,0.4); }
.skill-pink:hover .skill-info span:last-child { color: #e83e8c; border-color: rgba(232,62,140,0.5); }
.skill-pink i { color: #e83e8c; }

.reveal { opacity: 1; transform: translateY(0); }

/* 📱 手機版完美適配 */
@media (max-width: 767px) {
  #skills { padding: 60px 15px; }
  .section-title h2 { font-size: 1.6rem; letter-spacing: 1px; }
  .skill-container { display: flex; flex-direction: column; gap: 30px; }
  .skill-col { min-width: 100%; }
  .skill-col h3 { font-size: 1.3rem; margin-bottom: 15px; }
  .skill-col h3 i { font-size: 1.6rem; }
  .skill-item { padding: 15px; margin-bottom: 12px; }
  .skill-info { flex-direction: column; align-items: flex-start; gap: 10px; font-size: 1rem; }
  .skill-info i { font-size: 1.4rem; }
  .skill-info span:last-child { font-size: 0.75rem; padding: 3px 8px; }
}
</style>