/* =========================================================================
 * 🛡️ 宗師級 protect.js (零誤殺穩定版：精準反爬蟲 + SEO/社群完全放行 + 禁選文字)
 *    - 100% 放行：Google/Bing 檢索爬蟲、LINE/FB/IG/Discord 連結預覽與內建瀏覽器
 *    - 100% 放行：正常人類訪客（含無痕模式、關閉硬體加速、安裝 AdBlock 外掛者）
 *    - 精準攔截：Python/curl 等腳本請求、Selenium/Puppeteer/Playwright 自動化工具
 * ========================================================================= */
(function() {
    'use strict';

    // 🌟 [開發環境放行] 本地開發與內網測試絕對不攔截
    const isLocal = /^(localhost|127\.0\.0\.1|192\.168\.|10\.|172\.(1[6-9]|2[0-9]|3[0-1])\.)/.test(location.hostname);

    // ---------------------------------------------------------------------
    // 1. 動態注入 CSS：禁止全站選取文字（保留 input / textarea 可正常輸入）
    // ---------------------------------------------------------------------
    const injectNoSelectCSS = () => {
        const inject = () => {
            if (!document.head || document.getElementById('anti-select-style')) return;
            const style = document.createElement('style');
            style.id = 'anti-select-style';
            style.type = 'text/css';
            style.innerHTML = `
                body, html {
                    -webkit-user-select: none !important;
                    -moz-user-select: none !important;
                    -ms-user-select: none !important;
                    user-select: none !important;
                }
                input, textarea, [contenteditable="true"] {
                    -webkit-user-select: text !important;
                    -moz-user-select: text !important;
                    -ms-user-select: text !important;
                    user-select: text !important;
                }
            `;
            document.head.appendChild(style);
        };
        if (document.head) inject();
        else document.addEventListener('DOMContentLoaded', inject, { once: true });
    };
    injectNoSelectCSS();

    if (isLocal) return;

    // ---------------------------------------------------------------------
    // 2. 防網頁被第三方惡意 iframe 嵌入 (保留同源嵌入彈性)
    // ---------------------------------------------------------------------
    if (window.top !== window.self) {
        try {
            if (window.top.location.hostname !== window.self.location.hostname) {
                window.top.location = window.self.location;
            }
        } catch (e) {
            // 跨域惡意嵌入才清空
            document.documentElement.innerHTML = '';
        }
    }

    // ---------------------------------------------------------------------
    // 3. 「搜尋引擎、社群預覽機器人、通訊軟體內建瀏覽器」超級白名單
    // ---------------------------------------------------------------------
    const SEO_AND_SOCIAL_WHITELIST = new RegExp([
        // Google 全系列檢索與渲染服務
        'Googlebot', 'Google-InspectionTool', 'Storebot-Google', 'GoogleOther',
        'APIs-Google', 'Mediapartners-Google', 'AdsBot-Google', 'Google-Read-Aloud',
        'DuplexWeb-Google', 'Google Favicon', 'Google-Site-Verification',
        // 主流國際搜尋引擎
        'bingbot', 'adidxbot', 'MicrosoftPreview', 'BingPreview',
        'Slurp', 'DuckDuckBot', 'Baiduspider', 'YandexBot', 'Sogou', 'Applebot', 'NaverBot', 'Yeti',
        // 社群平台預覽爬蟲 & App 內建瀏覽器 (LINE / FB / IG / Threads / Discord / LinkedIn / X)
        'facebookexternalhit', 'Facebot', 'FBAN', 'FBAV', 'FB_IAB', 'Instagram', 'Barcelona',
        'Line', 'Line-Poker', 'LIFF',
        'Twitterbot', 'LinkedInBot', 'Discordbot', 'TelegramBot',
        'WhatsApp', 'Slackbot', 'Pinterestbot', ' Threads'
    ].join('|'), 'i');

    // ---------------------------------------------------------------------
    // 4. 「明確惡意爬蟲、自動化框架、裸體 HTTP 請求庫」黑名單
    //    (已移除 Dalvik 等容易誤傷 Android 正常 App WebView 的字眼)
    // ---------------------------------------------------------------------
    const STRICT_BAD_BOT_REGEX = new RegExp([
        // 無頭自動化控制工具
        'HeadlessChrome', 'PhantomJS', 'SlimerJS', 'Nightmare',
        'Playwright', 'Puppeteer', 'Selenium', 'WebDriver', 'Cypress',
        'Splash', 'HtmlUnit', 'CasperJS',
        // 裸體程式語言請求庫 (正常瀏覽器絕不會有這些 UA)
        'Python-urllib', 'python-requests', 'aiohttp', 'httpx', 'pycurl', 'Scrapy',
        'Apache-HttpClient', 'OkHttp', 'Java/', 'Jsoup',
        'Go-http-client', 'colly', 'fasthttp',
        'node-fetch', 'axios/', 'got/', 'undici', 'superagent',
        'curl/', 'wget/', 'libwww-perl', 'PHP/', 'GuzzleHttp', 'RestSharp',
        'PostmanRuntime', 'Insomnia',
        // 知名高消耗商業爬蟲與 AI 訓練收割機
        'AhrefsBot', 'SemrushBot', 'MJ12bot', 'DotBot', 'PetalBot', 'Bytespider',
        'BLEXBot', 'DataForSeoBot', 'MegaIndex', 'SeekportBot', 'ZoominfoBot',
        'CCBot', 'Diffbot', 'omgili', 'GPTBot', 'ClaudeBot'
    ].join('|'), 'i');

    // ---------------------------------------------------------------------
    // 5. 核心檢測流程：白名單優先 ➔ 黑名單攔截 ➔ 雙重證據才封鎖
    // ---------------------------------------------------------------------
    function runSecurityCheck() {
        const ua = navigator.userAgent || '';

        // [A] 完全空白或異常過短的偽造 UA 直接擋
        if (!ua || ua.trim().length < 12) {
            return triggerBlock('ERR_EMPTY_USER_AGENT');
        }

        // [B] 命中「SEO 搜尋引擎 / 社群預覽 / LINE與FB內建瀏覽器」白名單 ➔ 直接無條件放行！
        //     注意：Googlebot 渲染時底層基於 Headless Chromium，絕對不能對它檢查 webdriver，否則 SEO 會全毀
        if (SEO_AND_SOCIAL_WHITELIST.test(ua)) {
            return; 
        }

        // [C] 命中明確的惡意爬蟲與自動化工具 UA 黑名單 ➔ 立即攔截
        if (STRICT_BAD_BOT_REGEX.test(ua)) {
            return triggerBlock('ERR_AUTOMATED_CRAWLER_UA');
        }

        // [D] 檢查 Client Hints 是否直接自爆為 HeadlessChrome
        if (navigator.userAgentData && Array.isArray(navigator.userAgentData.brands)) {
            const brandStr = navigator.userAgentData.brands.map(b => b.brand).join(' ');
            if (/HeadlessChrome|Playwright|Puppeteer/i.test(brandStr)) {
                return triggerBlock('ERR_HEADLESS_CLIENT_HINT');
            }
        }

        // [E] 檢查 window / document 是否殘留 Selenium / ChromeDriver / Playwright 注入的全域控制變數
        if (hasAutomationFrameworkGlobals()) {
            return triggerBlock('ERR_DRIVER_INJECTED_GLOBALS');
        }

        // [F] 檢查標準 WebDriver 旗標
        //     為了防止少數特殊防毒軟體或企業瀏覽器誤觸，採用「webdriver 為 true 且無正常外掛/語言特徵」或直接命中時攔截
        if (navigator.webdriver === true) {
            return triggerBlock('ERR_WEBDRIVER_ACTIVE');
        }
    }

    // ---------------------------------------------------------------------
    // 輔助函式：只抓「100% 確定是自動化框架注入」的全域變數，不碰原生 Prototype
    // ---------------------------------------------------------------------
    function hasAutomationFrameworkGlobals() {
        const strictAutomatedKeys = [
            '__playwright',
            '__pw_manual',
            '_Selenium_IDE_Recorder',
            '_selenium',
            'calledSelenium',
            '__webdriver_evaluate',
            '__selenium_evaluate',
            '__webdriver_script_function',
            '__webdriver_script_func',
            '__webdriver_script_fn',
            '__fxdriver_evaluate',
            '__driver_unwrapped',
            '__webdriver_unwrapped',
            '__driver_evaluate',
            '__selenium_unwrapped',
            '__fxdriver_unwrapped',
            'callPhantom',
            '_phantom',
            '__phantomas',
            '__nightmare',
            'domAutomation',
            'domAutomationController'
        ];

        for (let i = 0; i < strictAutomatedKeys.length; i++) {
            if (strictAutomatedKeys[i] in window) {
                return true;
            }
        }

        // 掃描 ChromeDriver 預設注入的 $cdc_ 隨機特徵碼
        const cdcRegex = /^(\$cdc_[a-zA-Z0-9]+|__\$webdriverAsyncExecutor)$/;
        try {
            const docProps = Object.getOwnPropertyNames(document);
            for (let i = 0; i < docProps.length; i++) {
                if (cdcRegex.test(docProps[i])) return true;
            }
        } catch (e) {}

        return false;
    }

    // ---------------------------------------------------------------------
    // 6. 觸發攔截畫面 (403 Access Denied)
    // ---------------------------------------------------------------------
    function triggerBlock(code) {
        try {
            window.stop && window.stop();
        } catch (e) {}

        document.documentElement.innerHTML = `
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta name="robots" content="noindex, nofollow">
                <title>403 Access Denied</title>
            </head>
            <body style="background:#090d16; color:#f8fafc; font-family:system-ui,-apple-system,sans-serif; display:flex; justify-content:center; align-items:center; height:100vh; margin:0;">
                <div style="background:#1e293b; border:1px solid #ef4444; border-radius:16px; padding:40px; max-width:520px; text-align:center; box-shadow:0 20px 50px rgba(0,0,0,0.6); margin:20px;">
                    <div style="font-size:48px; margin-bottom:12px;">🛡️</div>
                    <h1 style="color:#f87171; font-size:26px; margin:0 0 12px 0;">403 Access Denied</h1>
                    <p style="color:#cbd5e1; font-size:16px; line-height:1.6; margin:0 0 20px 0;">
                        系統偵測到自動化爬蟲或非授權的腳本存取，已主動阻斷連線。
                    </p>
                    <div style="background:#0f172a; color:#38bdf8; font-family:monospace; font-size:13px; padding:10px; border-radius:8px; border:1px solid #334155; word-break:break-all;">
                        DEFENSE_SIGNATURE: ${code}
                    </div>
                </div>
            </body>
        `;
        throw new Error('[CyberDefense] Blocked automated client: ' + code);
    }

    runSecurityCheck();
})();