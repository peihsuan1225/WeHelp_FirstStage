print("------------------task1-----------------")
# task1 給一些朋友的訊息跟你現在所在捷運站，判斷出哪位朋友跟你離最近 

def find_and_print(messages, current_station):
    # 建立loc_dict字典，紀錄人名對應所在站點序號
    loc_dict = {}
    # 用for迴圈把訊息字典裡的每個鍵值跑一遍
    for name, message in messages.items():
        # 把greenline字典的站名一個一個取出
        for station in greenLine_dict.keys():
            # 當值符合greenline裡的站時
            if station in message:
                # 將名字放入loc_dict的key
                # 將對應的greenLine_dict的值放入loc_dict的value
                loc_dict[name] = greenLine_dict[station]

    # 把函式的參數"站名"換成"站點序號"
    rightnow_loc = greenLine_dict[current_station]
    # 建立距離字典，人名:距離
    distances_dict={}
    # 用for迴圈對每個有人的站做動作
    for name,someone_loc in loc_dict.items():
        # 對小碧潭的特殊算法
        # 如果所在站或有人的站是小碧潭(站點序號17.5)
        if rightnow_loc == 17.5 or someone_loc == 17.5:
            # 如果給的站跟有人站都是小碧潭那距離為0
            if rightnow_loc == someone_loc: 
                single_distance = 0
            # 如果(所在站在Qizhang或之前)或是(有人的站在Qizhang或之前)，套用特殊公式
            elif rightnow_loc <= 17 or someone_loc <= 17 :
                single_distance = abs(rightnow_loc - someone_loc) + 0.5
            # 如果(所在站在Xindian City Hall或之後)或是(有人的站在Xindian City Hall或之後)，套用特殊公式
            elif rightnow_loc >= 18 or someone_loc >= 18 :  
                single_distance = abs(rightnow_loc - someone_loc) + 1.5
        else:
            single_distance = abs(rightnow_loc-someone_loc)
        # 把計算出來的距離跟對應的人名放進distances_dict裡
        distances_dict[name] = single_distance 
    # print(distances_dict)
    # 找到距離字典裡最小的距離，印出對應的人
    closest_dist = min(distances_dict.values())
    for name,single_distance in distances_dict.items():
        if closest_dist == single_distance:
            closest_person=name
            print(closest_person)


# 建立綠線字典，由題目給的站名對應序號
greenLine_dict={
    "Songshan":1,"Nanjing Sanmin":2,"Taipei Arena":3,"Nanjing Fuxing":4,"Songjiang NanJing":5,"Zhongshan":6,
    "Beimen":7,"Ximen":8,"Xiaonanmen":9,"Chiang Kai-Shek Memorial Hall":10,"Guting":11,
    "Taipower Building":12,"Gongguan":13,"Wanlong":14,"Jingmei":15,"Dapinling":16,
    "Qizhang":17, "Xiaobitan":17.5,"Xindian City Hall":18,"Xindian":19
}

# 題目給的資訊(可能之後會有其他人的資訊以同樣的格式加入)
messages={
    "Leslie":"I'm at home near Xiaobitan station.",  
    "Bob":"I'm at Ximen MRT station.",  
    "Mary":"I have a drink near Jingmei MRT station.",  
    "Copper":"I just saw a concert at Taipei Arena.", 
    "Vivian":"I'm at Xindian station waiting for you."  
}

find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

print("------------------task2-----------------")
# task2 預約顧問，給標準跟時間判斷哪個顧問可以被預約

# 建立一個rate的字典，紀錄人名對應分數
rate_dict = {} 
# 建立一個price的字典，紀錄人名對應價格
price_dict = {} 
# 建立一個已被預訂時間的字典，紀錄人名對應已預定時間
ordered_time_dict = {} 

import copy

def book(consultants, hour, duration, criteria):
    # 把已建立的字典引用進來函式
    thisbook_rate_dict = rate_dict
    thisbook_price_dict = price_dict
    # 建立booked代表是否已經完成預定判斷，預設值為"尚未完成"(已完成就不會再重複迴圈)
    booked = False
    while not booked:
    # 第一個流程，透過criteria找到最符合的人
        # 建立the_person來裝第一個流程挑選出來的人
        the_person = None
        # 選擇標準為價錢
        if criteria == "price":
            lowest_price = min((thisbook_price_dict.values()))  # 找到最小的value(價格)
            for key, value in thisbook_price_dict.items():
                if value == lowest_price:  # 找對應最低價格的key(人名)
                    the_person = key
        # 選擇標準為評分
        elif criteria == "rate":
            hightest_rate = max(thisbook_rate_dict.values()) # 找到最大的value(評分)
            for key,value in thisbook_rate_dict.items():
                if value == hightest_rate:   # 找對應最高評分的key(人名)
                    the_person = key

        # 第二個流程，把本次的預定時間跟第一個流程選出來的人的已預定時間做比對
        # 建立本次預定的時間list
        booktime_list = []     
        # 用range把這次要預定的時間點一個一個列出來，放進booktime_list裡
        timeline = range(hour,(hour+duration)) 
        for singlehour in timeline:
            booktime_list.append(singlehour)
        # print(booktime_list)
        # 把當前選出來的人的已預定時間從dict中叫出來，用person_ordered裝起來
        person_ordered = ordered_time_dict[the_person]
        # print(person_ordered)
        # 建立overlap代表時間是否有重疊，預設值為"沒有重疊"
        overlap = False
        # 用for迴圈將這次要預定的時間跟選定顧問的已預定時間做比較
        for hr in booktime_list:
            # 如果預約時間有重疊，到對應的選擇標準dict把當前的顧問除名
            # 除名後判斷dict裡還有沒有其他人，沒有的話就印出No Service，把booked狀態變成true(結束while迴圈)
            if hr in person_ordered:
                overlap = True
                if criteria == "price":
                    del thisbook_price_dict[the_person]
                    if not thisbook_price_dict:
                        print("No Service")
                        booked =True
                elif criteria == "rate":
                    del thisbook_rate_dict[the_person]
                    if not thisbook_rate_dict:
                        print("No Service")
                        booked =True
        # 如果預約時間沒重疊，把本次預約時間加到當前選擇人的已預定時間list中，並印出名字，把booked狀態變成true(結束while迴圈)
        if not overlap:
            ordered_time_dict[the_person].extend(booktime_list)
            print(the_person)
            booked = True
    # print(ordered_time_dict)

# 題目給的資訊(可能之後會有其他人的資訊以同樣的格式加入)
consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]

 # 在consultants裡面抓取 name:rate 與 name:price 與name:[]，分別放進對應的字典中
for single_info in consultants:
    key = single_info["name"]
    value_rate = single_info["rate"]
    value_price = single_info["price"]
    rate_dict[key] = value_rate    
    price_dict[key] = value_price
    ordered_time_dict[key] = []

    # print(rate_dict)
    # print(price_dict)
    # print(ordered_time_dict)

book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John

print("------------------task3-----------------")
# task3 判斷獨一無二的中間名

def func(*data):
    # 建立一個所有 中間名 的 list
    middle_names_list = []
    # 建立一個所有 中間名:名字 的dictionary
    name_middlename_dict = {}

    # 用for迴圈抓每一個名字跟中間名，放入list跟dictionary裡
    for name in data:
        if len(name) <=3:   # 兩個字&三個字的名字
            middle_name = name[1]
            middle_names_list.append(middle_name)
            key = name[1]
            value = name
            name_middlename_dict[key] = value
        elif len(name) <=5:  # 四個字&五個字的名字
            middle_name = name[2]
            middle_names_list.append(middle_name)
            key = name[2]
            value = name
            name_middlename_dict[key] = value

    # print(middle_names_list)   
    # print(name_middlename_dict)

    unique_middle_names = []    #建立一個存放unique中間名的list
    # 用for迴圈把中間名拿出來計算，如果只有一次就放到unique_middle_names的list裡
    for middle_name in middle_names_list:
        if middle_names_list.count(middle_name) == 1:
            unique_middle_names.append(middle_name)
    # print(unique_middle_names)

    if not unique_middle_names:      #如果unique_middle_names這個list沒有值
        print("沒有")
    else :
        for middle_name in unique_middle_names:     #印出unique中間名對應的全名(dictionary的鍵)
            print(name_middlename_dict[middle_name])


func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安

print("------------------task4-----------------")
# task4 數列規律

# There is a number sequence: 0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25, …
# 規律為 +4 +4 -1

def get_number(index):
    # count用來計算次數(位置)
    count = 0
    # now用來儲存現在的值
    now = 0
    while count < index:
        if count % 3 == 2: # 在3n循環時，對當前數字減一
            now -= 1
        else:
            now += 4 # 在其他位置時，對當前數字加四
        count += 1 # 每過一個迴圈，把數列位置也推進一位
    print(now)

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70