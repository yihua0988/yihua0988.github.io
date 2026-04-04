/* HTML/protect.js */
(function() {
    // --- 1. SEO 白名單檢查 (讓 Google/Line/FB 爬蟲可以正常讀取) ---
    var userAgent = navigator.userAgent.toLowerCase();
    var allowedBots = [
        'googlebot', 'bingbot', 'baiduspider', 'yandex', 
        'facebookexternalhit', 'line', 'twitterbot', 'slack', 
        'telegrambot', 'discordbot', 'pinterest'
    ];
    
    for (var i = 0; i < allowedBots.length; i++) {
        if (userAgent.indexOf(allowedBots[i]) !== -1) {
            return;
        }
    }

    // --- 2. 暴力清空機制 (無提示瞬間銷毀版) ---
    function blockAccess() {
        // 第一時間直接把整個網頁結構徹底清空，不顯示任何文字或提示
        document.documentElement.innerHTML = "";
        
        // 執行跳轉
        if (window.location.hostname !== "www.google.com") {
            window.location.href = "https://www.google.com";
        }
    }

    // 【已移除】：動態注入 user-select: none 的 CSS (讓滑鼠可以反白文字)
    // 【已移除】：禁止 selectstart, copy, cut, paste 的事件攔截 (讓右鍵/快捷鍵複製生效)

    // --- 3. 禁止鍵盤與右鍵行為 ---
    // 禁止右鍵選單 (保留，防止直接點擊「檢視網頁原始碼」)
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
        e.stopPropagation(); 
    }, true);

    // 禁止鍵盤快捷鍵 (保留 F12, Ctrl+U, Ctrl+S，但【開放 Ctrl+C / Ctrl+X】)
    document.addEventListener('keydown', function(e) {
        // 阻擋 F12
        if (e.keyCode == 123) {
            e.preventDefault();
            blockAccess();
            return false;
        }
        
        // Ctrl 組合鍵檢查
        if (e.ctrlKey) {
            // Shift 組合鍵 (阻擋 I, J, 開發者工具)
            if (e.shiftKey) {
                // 這裡拿掉了 67(C)，只擋 73(I), 74(J)
                if (e.keyCode == 73 || e.keyCode == 74) { 
                    e.preventDefault();
                    blockAccess();
                    return false;
                }
            }
            // 單純 Ctrl 組合鍵 (阻擋 U=原始碼, S=存檔)
            // 這裡拿掉了 67(C) 和 88(X)，讓複製和剪下可以正常運作
            if (e.keyCode == 85 || e.keyCode == 83) {  
                e.preventDefault();
                blockAccess();
                return false;
            }
        }
    }, true);

    // --- 4. 多重維度偵測 (每 0.1 秒掃描一次) ---
    setInterval(function() {
        // [防護 A] 視窗比例異常偵測 (針對預先開好 F12 的人)
        var widthDiff = window.outerWidth - window.innerWidth;
        var heightDiff = window.outerHeight - window.innerHeight;
        
        // 容錯值設為 200 (外框與內部尺寸差大於 200px 視為開啟 F12)
        if ((widthDiff > 200 || heightDiff > 200) && window.innerWidth > 500) {
            blockAccess();
        }

        // [防護 B] Debugger 時間差攻擊
        var start = new Date().getTime();
        debugger; 
        var end = new Date().getTime();
        if (end - start > 50) { // 門檻值 50 毫秒
            blockAccess();
        }
    }, 100); // 100 毫秒 (0.1秒)

    // [防護 C] 只要切換視窗回來，立刻重新檢查
    document.addEventListener("visibilitychange", function() {
        if (!document.hidden) {
            var widthDiff = window.outerWidth - window.innerWidth;
            var heightDiff = window.outerHeight - window.innerHeight;
            if ((widthDiff > 200 || heightDiff > 200) && window.innerWidth > 500) {
                blockAccess();
            }
        }
    });

    // [防護 D] 只要拉動視窗大小，立刻重新檢查
    window.addEventListener('resize', function() {
        var widthDiff = window.outerWidth - window.innerWidth;
        var heightDiff = window.outerHeight - window.innerHeight;
        if ((widthDiff > 200 || heightDiff > 200) && window.innerWidth > 500) {
            blockAccess();
        }
    });

})();