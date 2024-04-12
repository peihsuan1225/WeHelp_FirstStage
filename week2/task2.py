# task2 預約顧問，給標準跟時間判斷哪個顧問可以被預約

# 建立一個rate的字典，紀錄人名對應分數
rate_dict = {} 
# 建立一個price的字典，紀錄人名對應價格
price_dict = {} 
# 建立一個已被預訂時間的字典，紀錄人名對應已預定時間
ordered_time_dict = {} 


def book(consultants, hour, duration, criteria):
    # 把已建立的字典引用進來函式(目的:讓外部字典的值不受函式內部的動作改變)
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
            lowest_price = min((thisbook_price_dict.values()))  #找到最小的value(價格)
            for key, value in thisbook_price_dict.items():
                if value == lowest_price:  # 找對應最低價格的key(人名)
                    the_person = key
        # 選擇標準為評分
        elif criteria == "rate":
            hightest_rate = max(thisbook_rate_dict.values()) #找到最大的value(評分)
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
