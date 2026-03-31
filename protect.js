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

    // --- 2. 行為攔截 ---
    function redirectToGoogle() {
        if (window.location.hostname !== "www.google.com") {
            window.location.href = "https://www.google.com";
        }
    }

    // 【已移除】：動態注入 user-select: none 的 CSS (讓滑鼠可以反白文字)
    // 【已移除】：禁止 selectstart, copy, cut, paste 的事件攔截 (讓右鍵複製或快捷鍵複製生效)

    // 禁止右鍵選單 (這項保留，防止直接右鍵另存圖片或檢視原始碼。使用者仍可用 Ctrl+C 複製)
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
        e.stopPropagation(); 
    }, true);

    // 禁止鍵盤快捷鍵 (保留 F12, Ctrl+U, Ctrl+S，但【開放 Ctrl+C / Ctrl+X】)
    document.addEventListener('keydown', function(e) {
        // 阻擋 F12
        if (e.keyCode == 123) {
            e.preventDefault();
            redirectToGoogle();
            return false;
        }
        
        // Ctrl 組合鍵檢查
        if (e.ctrlKey) {
            // Shift 組合鍵 (阻擋 I, J, 開發者工具)
            if (e.shiftKey) {
                // 這裡拿掉了 67(C)，只擋 73(I), 74(J)
                if (e.keyCode == 73 || e.keyCode == 74) { 
                    e.preventDefault();
                    redirectToGoogle();
                    return false;
                }
            }
            // 單純 Ctrl 組合鍵 (阻擋 U=原始碼, S=存檔)
            // 這裡拿掉了 67(C) 和 88(X)，讓複製剪下可以正常運作
            if (e.keyCode == 85 || e.keyCode == 83) {  
                e.preventDefault();
                redirectToGoogle();
                return false;
            }
        }
    }, true);

    // --- 3. 進階偵測：Debugger 時間差攻擊 (保留) ---
    setInterval(function() {
        var start = new Date().getTime();
        debugger; 
        var end = new Date().getTime();
        if (end - start > 100) { 
            redirectToGoogle();
        }
    }, 2000); 

})();