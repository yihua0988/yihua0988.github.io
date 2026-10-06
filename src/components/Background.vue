<template>
  <div class="circuit-bg">
    <div class="circuit-grid"></div>
    <svg class="pcb-traces" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="grad-yellow"><stop offset="0%" stop-color="#ffff00"/><stop offset="100%" stop-color="#ffcc00"/></linearGradient>
            <linearGradient id="grad-orange"><stop offset="0%" stop-color="#ff4500"/><stop offset="100%" stop-color="#ff8c00"/></linearGradient>
            <linearGradient id="grad-blue"><stop offset="0%" stop-color="#00f3ff"/><stop offset="100%" stop-color="#007bff"/></linearGradient>
            <linearGradient id="grad-green"><stop offset="0%" stop-color="#39ff14"/><stop offset="100%" stop-color="#00ff66"/></linearGradient>
            <linearGradient id="grad-purple"><stop offset="0%" stop-color="#bf00ff"/><stop offset="100%" stop-color="#8a2be2"/></linearGradient>

            <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
                <feGaussianBlur in="SourceGraphic" stdDeviation="6" result="blur"/>
                <feMerge>
                    <feMergeNode in="blur"/>
                    <feMergeNode in="SourceGraphic"/>
                </feMerge>
            </filter>
        </defs>

        <g class="base-tracks" stroke="rgba(255,255,255,0.03)" stroke-width="2" fill="none">
            <path d="M-100,150 H300 V450 H800 V200 H1500 V600 H2000" />
            <path d="M2000,850 H1400 V500 H900 V900 H400 V700 H-100" />
            <path d="M450,-100 V300 H150 V800 H600 V1200" />
            <path d="M1600,1200 V750 H1800 V350 H1200 V-100" />
            <path d="M-100,550 H200 V850 H700 V300 H1100 V800 H2000" />
            <path d="M1000,-100 V400 H1300 V900 H1700 V1200" />
        </g>

        <g class="current-flows" fill="none" stroke-linecap="round">
            <path class="flow-1" stroke="url(#grad-yellow)" stroke-width="6" d="M-100,150 H300 V450 H800 V200 H1500 V600 H2000" />
            <path class="flow-2" stroke="url(#grad-orange)" stroke-width="5" d="M2000,850 H1400 V500 H900 V900 H400 V700 H-100" />
            <path class="flow-3" stroke="url(#grad-blue)" stroke-width="6" d="M450,-100 V300 H150 V800 H600 V1200" />
            <path class="flow-4" stroke="url(#grad-green)" stroke-width="4" d="M1600,1200 V750 H1800 V350 H1200 V-100" />
            <path class="flow-5" stroke="url(#grad-purple)" stroke-width="7" d="M-100,550 H200 V850 H700 V300 H1100 V800 H2000" />
            <path class="flow-6" stroke="url(#grad-yellow)" stroke-width="5" d="M1000,-100 V400 H1300 V900 H1700 V1200" />
        </g>

        <g class="data-packets" fill="none" stroke-linecap="round" stroke="#ffffff" filter="url(#glow)">
            <path class="packet-1" stroke-width="2" d="M-100,150 H300 V450 H800 V200 H1500 V600 H2000" />
            <path class="packet-2" stroke-width="2" d="M2000,850 H1400 V500 H900 V900 H400 V700 H-100" />
            <path class="packet-3" stroke-width="2" d="M450,-100 V300 H150 V800 H600 V1200" />
            <path class="packet-5" stroke-width="3" d="M-100,550 H200 V850 H700 V300 H1100 V800 H2000" />
        </g>

        <g class="pcb-nodes" filter="url(#glow)">
            <circle cx="300" cy="450" r="5" fill="url(#grad-yellow)" class="node-pulse" />
            <circle cx="800" cy="200" r="6" fill="url(#grad-yellow)" class="node-pulse" style="animation-delay: 1s;" />
            <circle cx="1400" cy="500" r="5" fill="url(#grad-orange)" class="node-pulse" style="animation-delay: 0.5s;" />
            <circle cx="900" cy="900" r="4" fill="url(#grad-orange)" class="node-pulse" style="animation-delay: 1.5s;" />
            <circle cx="150" cy="800" r="5" fill="url(#grad-blue)" class="node-pulse" style="animation-delay: 0.2s;" />
            <circle cx="1800" cy="350" r="4" fill="url(#grad-green)" class="node-pulse" style="animation-delay: 0.8s;" />
            <circle cx="700" cy="300" r="7" fill="url(#grad-purple)" class="node-pulse" style="animation-delay: 1.2s;" />
            <circle cx="1100" cy="800" r="5" fill="url(#grad-purple)" class="node-pulse" style="animation-delay: 0.4s;" />
            <circle cx="1300" cy="900" r="5" fill="url(#grad-yellow)" class="node-pulse" style="animation-delay: 1.8s;" />
        </g>
    </svg>
  </div>
  <!-- Canvas 粒子特效畫布 -->
  <canvas ref="particleCanvas" id="particle-canvas"></canvas>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const particleCanvas = ref(null)
let animationFrameId = null

onMounted(() => {
  const canvas = particleCanvas.value
  if (!canvas) return
  const ctx = canvas.getContext('2d')
  let particles = []

  function initCanvas() {
      canvas.width = window.innerWidth
      canvas.height = window.innerHeight
      particles = []
      for(let i = 0; i < 10; i++) {
          particles.push({
              x: Math.random() * canvas.width,
              y: Math.random() * canvas.height,
              vx: (Math.random() - 0.5) * 0.5,
              vy: (Math.random() - 0.5) * 0.5,
              size: Math.random() * 2 + 1
          })
      }
  }

  function drawParticles() {
      ctx.clearRect(0, 0, canvas.width, canvas.height)
      ctx.fillStyle = 'rgba(0, 123, 255, 0.4)'
      particles.forEach(p => {
          ctx.beginPath(); ctx.arc(p.x, p.y, p.size, 0, Math.PI*2); ctx.fill()
          p.x += p.vx; p.y += p.vy
          if(p.x < 0 || p.x > canvas.width) p.vx *= -1
          if(p.y < 0 || p.y > canvas.height) p.vy *= -1
      })
      animationFrameId = requestAnimationFrame(drawParticles)
  }

  const handleResize = () => initCanvas()
  window.addEventListener('resize', handleResize)
  
  initCanvas() 
  drawParticles()

  // 當元件被卸載時清理監聽器與動畫迴圈，防止記憶體洩漏
  onUnmounted(() => {
    window.removeEventListener('resize', handleResize)
    cancelAnimationFrame(animationFrameId)
  })
})
</script>

<style scoped>
.circuit-bg {
    position: fixed; inset: 0; width: 100vw; height: 100vh;
    background: radial-gradient(circle at center, #0a142e 0%, #02040a 100%);
    z-index: 0; 
    pointer-events: none;
    contain: strict paint layout size; 
    overflow: hidden;
    transform: translateZ(0); 
}

.circuit-grid {
    position: absolute; inset: 0; width: 100%; height: 100%;
    background-image:
        linear-gradient(rgba(0, 123, 255, 0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 123, 255, 0.05) 1px, transparent 1px);
    background-size: 60px 60px; 
    opacity: 0.5; 
}

.pcb-traces {
    position: absolute; inset: 0; width: 100%; height: 100%; 
    opacity: 0.4; 
    transform: translateZ(0); 
}

.base-tracks path { 
    stroke: rgba(255, 255, 255, 0.1); 
    stroke-width: 1.5; 
    fill: none; 
}

.current-flows path {
    fill: none;     
    stroke-linecap: round; 
    animation-name: neonPulse;
    animation-timing-function: cubic-bezier(0.4, 0, 0.2, 1); 
    animation-iteration-count: infinite;
    animation-direction: alternate;
}

@keyframes neonPulse {
    0% { opacity: 0.02; filter: blur(2px); }
    100% { opacity: 0.95; filter: drop-shadow(0 0 8px currentColor); }
}

.flow-1 { stroke-width: 3.5px; animation-duration: 2.1s; animation-delay: 0s; }
.flow-2 { stroke-width: 2px;   animation-duration: 3.4s; animation-delay: -1.2s; }
.flow-3 { stroke-width: 4.5px; animation-duration: 2.7s; animation-delay: -0.7s; }
.flow-4 { stroke-width: 1.5px; animation-duration: 4.1s; animation-delay: -2.3s; }
.flow-5 { stroke-width: 3px;   animation-duration: 1.8s; animation-delay: -0.4s; }
.flow-6 { stroke-width: 2.5px; animation-duration: 3.8s; animation-delay: -1.9s; }

#particle-canvas {
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    z-index: 1; pointer-events: none; 
    opacity: 0.7; 
    transform: translateZ(0);
}

@media (max-width: 767px) {
    .pcb-traces { display: none !important; }
    .circuit-grid { opacity: 0.2; }
}
</style>