# task1 給一些朋友的訊息跟現在所在捷運站，判斷出哪位朋友跟你離最近 

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
            # 如果(所在站在Qizhang之前)或是(有人的站在Qizhang之前)，套用特殊公式
            elif rightnow_loc <= 17 or someone_loc <= 17 :
                single_distance = abs(rightnow_loc - someone_loc) + 0.5
            # 如果(所在站在Xindian City Hall之後)或是(有人的站在Xindian City Hall之後)，套用特殊公式
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
greenLine_dict={"Songshan":1,"Nanjing Sanmin":2,"Taipei Arena":3,"Nanjing Fuxing":4,"Songjiang NanJing":5,"Zhongshan":6,
    "Beimen":7,"Ximen":8,"Xiaonanmen":9,"Chiang Kai-Shek Memorial Hall":10,"Guting":11,
    "Taipower Building":12,"Gongguan":13,"Wanlong":14,"Jingmei":15,"Dapinling":16,
    "Qizhang":17, "Xiaobitan":17.5,"Xindian City Hall":18,"Xindian":19}

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
