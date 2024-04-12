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