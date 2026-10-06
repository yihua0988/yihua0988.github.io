<template>
  <section id="experience">
    <div class="section-title reveal">
      <h2>職涯歷程<br>CAREER LOG</h2>
    </div>
    
    <!-- 圓餅圖統計列 -->
    <div class="chart-row reveal delay-100">
      <div class="cyber-card chart-container">
        <h4>產業經驗分佈</h4>
        <div id="industry-chart-wrapper" class="custom-pie-container">
            <div class="pie-chart"></div>
            <div class="pie-legend"></div>
        </div>
      </div>
      <div class="cyber-card chart-container">
        <h4>職能性質佔比</h4>
        <div id="job-chart-wrapper" class="custom-pie-container">
            <div class="pie-chart"></div>
            <div class="pie-legend"></div>
        </div>
      </div>
    </div>

    <!-- 職涯時間軸列表 -->
    <div class="exp-list">
      <div class="cyber-card exp-item reveal delay-100">
        <div class="exp-meta">
          <span class="exp-period">2025-至今</span>
          <span class="exp-role">資訊科技碩士班<strong>&</strong><br>全端開發工程師</span>
        </div>
        <div class="exp-content">
          <h3>僑光科技大學<br>重返資訊本業</h3>
          <p>
            <strong>【專攻自動化與數據架構】</strong><br>
            在累積7年豐富的職場工作經驗後，決定重返資訊核心領域深造，目前攻讀資訊科技碩士學位，將實務淬鍊與學術理論完美結合。<br>
            現階段專注於<strong>Python數據清洗(ETL)</strong>與<strong>HTML/CSS網頁前端開發</strong>。能夠獨立建置本地資料庫，並將處理好的資料串接至前端，完成完整的網頁視覺化呈現。
          </p>
        </div>
      </div>

      <div class="cyber-card exp-item reveal delay-200">
        <div class="exp-meta">
          <span class="exp-period">2017-2025</span>
          <span class="exp-role">7年多元實戰<strong>&</strong><br>多角化職能淬鍊</span>
        </div>
        <div class="exp-content">
          <h3>跨領域工作經驗與多元歷練</h3>
          <p>
            <strong>【7年多角化職場實務】</strong><br>
            在這7年的職場生涯中，歷經了不同業態與環境的洗禮，職能涵蓋機電設施維運、技術支援等多樣化領域。具備極強的環境適應力，能在不同業務情境下快速釐清痛點並找出解決方案。<br>
            這段豐富的跨界工作經驗，不僅淬鍊出強大的<strong>邏輯除錯思維與精準的問題洞察力</strong>，更讓我擅長從不同維度理解業務邏輯，成為日後開發軟體與系統架構設計時的重要養分。
          </p>
        </div>
      </div>

      <div class="cyber-card exp-item reveal delay-300">
        <div class="exp-meta">
          <span class="exp-period">早期基礎</span>
          <span class="exp-role">臺中高工<strong>&</strong><br>國家技術士認證</span>
        </div>
        <div class="exp-content">
          <h3>硬體裝修與工程邏輯扎根</h3>
          <p>
            <strong>【技職體系的硬派扎根】</strong><br>
            於高職階段完整淬鍊工程思維，深入研究電腦硬體裝修與伺服器基礎架構。<br>
            在校期間即成功考取<strong>「乙級電腦硬體裝修」</strong>與<strong>「丙級網頁設計」</strong>等國家技術士證照，在最早期便奠定了軟硬體整合的嚴謹邏輯大腦。
          </p>
        </div>
      </div>
    </div>

    <!-- 🚨 修正：懸浮提示框 (Tooltip) 綁定動態顏色 -->
    <div id="chart-tooltip" v-show="tooltip.show" 
         :style="{ 
           left: tooltip.x + 'px', 
           top: tooltip.y + 'px', 
           borderColor: tooltip.color,
           boxShadow: `0 0 20px ${tooltip.color}80` 
         }">
      <span v-html="tooltip.content"></span>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const tooltip = ref({
  show: false,
  x: 0,
  y: 0,
  content: '',
  color: '#007bff' // 預設光暈顏色
})

onMounted(() => {
  // 渲染 SVG 圓餅圖的繪圖引擎
  function renderSvgDonut(wrapperId, dataObj) {
    const wrapper = document.getElementById(wrapperId)
    if (!wrapper) return

    let total = 0
    Object.values(dataObj.data).forEach(v => total += v)

    let cumulativePercent = 0
    let svgPaths = ''
    let legendHtml = ''
    let i = 0

    Object.entries(dataObj.data).forEach(([key, value]) => {
      const percent = value / total
      const color = dataObj.colors[i]
      
      const startX = Math.cos(2 * Math.PI * cumulativePercent)
      const startY = Math.sin(2 * Math.PI * cumulativePercent)
      cumulativePercent += percent
      const endX = Math.cos(2 * Math.PI * cumulativePercent)
      const endY = Math.sin(2 * Math.PI * cumulativePercent)
      const largeArcFlag = percent > 0.5 ? 1 : 0

      const pathData = [
        `M ${startX} ${startY}`,
        `A 1 1 0 ${largeArcFlag} 1 ${endX} ${endY}`,
        `L 0 0`
      ].join(' ')

      let pctString = Math.round(percent * 100) + '%'

      svgPaths += `<path d="${pathData}" fill="${color}" stroke="#060b19" stroke-width="0.05" class="pie-slice" data-key="${key}" data-val="${value}" data-percent="${pctString}" />`

      legendHtml += `
      <div class="legend-item">
          <div class="legend-color" style="background:${color}"></div>
          <span style="flex:1;">${key}</span>
          <span style="color:${color}; font-weight:900; text-shadow: 0 0 5px ${color};">${pctString}</span>
      </div>`
      i++
    })

    const svgHtml = `
    <svg viewBox="-1.2 -1.2 2.4 2.4" style="width: 100%; height: 100%; transform: rotate(-90deg);">
        ${svgPaths}
    </svg>
    `

    wrapper.querySelector('.pie-chart').innerHTML = svgHtml
    wrapper.querySelector('.pie-legend').innerHTML = legendHtml
  }

  // 繪製兩張統計圖表
  renderSvgDonut('industry-chart-wrapper', {
      data: { '百貨服務業': 49, '飯店業': 9, '視廳歌唱業': 14, '人才綜合服務': 10 },
      colors: ['#007bff', '#20c997', '#fd7e14', '#b55fe6']
  })

  renderSvgDonut('job-chart-wrapper', {
      data: { '工務機電': 40, '設備維護': 23, '電話行銷': 10 },
      colors: ['#007bff', '#20c997', '#fd7e14']
  })

  // 🚨 修正：綁定圖表區塊的滑鼠互動事件，自動抓取對應扇形的顏色
  const experienceSection = document.getElementById('experience')
  experienceSection.addEventListener('mousemove', (e) => {
    const slice = e.target.closest('.pie-slice')
    if (slice) {
      let key = slice.getAttribute('data-key')
      let pct = slice.getAttribute('data-percent')
      let sliceColor = slice.getAttribute('fill') // 取得扇形顏色

      tooltip.value = {
        show: true,
        x: e.clientX,
        y: e.clientY,
        color: sliceColor, // 將邊框與光暈設定為該扇形的顏色
        content: `${key}<br><span style="color:${sliceColor}; font-size:1.3rem; text-shadow: 0 0 8px ${sliceColor};">${pct}</span>` // 將文字也變成同顏色
      }
      slice.style.transform = 'scale(1.05)'
      slice.style.filter = 'brightness(1.2)'
    }
  })

  experienceSection.addEventListener('mouseout', (e) => {
    const slice = e.target.closest('.pie-slice')
    if (slice) {
      tooltip.value.show = false
      slice.style.transform = 'scale(1)'
      slice.style.filter = 'brightness(1)'
    }
  })
})
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

#experience { padding: 120px 8%; position: relative; z-index: 10; }

.chart-row { display: flex; flex-wrap: wrap; gap: 60px; justify-content: center; margin-bottom: 80px; max-width: 1200px; margin-left: auto; margin-right: auto; }
.chart-container { flex: 1; min-width: 380px; max-width: 500px; padding: 40px; display: flex; flex-direction: column; align-items: center; }
.chart-container:hover { border-color: var(--accent-primary); box-shadow: 0 0 30px rgba(0,123,255,0.3); transform: translateY(-10px); }
.chart-container h4 { font-size: 1.6rem; margin: 0 0 40px; color: #fff; text-align: center; font-weight: 900; text-shadow: 0 0 10px rgba(255,255,255,0.3);}

.custom-pie-container { display: flex; flex-direction: column; align-items: center; gap: 40px; width: 100%;}
.pie-chart { position: relative; width: 220px; height: 220px; border-radius: 50%; background: rgba(0,0,0,0.5); padding: 15px; box-sizing: border-box; display: flex; justify-content: center; align-items: center; border: 1px solid rgba(255,255,255,0.05); }
.pie-slice { cursor: pointer; transition: 0.3s; transform-origin: center; stroke: #060b19; stroke-width: 0.05;}
.pie-legend { display: flex; flex-direction: column; gap: 12px; width: 100%;}
.legend-item { display: flex; align-items: center; gap: 15px; font-size: 1.1rem; color: #fff; font-weight: 800; padding: 10px 15px; border-radius: 8px; transition: 0.3s; background: rgba(0,0,0,0.3); border: 1px solid transparent;}
.legend-item:hover { background: rgba(0,123,255,0.1); border-color: rgba(0,123,255,0.3); transform: translateX(8px); }
.legend-color { width: 18px; height: 18px; border-radius: 4px; box-shadow: 0 0 8px currentColor;}

/* 🚨 修正：移除原本寫死的陰影與邊框，交給上方的 Vue 自動計算填入 */
#chart-tooltip { position: fixed; background: rgba(10, 15, 30, 0.95); color: #fff; text-align: center; font-weight: 800; border-radius: 8px; padding: 10px 18px; z-index: 9999; pointer-events: none; backdrop-filter: blur(5px); font-size: 1.1rem; transform: translate(-50%, -100%); margin-top: -15px; border: 1px solid transparent; transition: border-color 0.2s, box-shadow 0.2s; }

.exp-list { max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; gap: 40px;}
.exp-item { display: flex; padding: 50px; border-radius: 0 25px 25px 0; border-left: 6px solid var(--accent-primary); align-items: stretch; }

/* 🚨 修正：把突兀的綠光拔掉，改成與左側粗線條一致的「藍光」，質感大提升 */
.exp-item:hover { transform: translateX(15px); border-color: var(--accent-primary); box-shadow: 0 0 30px rgba(0, 123, 255, 0.4), inset 0 0 10px rgba(0, 123, 255, 0.1); }

.exp-meta { min-width: 220px; margin-right: 40px; color: var(--accent-primary); border-right: 2px dashed rgba(255,255,255,0.2); padding-right: 30px; }
.exp-period { font-size: 1.6rem; font-weight: 900; display: block; margin-bottom: 10px; text-shadow: 0 0 8px currentColor;}
.exp-role { font-size: 1.1rem; color: var(--text-muted); display: block; font-weight: 800;}
.exp-content h3 { margin: 0 0 15px 0; color: #fff; font-size: 1.8rem; font-weight: 900; text-shadow: 0 2px 4px rgba(0,0,0,0.8);}
.exp-content p { color: var(--text-muted); margin: 0; font-size: 1.15rem; text-align: justify; line-height: 1.9; font-weight: 600;}

.cyber-card {
  background: rgba(17, 24, 43, 0.95); 
  border-radius: 22px; box-sizing: border-box;
  border: 1px solid rgba(255, 255, 255, 0.08); box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
  transition: all 0.4s var(--spring); position: relative; overflow: hidden;
}

.reveal { opacity: 1; transform: translateY(0); }

@media (max-width: 767px) {
  .chart-row { display: block !important; }
  .chart-container { min-width: 0 !important; margin-bottom: 30px; }
  .pie-chart { width: 200px !important; height: 200px !important; margin-bottom: 20px; }
  .exp-list { width: 100% !important; padding: 0 !important; display: block !important; }
  .exp-item { display: block !important; width: auto !important; margin: 0 8px 30px 8px !important; padding: 25px 20px !important; border-radius: 18px !important; border-left: none !important; border-top: 4px solid var(--accent-primary) !important; }
  .exp-meta { min-width: 0 !important; width: 100% !important; margin: 0 0 15px 0 !important; padding: 0 0 15px 0 !important; border-right: none !important; border-bottom: 2px dashed rgba(255,255,255,0.2) !important; }
}
</style>