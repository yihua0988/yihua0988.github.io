/* 安全的閹割版 protect.js (不會影響 SEO) */
(function() {
    // 禁止右鍵選單 (防一般使用者)
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
    }, false);

    // 禁止 F12, Ctrl+U, Ctrl+S
    document.addEventListener('keydown', function(e) {
        if (e.keyCode == 123 || // F12
           (e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 74)) || // Ctrl+Shift+I/J
           (e.ctrlKey && (e.keyCode == 85 || e.keyCode == 83))) { // Ctrl+U/S
            e.preventDefault();
            return false;
        }
    }, false);
})();