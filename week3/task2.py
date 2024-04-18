# 導入urllib.request模組 與 設定目的網址
import urllib.request as req

def getData(url,open_mode):
    # 模擬真人透過瀏覽器造訪ptt樂透版的網頁請求
    request = req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    })
    # 透過請求造訪網頁，並獲取樂透版網頁內容存放在data中
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # 導入Beautiful Soup 4 模組
    import bs4
    # 打開一個article.csv的檔案
    with open("task2_article.csv",open_mode,encoding="utf-8") as file:
        # 用bs4解析網頁的HTML內容
        root = bs4.BeautifulSoup(data,"html.parser")
        # 抓取 class=r-ent的div(裡面包含貼文的所有資訊)
        rents = root.find_all("div",class_="r-ent")
        for rent in rents:
            # 抓取 在rent下 class=title 的 div
            title = rent.find("div",class_="title")
            # 如果文章標題沒有=None(即文章標題存在)
            if title.a != None:
                article_text = title.a.string
                # 抓取 在rent下 class=hl 的 span
                counts = rent.find("span",class_="hl")
                # 如果沒有值，就帶入"0"
                if counts is None:
                    counts = "0"
                for count in counts:
                    counts_text = count
                # 獲取文章連結
                article_link = title.a["href"]
                full_url = "https://www.ptt.cc"+ article_link
                # 模擬真人透過瀏覽器造訪文章網頁的請求
                request = req.Request(full_url,headers={
                    "cookie":"over18=1",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
                })
                # 透過請求造訪網頁，並獲取文章網頁內容存放在article_data變數中
                with req.urlopen(request) as response:
                    article_data = response.read().decode("utf-8")
                    # 用bs4解析文章網頁的HTML內容
                    root_article = bs4.BeautifulSoup(article_data,"html.parser")
                    
                    # 抓取文章的貼文時間
                    metalines = root_article.find_all("div", class_="article-metaline")
                    for metaline in metalines:
                        tag = metaline.find("span", class_="article-meta-tag")
                        # print(metaline)
                        if tag and tag.string == "時間":
                            value = metaline.find("span", class_="article-meta-value")
                            if value is None:
                                date = ""
                            else:
                                date = value.string
                # 寫入檔案(文章標題,按讚/倒讚數，發布時間)
                file.write(f"{article_text},{counts_text},{date}\n")
        # 回傳上一頁的連結
        nextlink = root.find("a",string="‹ 上頁") #找到內文是‹ 上頁 的a標籤
        return nextlink["href"] # 回傳這個標籤的href屬性

pageurl="https://www.ptt.cc/bbs/Lottery/index.html"
# 用迴圈跟函式來抓取前三頁的資料，並把檔案的mode設定為第一頁是w(清空>賦值)，二三頁是a(追加內容)
count = 0
while count<3:
    if count == 0:
        mode = "w"
    else:
        mode = "a"
    pageurl="http://www.ptt.cc"+getData(pageurl,mode)
    count +=1

