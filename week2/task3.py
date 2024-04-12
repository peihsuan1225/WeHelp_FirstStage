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