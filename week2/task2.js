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
