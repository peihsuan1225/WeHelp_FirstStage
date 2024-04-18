// popup視窗處理
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
// 引用外部資料處理
// 發送 HTTP GET 請求獲取 CSV 檔案
var request = new XMLHttpRequest();
request.open("GET","task3_use.csv",true);
request.onreadystatechange = function(){
    if(request.readyState === 4 && request.status ===200){
        var csvData = request.responseText;
        var lines = csvData.split("\n")

        var startNum = 0;
        var endNum = 12;
        var count = 0;
        function loadMore(){
            // 將 CSV 檔案的每一行拆解為標題和圖片連結
            for (var i = startNum;i <= endNum; i++){
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
            if(count == 0){
                startNum = 13;
            }
            else{
                startNum += 10;
            }
            endNum +=10
            count +=1 
        }
        
        loadMore();

        var loadMoreBtn = document.querySelector(".loadmoreButton");
        loadMoreBtn.addEventListener("click",loadMore);
    }
};
request.send();