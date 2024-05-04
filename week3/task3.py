# 抓取景點名稱與第一張照片，放到task3_use.csv的檔案內
import urllib.request as req
import json
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
with req.urlopen(url) as response:
    data = json.load(response)

result = data["data"]["results"]

with open("task3_use.csv","w",encoding="utf-8") as file:
    for index, info in enumerate(result):
        spot_title = info["stitle"]
        images = info["filelist"]
        first_image = images.split("https")[1]
        first_image_fullurl = "https"+ first_image

        # 如果是最後一行(長度減一是因為index從0開始)，就直接輸出資料不用往下換行(避免出現多一行空值)
        if index == len(result) -1 :
            file.write(f"{spot_title},{first_image_fullurl}")
        else:
            file.write(f"{spot_title},{first_image_fullurl}\n")