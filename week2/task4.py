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