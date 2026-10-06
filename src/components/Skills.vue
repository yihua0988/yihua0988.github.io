<template>
  <section id="skills">
    <div class="section-title reveal">
      <h2>核心能力矩陣<br>SKILLS</h2>
    </div>
    <div class="skill-container">
      
      <!-- 左欄：資訊技術與數據 -->
      <div class="skill-col reveal delay-100">
        <h3><i class="fas fa-code"></i>資訊技術與數據</h3>
        
        <div class="cyber-card skill-item">
          <div class="skill-info">
            <span><i class="fab fa-python" style="color:#3776AB; font-size:1.8rem; margin-right:12px; vertical-align:middle;"></i>Python爬蟲與資料處理</span>
            <span>Web Scraping/ETL工程</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item">
          <div class="skill-info">
            <span><i class="fab fa-html5" style="color:#E34F26; font-size:1.8rem; margin-right:12px; vertical-align:middle;"></i>網頁前端技術</span>
            <span>HTML/CSS/RWD設計</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item">
          <div class="skill-info">
            <span><i class="fas fa-chart-bar" style="color:#F2C811; font-size:1.8rem; margin-right:12px; vertical-align:middle;"></i>Power BI商業智慧</span>
            <span>數據視覺化</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item">
          <div class="skill-info">
            <span><i class="fas fa-database" style="color:#336791; font-size:1.8rem; margin-right:12px; vertical-align:middle;"></i>SQL/資料庫</span>
            <span>資料庫管理</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item">
          <div class="skill-info">
            <span><i class="fab fa-git-alt" style="color:#F05032; font-size:1.8rem; margin-right:12px; vertical-align:middle;"></i>Excel VBA/Git</span>
            <span>行政自動化/版本控制</span>
          </div>
        </div>
      </div>
      
      <!-- 右欄：硬體維護及軟實力 -->
      <div class="skill-col reveal delay-200">
        <h3><i class="fas fa-server"></i>硬體維護及軟實力</h3>
        
        <div class="cyber-card skill-item">
          <div class="skill-info">
            <span><i class="fas fa-microchip" style="color:#6c757d; font-size:1.8rem; margin-right:12px; vertical-align:middle;"></i>硬體裝修與故障排除</span>
            <span>電腦裝修/系統維護</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item">
          <div class="skill-info">
            <span><i class="fas fa-plug" style="color:#6c757d; font-size:1.8rem; margin-right:12px; vertical-align:middle;"></i>機電與弱電維護</span>
            <span>辦公網路佈線/設施巡檢</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item">
          <div class="skill-info">
            <span><i class="fas fa-shield-alt" style="color:#dc3545; font-size:1.8rem; margin-right:12px; vertical-align:middle;"></i>資安與工安管理</span>
            <span>防火管理員/資安管理</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item">
          <div class="skill-info">
            <span><i class="fas fa-bug" style="color:#6f42c1; font-size:1.8rem; margin-right:12px; vertical-align:middle;"></i>技術故障排查</span>
            <span>錯誤分析/鎖定問題核心</span>
          </div>
        </div>
        
        <div class="cyber-card skill-item">
          <div class="skill-info">
            <span><i class="fas fa-language" style="color:#e83e8c; font-size:1.8rem; margin-right:12px; vertical-align:middle;"></i>日文技術資訊檢索</span>
            <span>JLPT N2/原廠技術解法</span>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>

<script setup>
// 技能區塊為靜態展示，無需額外邏輯
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

#skills { padding: 120px 8%; position: relative; z-index: 10; }
.skill-container { display: flex; flex-wrap: wrap; gap: 60px; width: 100%; box-sizing: border-box; max-width: 1200px; margin: 0 auto; }
.skill-col { flex: 1; min-width: min(100%, 350px); box-sizing: border-box; } 
.skill-col h3 { font-size: 2rem; color: #fff; text-shadow: 0 0 10px rgba(255,255,255,0.5); border-bottom: 2px solid rgba(255,255,255,0.2); padding-bottom: 15px; margin-bottom: 35px; font-weight: 900;}
.skill-col h3 i { margin-right: 15px; font-size: 2.5rem; vertical-align: middle; color: var(--accent-secondary); filter: drop-shadow(0 0 8px var(--accent-secondary));}

.cyber-card {
  background: rgba(17, 24, 43, 0.95); 
  border-radius: 22px; box-sizing: border-box;
  transition: all 0.4s var(--spring); position: relative; overflow: hidden;
}

.skill-item { margin-bottom: 20px; padding: 18px 20px; border-radius: 12px; width: 100%; box-sizing: border-box; border: 1px solid rgba(255, 255, 255, 0.08); }
.skill-item:hover { transform: translateX(10px); border-color: var(--accent-secondary); box-shadow: 0 0 20px rgba(32, 201, 151, 0.4), inset 0 0 10px rgba(32, 201, 151, 0.1); }
.skill-info { display: flex; justify-content: space-between; align-items: center; font-weight: 800; color: #fff; font-size: 1.1rem; flex-wrap: wrap; gap: 8px; }
.skill-info i { filter: drop-shadow(0 0 5px currentColor); }
.skill-info span:last-child { font-size: 0.9rem; color: var(--accent-secondary); font-weight: 700; background: rgba(0,0,0,0.6); padding: 4px 10px; border-radius: 5px; border: 1px solid rgba(32, 201, 151, 0.3); }

.reveal { opacity: 1; transform: translateY(0); }

@media (max-width: 767px) {
  .skill-container { display: block !important; width: 100% !important; }
  .skill-item { margin-bottom: 15px; }
  .skill-info { flex-direction: column !important; align-items: flex-start !important; gap: 8px; margin-bottom: 10px; }
}
</style>