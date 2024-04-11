// 取得class是menuItems這個標籤物件
var menu=document.querySelector(".menuItems");

// popup視窗的函式，把menuItems的display改成block
function popupMenu(){
    menu.style.display = "block";
}

// 關閉視窗的函式，把menuItems的display改成none
// 函式名稱一開始設定為close，後來發現close是一個html的預設函数，在跑的時候系統會優先判別HTML的close，而不是這邊設定的close函式。
function closeMenu(){
    menu.style.display = "none";
}

// 只要視窗大小被改變，會就呼叫函式
// 函式：判斷視窗大小是否大於600，如果成立把透過js添加在menuItems的display樣式移除(就會回歸css檔案的設定)
// 多寫這個函式是因為發現在小於600的視窗如果執行過popupMenu或closeMenu函式後，會覆蓋掉中視窗跟大視窗原本的css
window.addEventListener('resize', function() {
    var screenWidth = window.innerWidth;
    if (screenWidth > 600) {
        menu.style.display=""; 
    }
});
