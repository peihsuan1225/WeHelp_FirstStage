// popup視窗處理:
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

// ---------------------------------------------------------------------------------------------------
// 引用外部資料並放進box格式內，加載更多按鈕動作處理:
// 發送 HTTP GET 請求獲取 CSV 檔案
var request = new XMLHttpRequest();
// open 方法用於設定請求的方法、URL 和是否異步進行
//"GET"：請求的方法。"task3_use.csv"：請求的 URL，指向一個 CSV 文件。true：表示請求應當是非同步的
request.open("GET","task3_use.csv",true);
// onreadystatechange 事件處理器，在 request 對象的狀態變化時被觸發。當狀態變化的處理函式被呼叫時
// readyState === 4：表示請求已完成，並且響應已經就緒。status === 200：HTTP 狀態碼 200 表示請求成功。
request.onreadystatechange = function(){
    if(request.readyState === 4 && request.status ===200){
        var csvData = request.responseText;
        var lines = csvData.split("\n")
        // 設定預設值:開始顯示>第1筆，次數>1
        var startNum = 1;
        var count = 1;
        function loadMore(){
            // 計算剩下的資料數
            var remaindata = lines.length - startNum + 1;
            // 檢查還有沒有剩下的資料
            if (remaindata <= 0){
                console.log("沒有更多資料")
                return;
            }
            // 計算要load的資料筆數，如果小於10就取原數，大於10就取10
            var dataToLoad = Math.min(remaindata,10);
             // 在第1次的時候 顯示13筆
            if(count == 1){
                dataToLoad = 13;
            }
            
            // 將 CSV 檔案的每一行拆解為標題和圖片連結
            for (var i = startNum-1; i < startNum + dataToLoad-1; i++){
                var parts = lines[i].split(",");
                var title = parts[0];
                var imgUrl = parts[1];

                // 定義元素跟創建元素(按照原本html的結構去做)
                var smallBoxesElement = document.querySelector(".smallBoxes");
                var smallBoxElement = document.createElement("div");
                smallBoxElement.className = "smallBox";

                var bigBoxesElement = document.querySelector(".bigBoxes");
                var bigBoxElement = document.createElement("div");
                bigBoxElement.className = "bigBox";
                var starElement = document.createElement("div");
                starElement.className = "star";
                var starImg = document.createElement("img");
                starImg.src = "star.png";

                var titleElement = document.createElement("div");
                titleElement.textContent = title; // 指定內容(來自csv檔案)
                titleElement.title = title;
                var imgElement = document.createElement("img");
                imgElement.src = imgUrl; // 指定連結(來自csv檔案)

                // 前三組用smallbox的形式，後面的用bigbox的形式
                if(i<3){
                    imgElement.className = "smallBoxPic";
                    titleElement.className = "promotion";
                    smallBoxesElement.appendChild(smallBoxElement);
                    smallBoxElement.appendChild(imgElement);
                    smallBoxElement.appendChild(titleElement);
                }
                else{
                    titleElement.className = "title";
                    bigBoxesElement.appendChild(bigBoxElement);
                    bigBoxElement.appendChild(imgElement);
                    bigBoxElement.appendChild(titleElement);
                    bigBoxElement.appendChild(starElement);
                    starElement.appendChild(starImg);

                };
            }
           
            // endNum +=10
            count +=1 
            startNum = startNum+dataToLoad;
        }
        // 初始網頁加載
        loadMore();
        // 點擊loadmore按鈕會呼叫loadMore function
        var loadMoreBtn = document.querySelector(".loadmoreButton");
        loadMoreBtn.addEventListener("click",loadMore);
    }
};
// 發送請求
request.send();