// task1 給一些朋友的訊息跟你現在所在捷運站，判斷出哪位朋友跟你離最近 

function findAndPrint(messages, currentStation){
    // 建立locDict，紀錄人名對應所在站點序號
    let locDict = {};
    // 用for迴圈把訊息裡的每個鍵值跑一遍
    for(const [name,message] of Object.entries(messages)){
        // 把greenLineDict裡的站名一個一個取出
        for(const station in greenLineDict){
            // 當值符合greenline的站時
            if(message.includes(station)){
                // 將名字放入locDict的key
                // 將對應的greenLineDict的值放入locDict的value
                locDict[name] = greenLineDict[station];
            }
        }
    }
    // console.log(locDict);
    // 把函式的參數"站名"換成"站點序號"
    let rightnowLoc = greenLineDict[currentStation];
    // console.log(rightnowLoc);
    // 建立距離物件，人名:距離
    let distanceDict = {};
    // 用for迴圈對每個有人的站做動作
    for(const [name,someoneLoc] of Object.entries(locDict)){
        // 對小碧潭的特殊算法
        // 如果所在站或有人的站是小碧潭(站點序號17.5)
        if(rightnowLoc === 17.5 || someoneLoc === 17.5){
            if(rightnowLoc === someoneLoc){
                singleDistance = 0;
            }
            // 如果(所在站在Qizhang或之前)或是(有人的站在Qizhang或之前)，套用特殊公式
            else if(rightnowLoc <= 17 || someoneLoc <= 17){
                singleDistance = Math.abs(rightnowLoc - someoneLoc)+0.5;
            }
            // 如果(所在站在Xindian City Hall或之後)或是(有人的站在Xindian City Hall或之後)，套用特殊公式
            else if(rightnowLoc >= 18 || someoneLoc >= 18){
                singleDistance = Math.abs(rightnowLoc - someoneLoc)+1.5;
            }
        }
        else{
            singleDistance = Math.abs(rightnowLoc - someoneLoc);
        };
        // 把計算出來的距離跟對應的人名放進distanceDict裡
        distanceDict[name] = singleDistance;
    }
    // console.log(distanceDict);
    // 找到距離最小的距離，印出對應的人
    let cloestDist = Math.min(...Object.values(distanceDict));
    for(let[name,singleDistance] of Object.entries(distanceDict)){
        if(cloestDist == singleDistance){
            let cloestPerson = name;
            console.log(cloestPerson);
        }
    };
}


// 建立綠線，由題目給的站名對應序號
const greenLineDict={
    "Songshan":1,"Nanjing Sanmin":2,"Taipei Arena":3,"Nanjing Fuxing":4,"Songjiang NanJing":5,"Zhongshan":6,
    "Beimen":7,"Ximen":8,"Xiaonanmen":9,"Chiang Kai-Shek Memorial Hall":10,"Guting":11,
    "Taipower Building":12,"Gongguan":13,"Wanlong":14,"Jingmei":15,"Dapinling":16,
    "Qizhang":17, "Xiaobitan":17.5,"Xindian City Hall":18,"Xindian":19
};


// 題目給的資訊(可能之後會有其他人的資訊以同樣的格式加入)
const messages={
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Leslie":"I'm at home near Xiaobitan station.",
"Vivian":"I'm at Xindian station waiting for you."
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian