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