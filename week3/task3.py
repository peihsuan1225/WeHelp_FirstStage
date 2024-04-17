import urllib.request as req
import json
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
with req.urlopen(url) as response:
    data = json.load(response)

result = data["data"]["results"]

with open("task3_use.csv","w",encoding="utf-8") as file:
    for info in result:
        spot_title = info["stitle"]
        images = info["filelist"]
        first_image = images.split("https")[1]
        first_image_fullurl = "https"+ first_image
        file.write(f"{spot_title},{first_image_fullurl}\n")