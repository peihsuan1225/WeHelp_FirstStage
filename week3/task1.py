import urllib.request as request
import json
url1="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
url2="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
# 存取url的內容，用json模組處理 json資料格式
with request.urlopen(url1) as response1:
    data1 = json.load(response1)

results1 = data1["data"]["results"]

with request.urlopen(url2) as response2:
    data2 = json.load(response2)

results2 = data2["data"]

# 建立字典，存放 景點編號:景點隸屬行政區
no_adress_dict = {}
# 建立字典，存放 景點編號:捷運站
no_mrt_dict = {}
# 把地址分割處理，提取出區域(先用空格分割、再用"區"分割)
for item in results2:
    no_adress_dict[item["SERIAL_NO"]] = (item["address"].split(" ")[2]).split("區")[0]
    no_mrt_dict[item["SERIAL_NO"]] = (item["MRT"])
# print(no_adress_dict)


# 開啟一個spot.csv檔案，寫入指定的內容
with open("task1_spot.csv","w",encoding="utf-8") as file:
    # 遍歷 results1 取得對應的標題、編號、經緯度、圖片連結
    for infos in results1:
        SpotTitle = infos["stitle"] 
        # 取得編號後，對應到字典中的隸屬行政區
        spotNo = infos["SERIAL_NO"]
        District = no_adress_dict[spotNo]
        Longitude = infos["longitude"]
        Latitude = infos["latitude"]
        ImageURL = infos["filelist"]
        FirstImageURL = ImageURL.split("https")[1] # 將 ImageURLs 以空格分割，並只取第一個圖片連結
        file.write(SpotTitle + "," + District + "區" + "," + Longitude + "," + Latitude + "," + "https" + FirstImageURL + "\n")

# 建立一個mtr_spot_dict字典，存放捷運站名(不重複):景點名
mtr_spot_dict={}
# 開啟一個mrt.csv檔案，寫入指定的內容
with open("task1_mrt.csv","w",encoding="utf-8") as file:
    # 在第一個連結的資料中，取出景點編號對應到no_mrt_dict字典的捷運站，把捷運站加到mtr_spot_dict中當做key
    for infos1 in results1:
        spotNo = infos1["SERIAL_NO"]
        MRT = no_mrt_dict[spotNo]
        if MRT not in mtr_spot_dict:
            mtr_spot_dict[MRT] = []
    # 在第二個連結的資料中，取出景點編號、捷運站
    for infos2 in results2:
        spotNo = infos2["SERIAL_NO"]
        MRT = infos2["MRT"]
        # 將第二個連結取出的景點編號跟第一個連結取出的景點編號比對，如果相等在mtr_spot_dict把對應的捷運站key加上景點名稱的value
        for infos1 in results1:
            if spotNo == infos1["SERIAL_NO"]:
                mtr_spot_dict[MRT].append(infos1["stitle"])
    # print(mtr_spot_dict)
    # 遍歷mtr_spot_dict的鍵值，印出捷運站,景點名稱1,景點名稱2,...
    for mrt, spots in mtr_spot_dict.items():
        file.write(mrt + ",")
        for spot in spots:
            file.write(spot + ",")
        file.write("\n")

   

        