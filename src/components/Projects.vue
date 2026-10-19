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
          
         <p v-html="project.description"></p>
          
         <!-- 🌟 動態數據與洞察區塊 -->
         <div v-if="project.dynamicStats" class="dynamic-stats-container">
           <div v-for="(stat, sIdx) in project.dynamicStats" :key="sIdx" class="stat-item">
             <span class="stat-icon">{{ stat.icon }}</span>
             <span class="stat-label">{{ stat.label }}：</span>
             <span class="stat-value" v-html="stat.value"></span>
           </div>
         </div>

         <div class="tags">
           <span v-for="(tag, tagIndex) in project.tags" :key="tagIndex">
              {{ tag }}
           </span>
         </div>
          
         <a :href="project.link" target="_blank" rel="noopener noreferrer">
            {{ project.btnText }}<i class="fas" :class="project.btnIcon"></i>
         </a>
       </div>
     </div>
   </div>
 </section>
</template>
<script setup>
import { ref, onMounted } from 'vue'

const SUPABASE_URL = import.meta.env.VITE_SUPABASE_URL
const SUPABASE_ANON_KEY = import.meta.env.VITE_SUPABASE_ANON_KEY || import.meta.env.VITE_SUPABASE_KEY

// 🌟 初始化你的 5 個實作專案卡片版面
const projectList = ref([
  {
    icon:'fas fa-user-shield',
    title:'詐騙防制數據專案',
    description:'全面採用<strong>Vue3環境架構</strong>進行重構，運用Python針對政府Opendata進行ETL數據清洗。前端全面改結合資料庫以<strong>JavaScript動態數據視覺化</strong>技術自主渲染互動式圖表。',
    dynamicStats:[
      { icon:'🔵', label:'受害人被騙金額', value:'數據讀取中...' },
      { icon:'🟠', label:'查扣不法所得', value:'數據讀取中...' },
      { icon:'🔍', label:'雙軸交叉洞察', value:'分析中...' },
      { icon:'📅', label:'資料計算期間', value:'計算中...' },
      { icon:'🕒', label:'與資料庫同步', value:'時間連線中...' }
    ],
    tags:['Vue3架構', 'PythonETL', 'PostgreSQL'],
    link:'https://yihua0988.github.io/PFvue/',
    btnText:'觀看當前版本(CURRENT DEMO)',
    btnIcon:'fa-arrow-right'
  },
  {
    icon:'fas fa-gamepad',
    title:'Vanilla JavaScript 網頁遊戲與效能控制',
    description:'完全不依賴遊戲引擎，純粹使用<strong>Vanilla JavaScript</strong>與Canvas打造的<strong>跨裝置網頁遊戲</strong>。除了完美適應各式螢幕尺寸，這個專案最大的技術亮點在於<strong>「動態效能分流」</strong>：特別撰寫了底層偵測機制，讓低資源的行動裝置載入輕量模式以確保穩定的24FPS流暢度，而桌上型電腦則解除限制全速渲染。這是一次對JavaScript畫面更新、跨螢幕佈局與底層效能控制的深度實作驗證。',
    tags:['Vanilla', 'Canvas', '效能分流'],
    link:'https://yihua0988.github.io/1150527game/',
    btnText:'開始遊玩(PLAY GAME)',
    btnIcon:'fa-play'
  },
  {
    icon:'fas fa-cart-shopping',
    title:'活力購物網 - 動態電商前端',
    description:'具備質感的動態電子商務平台。採用Bootstrap5進行網頁佈局，並在jQuery環境下靈活操作DOM與非同步請求，深度串接<strong>PostgreSQL雲端資料庫(BaaS)</strong>。專案核心聚焦於建構<strong>完整的電商購物車邏輯</strong>，從商品選購、狀態管理到結帳拋單，完美實現前後端資料同步，支援訂單即時渲染與<strong>前端直接寫入資料庫</strong>的實務應用。',
    tags:['jQuery', 'BaaS', 'Bootstrap5'],
    link:'https://yihua0988.github.io/1150311JavaScriptSQL',
    btnText:'觀看專案實作(VIEW SITE)',
    btnIcon:'fa-arrow-right'
  },
  {
    icon:'fas fa-mobile-alt',
    title:'互動式問答 Android 應用程式',
    description:'使用MIT App Inventor2開發，為一套<strong>可供實體手機直接安裝執行(APK)</strong>的Android應用程式。系統核心運用本地資料持久化技術以追蹤使用者答題進度與狀態;同時針對測驗情境，深度整合了多媒體邏輯、<strong>影音防作弊機制</strong>，以及震動等<strong>底層硬體控制</strong>，完整展現行動裝置的軟硬體整合開發能力。',
    tags:['Android APK','底層硬體控制'],
    link:'https://github.com/yihua0988/yihua0988.github.io/tree/main/%E4%BD%9C%E5%93%81%E9%9B%86/apk',
    btnText:'下載APK安裝檔(DOWNLOAD)',
    btnIcon:'fa-download'
  },
  {
    icon:'fas fa-hard-hat',
    title:'AIoT 主動式工安防護系統 (概念架構)',
    description:'以第21屆育秀盃銅獎作品為基礎，針對「工地公安防護」提出的AIoT概念性架構。專案核心探討如何整合<strong>YOLO影像辨識</strong>與<strong>MQTT機電連動</strong>，將傳統被動通報轉化為<strong>「主動式實體警報」</strong>。目前系統的邊緣運算與防護迴圈仍在持續優化與概念驗證階段，<strong>未來尚有更多的驗證性與擴充空間</strong>，期望能完善更嚴密的資安機制。',
    tags:['AIoT概念', 'YOLO辨識', 'MQTT協定'],
    link:'https://yihua0988.github.io/1150402point/',
    btnText:'觀看專案簡報(VIEW PPT)',
    btnIcon:'fa-arrow-right'
  }
])

// 📅 日期解析工具函數
function parseDateAndQuarter(row) {
  let yr = Number(row.年度 || row.年份 || row.年 || 0)
  let mo = Number(row.月份 || row.月 || 1)
  const dateStr = String(row.統計期 || row.年月 || row.期間 || row.日期 || '')
  const mMatch = dateStr.match(/(\d{2,4})\s*[年/\-.]\s*(\d{1,2})/)

  if (mMatch) {
    if (!yr) yr = parseInt(mMatch[1], 10)
    mo = parseInt(mMatch[2], 10)
  }
  if (yr >0 && yr< 1911) yr += 1911
  return { yr, mo }
}

function normalizeTableRows(rows) {
  const records = []
  const metaKeys = new Set([
    'id', '年度', '年份', '年', '月份', '月', '季', '季度', '季別',
    '統計期', '年月', '期間', '日期', '單位', '數值', 'created_at', 'updated_at'
  ])

  rows.forEach(row =>{
    const { yr, mo } = parseDateAndQuarter(row)
    if (!yr) return

    if (row.數值 !== undefined && row.數值 !== null) {
      const val = Number(String(row.數值).replace(/,/g, '')) || 0
      const unit = String(row.單位 || '件').trim()
      if (unit.toUpperCase() === 'GB') return

      let name = ''
      Object.entries(row).forEach(([k, v]) =>{
        if (!metaKeys.has(k) && v !== null && v !== undefined) {
          const s = String(v).trim()
          if (s && s !== '總計' && s !== '合計') name = s
        }
      })

      if (unit === '元') {
        if (name.includes('查扣') || name.includes('不法所得')) name = '查扣不法所得'
        else name = '受害人被騙金額'
      }
      records.push({ yr, mo, name, unit, val })
    } else {
      Object.entries(row).forEach(([k, v]) =>{
        if (metaKeys.has(k) || v === null || v === undefined) return
        const num = Number(String(v).replace(/,/g, '').replace(/%/g, ''))
        if (!isNaN(num)) {
          let unit = '件'
          if (k.includes('額') || k.includes('元')) unit = '元'

          let name = k.trim()
          if (unit === '元') {
            if (name.includes('查扣') || name.includes('不法所得')) name = '查扣不法所得'
            else name = '受害人被騙金額'
          }
          records.push({ yr, mo, name, unit, val:num })
        }
      })
    }
  })
  return records
}

async function fetchAllRows(tableName, headers) {
  const pageSize = 1000
  let offset = 0
  let allData = []
  while (true) {
    const url = `${SUPABASE_URL}/rest/v1/${tableName}?select=*&limit=${pageSize}&offset=${offset}`
    const res = await fetch(url, { headers })
    if (!res.ok) throw new Error(`讀取資料表 ${tableName} 失敗`)
    const chunk = await res.json()
    allData = allData.concat(chunk)
    if (chunk.length< pageSize) break
    offset += pageSize
  }
  return allData
}

// 🚀 100% 動態計算金額、區間與皮爾森相關係數 r
onMounted(async () =>{
  const stats = projectList.value[0].dynamicStats

  if (!SUPABASE_URL || !SUPABASE_ANON_KEY) {
    return
  }

  try {
    const headers = {
      apikey:SUPABASE_ANON_KEY,
      Authorization:`Bearer ${SUPABASE_ANON_KEY}`
    }

    const perfRaw = await fetchAllRows('anti_fraud_performance', headers)
    const records = normalizeTableRows(perfRaw)

    if (records.length >0) {
      const startMIdx = 2025 * 12 + 8  // 2025年9月 (114/09)
      const endMIdx = 2026 * 12 + 7    // 2026年8月 (115/08)

      const filtered = records.filter(r =>{
        const mIdx = r.yr * 12 + (r.mo - 1)
        return mIdx >= startMIdx && mIdx<= endMIdx
      })

      // 依月份分組對齊被騙金額與查扣金額，用來動態計算相關係數 r
      const monthlyMap = {}
      filtered.forEach(r =>{
        const key = `${r.yr}-${r.mo}`
        if (!monthlyMap[key]) monthlyMap[key] = { victim:0, seized:0 }
        if (r.name === '受害人被騙金額') monthlyMap[key].victim += r.val
        if (r.name === '查扣不法所得') monthlyMap[key].seized += r.val
      })

      const monthsArr = Object.values(monthlyMap)
      let totalVictim = 0
      let totalSeized = 0
      monthsArr.forEach(m =>{
        totalVictim += m.victim
        totalSeized += m.seized
      })

      // 計算皮爾森相關係數 r
      const n = monthsArr.length
      let rVal = 0
      if (n >1) {
        const vMean = totalVictim / n
        const sMean = totalSeized / n
        let num = 0, denV = 0, denS = 0
        monthsArr.forEach(m =>{
          const dv = m.victim - vMean
          const ds = m.seized - sMean
          num += dv * ds
          denV += dv * dv
          denS += ds * ds
        })
        rVal = (denV >0 && denS >0) ? Number((num / Math.sqrt(denV * denS)).toFixed(2)) :0
      }

      const vYi = (totalVictim / 100000000).toFixed(2)
      const vAvg = (totalVictim / 100000000 / 12).toFixed(2)
      const sYi = (totalSeized / 100000000).toFixed(2)
      const sAvg = (totalSeized / 100000000 / 12).toFixed(2)
      const ratio = totalVictim >0 ? ((totalSeized / totalVictim) * 100).toFixed(2) :'計算中...'

      // 動態抓出過濾後資料的最早與最新年月
      let minYr = 9999, minMo = 12, maxYr = 0, maxMo = 0
      filtered.forEach(r =>{
        if (r.yr< minYr || (r.yr === minYr && r.mo< minMo)) { minYr = r.yr; minMo = r.mo }
        if (r.yr >maxYr || (r.yr === maxYr && r.mo >maxMo)) { maxYr = r.yr; maxMo = r.mo }
      })

      const startStr = `${minYr - 1911}年${String(minMo).padStart(2, '0')}月`
      const endStr = `${maxYr - 1911}年${String(maxMo).padStart(2, '0')}月`

      stats[0].value = `期間總計<strong style="color:#38bdf8;">${vYi} 億元</strong>(月均 ${vAvg} 億)`
      stats[1].value = `期間總計<strong style="color:#fb923c;">${sYi} 億元</strong>(月均 ${sAvg} 億)`
      stats[2].value = `期間查扣佔比達<strong style="color:var(--accent-secondary);">${ratio}%</strong>｜各自獨立波動 (r = ${rVal})`
      stats[3].value = `<strong style="color:#38bdf8;">${startStr} ~ ${endStr}</strong>`
    }

    // 抓取與資料庫同步的最後更新時間
    const locRes = await fetch(`${SUPABASE_URL}/rest/v1/police_location?select=updated_at&order=updated_at.desc&limit=1`, { headers })
    if (locRes.ok) {
      const locData = await locRes.json()
      if (locData && locData.length >0 && locData[0].updated_at) {
        const rawDate = new Date(locData[0].updated_at)
        const formattedTime = rawDate.toLocaleString('zh-TW', {
          year:'numeric',
          month:'2-digit',
          day:'2-digit',
          hour:'2-digit',
          minute:'2-digit',
          hour12:false
        })
        stats[4].value = `<strong style="color:var(--accent-primary);">${formattedTime}</strong>`
      } else {
        stats[4].value = '<strong style="color:#94a3b8;">2026/10/18 12:00</strong>'
      }
    }

  } catch (err) {
    console.error('動態資料計算失敗:', err)
  }
})
</script>
<style scoped>
	/* ===================================================
	   🌟 專案區塊外觀與排版
	=================================================== */
	#projects { padding:120px 8%; position:relative; z-index:10; }
	.section-title { text-align:center; margin-bottom:80px; }
	.section-title h2 {
	  font-size:3rem; font-weight:900; letter-spacing:3px; display:inline-block; position:relative; 
	  color:#fff; line-height:1.3; text-shadow:0 0 15px rgba(0, 123, 255, 0.7); 
	}
	.section-title h2::after {
	  content:''; width:80px; height:4px; background:var(--accent-primary);
	  position:absolute; bottom:-20px; left:50%; transform:translateX(-50%); border-radius:5px;
	  box-shadow:0 0 10px var(--accent-primary);
	}

	.project-grid { 
	  display:grid; 
	  grid-template-columns:repeat(2, 1fr); 
	  gap:50px; 
	  justify-content:center; 
	  max-width:1200px; 
	  margin:0 auto; 
	}

	.reveal { opacity:1; transform:translateY(0); transition:0.8s var(--spring); }

	/* ===================================================
	   🌟 基礎卡片樣式
	=================================================== */
	.cyber-card {
	  background:rgba(17, 24, 43, 0.95); 
	  border-radius:22px; padding:40px 30px; box-sizing:border-box;
	  border:1px solid rgba(255, 255, 255, 0.08); box-shadow:0 10px 40px rgba(0, 0, 0, 0.5);
	  transition:all 0.4s var(--spring); position:relative; overflow:hidden;
	}
	.project-card-content .card-icon { font-size:4rem; margin-bottom:25px; filter:drop-shadow(0 0 10px currentColor); transition:0.4s var(--spring);}
	.project-grid .cyber-card:hover { transform:translateY(-10px); }
	.project-grid .cyber-card:hover .card-icon { transform:scale(1.1) rotate(-5deg); }

	.project-card-content h3 { font-size:2.2rem; margin-top:0; margin-bottom:20px; font-weight:900; text-shadow:0 2px 5px rgba(0,0,0,0.8);}
	.project-card-content p { color:var(--text-muted); font-size:1.15rem; text-align:justify; line-height:1.9; font-weight:600; margin-bottom:15px;}

  /* 🌟 動態戰情區塊的專屬樣式 */
  .dynamic-stats-container {
    background:rgba(0, 0, 0, 0.45);
    border-radius:12px;
    padding:16px 20px;
    margin-top:15px;
    border-left:4px solid var(--accent-primary);
    box-shadow:inset 0 0 20px rgba(0, 0, 0, 0.5);
  }
  .stat-item {
    font-size:1rem;
    margin-bottom:10px;
    color:#e2e8f0;
    display:flex;
    align-items:baseline;
    flex-wrap:wrap;
    line-height:1.5;
  }
  .stat-item:last-child { margin-bottom:0; padding-top:8px; border-top:1px dashed rgba(255, 255, 255, 0.1); }
  .stat-icon { margin-right:10px; font-size:1.1rem; }
  .stat-label { font-weight:800; color:#adb5bd; margin-right:6px; white-space:nowrap; }
  .stat-value { font-family:'Courier New', Courier, monospace; font-weight:700; font-size:1rem; }

	.tags { display:flex; flex-wrap:wrap; justify-content:flex-start; gap:15px; margin-top:30px; }
	.tags span { background:rgba(0, 0, 0, 0.5); padding:8px 18px; font-size:0.95rem; text-transform:uppercase; letter-spacing:1px; border-radius:5px; font-weight:800; border:1px solid; transition:0.2s ease; max-width:100%; word-break:break-word; white-space:normal; line-height:1.4; }
	.tags span:hover { color:#fff !important; transform:translateY(-2px); }

	/* 🔗 連結按鈕與點擊特效 */
	.project-card-content a { 
	  font-size:1.15rem; margin-top:35px; display:inline-flex; align-items:center; gap:8px; font-weight:900; 
	  text-shadow:0 0 8px currentColor; transition:all 0.15s ease-out; cursor:pointer;
	}
	.project-card-content a:hover { filter:brightness(1.3); transform:translateX(5px); text-shadow:0 0 15px currentColor;}
	.project-card-content a:active { transform:scale(0.95); filter:brightness(1.5); text-shadow:0 0 15px currentColor, 0 0 30px currentColor; opacity:0.8; }

	/* ===================================================
	   🌈 無限循環：五色卡片全自動上色與 Hover 特效
	=================================================== */
	.project-grid .cyber-card:nth-of-type(5n+1) .card-icon,
	.project-grid .cyber-card:nth-of-type(5n+1) h3,
	.project-grid .cyber-card:nth-of-type(5n+1) a,
	.project-grid .cyber-card:nth-of-type(5n+1) .tags span { color:var(--accent-primary); }
	.project-grid .cyber-card:nth-of-type(5n+1) .tags span { border-color:var(--accent-primary); }
	.project-grid .cyber-card:nth-of-type(5n+1):hover { border-color:var(--accent-primary); box-shadow:0 0 30px rgba(0, 123, 255, 0.5), inset 0 0 15px rgba(0, 123, 255, 0.1); }
	.project-grid .cyber-card:nth-of-type(5n+1) .tags span:hover { background:var(--accent-primary); box-shadow:0 0 15px var(--accent-primary); color:#fff;}

	.project-grid .cyber-card:nth-of-type(5n+2) .card-icon,
	.project-grid .cyber-card:nth-of-type(5n+2) h3,
	.project-grid .cyber-card:nth-of-type(5n+2) a,
	.project-grid .cyber-card:nth-of-type(5n+2) .tags span { color:var(--accent-purple); }
	.project-grid .cyber-card:nth-of-type(5n+2) .tags span { border-color:var(--accent-purple); }
	.project-grid .cyber-card:nth-of-type(5n+2):hover { border-color:var(--accent-purple); box-shadow:0 0 30px rgba(181, 95, 230, 0.5), inset 0 0 15px rgba(181, 95, 230, 0.1); }
	.project-grid .cyber-card:nth-of-type(5n+2) .tags span:hover { background:var(--accent-purple); box-shadow:0 0 15px var(--accent-purple); color:#fff;}

	.project-grid .cyber-card:nth-of-type(5n+3) .card-icon,
	.project-grid .cyber-card:nth-of-type(5n+3) h3,
	.project-grid .cyber-card:nth-of-type(5n+3) a,
	.project-grid .cyber-card:nth-of-type(5n+3) .tags span { color:var(--accent-pink, #ff007f); }
	.project-grid .cyber-card:nth-of-type(5n+3) .tags span { border-color:var(--accent-pink, #ff007f); }
	.project-grid .cyber-card:nth-of-type(5n+3):hover { border-color:var(--accent-pink, #ff007f); box-shadow:0 0 30px rgba(255, 0, 127, 0.5), inset 0 0 15px rgba(255, 0, 127, 0.1); }
	.project-grid .cyber-card:nth-of-type(5n+3) .tags span:hover { background:var(--accent-pink, #ff007f); box-shadow:0 0 15px var(--accent-pink, #ff007f); color:#fff;}

	.project-grid .cyber-card:nth-of-type(5n+4) .card-icon,
	.project-grid .cyber-card:nth-of-type(5n+4) h3,
	.project-grid .cyber-card:nth-of-type(5n+4) a,
	.project-grid .cyber-card:nth-of-type(5n+4) .tags span { color:var(--accent-tertiary); }
	.project-grid .cyber-card:nth-of-type(5n+4) .tags span { border-color:var(--accent-tertiary); }
	.project-grid .cyber-card:nth-of-type(5n+4):hover { border-color:var(--accent-tertiary); box-shadow:0 0 30px rgba(253, 126, 20, 0.5), inset 0 0 15px rgba(253, 126, 20, 0.1); }
	.project-grid .cyber-card:nth-of-type(5n+4) .tags span:hover { background:var(--accent-tertiary); box-shadow:0 0 15px var(--accent-tertiary); color:#fff;}

	.project-grid .cyber-card:nth-of-type(5n+5) .card-icon,
	.project-grid .cyber-card:nth-of-type(5n+5) h3,
	.project-grid .cyber-card:nth-of-type(5n+5) a,
	.project-grid .cyber-card:nth-of-type(5n+5) .tags span { color:var(--accent-secondary); }
	.project-grid .cyber-card:nth-of-type(5n+5) .tags span { border-color:var(--accent-secondary); }
	.project-grid .cyber-card:nth-of-type(5n+5):hover { border-color:var(--accent-secondary); box-shadow:0 0 30px rgba(32, 201, 151, 0.5), inset 0 0 15px rgba(32, 201, 151, 0.1); }
	.project-grid .cyber-card:nth-of-type(5n+5) .tags span:hover { background:var(--accent-secondary); box-shadow:0 0 15px var(--accent-secondary); color:#fff;}

	/* ===================================================
	   📱 RWD 平板與手機版適配
	=================================================== */
	@media (max-width:1024px) {
	  .project-grid { grid-template-columns:repeat(2, 1fr); gap:20px; }
	  .cyber-card { padding:25px; margin:10px; }
	  .section-title h2 { font-size:2.2rem; }
	}

	@media (max-width:767px) {
	  #projects { padding:60px 15px; }
	  .section-title h2 { font-size:1.5rem; }
	  .project-grid { display:block; width:100%; }
	  .cyber-card { width:auto; margin:0 8px 30px 8px; padding:30px 20px; }
	  .project-card-content h3 { font-size:1.4rem; }
	  .project-card-content p { font-size:1.05rem; }
    .dynamic-stats-container { padding:14px 15px; }
    .stat-item { font-size:0.9rem; margin-bottom:8px; }
    .stat-value { font-size:0.9rem; }
	}
</style>