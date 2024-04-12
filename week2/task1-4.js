console.log("------------------task1-----------------")
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

console.log("------------------task2-----------------")
// task2 預約顧問，給標準跟時間判斷哪個顧問可以被預約

// 建立一個rateDict物件，紀錄人名對應分數
let rateDict = {};
// 建立一個price物件，紀錄人名對應價格
let priceDict = {};
// 建立一個orderedTimeDict，紀錄人名對應已預定時間
let orderedTimeDict = {};

function book(consultants, hour, duration, criteria){
    // 把已建立的物件引用進來函式
    let thisbookRateDict = rateDict ;
    let thisbookPriceDict = priceDict ;
    // 建立booked代表是否已經完成預定判斷，預設值為"尚未完成"(已完成就不會再重複迴圈)
    let booked = false;
    while(!booked){
    // 第一個流程，透過criteria找到最符合的人
        // 建立thePerson來裝第一個流程挑選出來的人
        let thePerson = null;
        // 選擇標準為價錢
        if(criteria == "price"){
            let lowestPrice = Math.min(...Object.values(thisbookPriceDict));  // 找到最小的value(價格)
            for([key,value] of Object.entries(thisbookPriceDict)){
                if(value === lowestPrice){        // 找對應最低價格的key(人名)
                    thePerson = key;
                }
            }
        }
        // 選擇標準為評分
        else if(criteria == "rate"){
            let hightestRate = Math.max(...Object.values(thisbookRateDict)); // 找到最大的value(評分)
            for([key,value] of Object.entries(thisbookRateDict)){
                if(value === hightestRate){       // 找對應最高評分的key(人名)
                    thePerson = key;         
                }
            }
        }
        // 第二個流程，把本次的預定時間跟第一個流程選出來的人的已預定時間做比對
        // 建立本次預定的時間list
        let booktimeList = [];
        for (let i = hour; i < hour + duration; i++) {
            booktimeList.push(i);
        }
        // 把當前選出來的人的已預定時間從orderedTimeDict中叫出來，用personOrdered裝起來
        let personOrdered = orderedTimeDict[thePerson];
        // 建立overlap代表時間是否有重疊，預設值為"沒有重疊"
        let overlap = false;
        // 用for迴圈將這次要預定的時間跟選定顧問的已預定時間做比較
        for(let hr of booktimeList){
            // 如果預約時間有重疊，到對應的選擇標準把當前的顧問除名
            // 除名後判斷還有沒有其他人，沒有的話就印出No Service，把booked狀態變成true(結束while迴圈)
            if(personOrdered.includes(hr)){
                overlap = true;
                if(criteria == "price"){
                    delete thisbookPriceDict[thePerson];
                    if(Object.keys(thisbookPriceDict).length === 0){
                        console.log("No Service");
                        booked = true;
                    }
                }
                else if(criteria == "rate"){
                    delete thisbookRateDict[thePerson];
                    if(Object.keys(thisbookRateDict).length === 0){
                        console.log("No Service");
                        booked = true;
                    }
                }    
            }
        }
        // 如果預約時間沒重疊，把本次預約時間加到當前選擇人的已預定時間list中，並印出名字，把booked狀態變成true(結束while迴圈)
        if(!overlap){
            if (orderedTimeDict[thePerson]) {
                orderedTimeDict[thePerson] = orderedTimeDict[thePerson].concat(booktimeList);
            } 
            console.log(thePerson);
            booked = true;
        };


    }
    
}
  

// 題目給的資訊(可能之後會有其他人的資訊以同樣的格式加入)
const consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
];

// 在consultants裡面抓取 name:rate 與 name:price 與name:[]，分別放進對應的物件中
for(let singleInfo of consultants){
    let key = singleInfo.name;
    let rateValue = singleInfo.rate;
    let priceValue = singleInfo.price;
    rateDict[key] = rateValue;
    priceDict[key] = priceValue;
    orderedTimeDict[key] = []; 
};
// console.log(rateDict)
// console.log(priceDict)
// console.log(orderedTimeDict)

book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John

console.log("------------------task3-----------------")
// task3 判斷獨一無二的中間名

function func(...data){
    // 建立一個所有 中間名 的 array
    let middleNamesList = [];
    // 建立一個所有 中間名:名字 的物件
    let nameMiddlenameDict = {};

    // 用forEach 抓每一個名字跟中間名，放入 array 跟物件
    data.forEach(name =>{
        if (name.length <=3){       // 兩個字&三個字的名字
            let middleName = name[1];
            middleNamesList.push(middleName);
            let key = name[1];
            let value = name;
            nameMiddlenameDict[key] = value;
        } 
        else if(name.length <=5){    // 四個字&五個字的名字
            let middleName = name[2];
            middleNamesList.push(middleName);
            let key = name[2];
            let value = name;
            nameMiddlenameDict[key] = value;
        }
    });
    // console.log(middleNamesList);   
    // console.log(nameMiddlenameDict);

    //建立一個存放 unique 中間名的 array
    let uniqueMiddleNames = [];   
    // 用 forEach 把中間名拿出來計算，如果只有一次就放到 uniqueMiddleNames 的 array 裡   
    middleNamesList.forEach(middleName =>{
        if(middleNamesList.filter(mid => mid === middleName).length === 1){
            uniqueMiddleNames.push(middleName);
        }
    });

    
    if(uniqueMiddleNames.length === 0){    //如果 uniqueMiddleNames 這個 array 沒有值
        console.log("沒有");
    }
    else{
        uniqueMiddleNames.forEach(middleName =>{
            console.log(nameMiddlenameDict[middleName]);
        });
    }
 }
 
 
func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安

console.log("------------------task4-----------------")
// task4 數列規律

// There is a number sequence: 0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25, …
// 規律為 +4 +4 -1

function getNumber(index){
    // count用來計算次數(位置)
    let count = 0;
    // now用來儲存現在的值
    let now = 0;
    while(count < index){
        // 在3n循環時，對當前數字減一
        if(count % 3 == 2){
            now -= 1;
        }
        // 在其他位置時，對當前數字加四
        else{
            now +=4;
        }
        // 每過一個迴圈，把數列位置也推進一位
        count +=1;
    }
    console.log(now);
}
    
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70