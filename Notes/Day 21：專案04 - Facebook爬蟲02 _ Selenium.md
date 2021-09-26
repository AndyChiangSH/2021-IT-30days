# Day 21：專案04 - Facebook爬蟲02 | Selenium

###### tags: `2021 IT鐵人賽`

![](https://i.imgur.com/J8UCPUJ.png)

昨天結束在Facebook登入之後，今天就接續昨天的內容，以[木棉花的粉絲專頁](https://www.facebook.com/emuse.com.tw)為例，來講怎麼爬下來貼文的內容吧!

![](https://i.imgur.com/gBWl7jj.jpg)

## 進到木棉花粉專

```python
time.sleep(5)

# 進入木棉花專頁
driver.get("https://www.facebook.com/emuse.com.tw")

time.sleep(5)
```

其實就跟昨天一樣，使用`get()`函數進到木棉花的粉專。

`time.sleep()`設定延遲是為了讓Facebook有處理資料的時間，這點在使用Selenium時很重要，如果你都不給延遲時間，就有可能因為資料還沒載入而出錯。

## 模擬滾輪下滑

![](https://i.imgur.com/1OQkllP.gif)

昨天已經講過了Facebook必須往下滑動才會載入資料，所以現在就要讓Selenium模擬出使用者滑鼠往下滑動的行為。

```python
# 往下滑3次，讓Facebook載入文章內容
for x in range(3):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("scroll")
    time.sleep(5)
```

這邊是讓Selenium執行JavaScript的程式，雖然我沒有講過JavaScript，但你只要知道這段程式就是控制瀏覽器向下滑1頁。而且每次下滑後都要給一點延遲時間載入資料。

## 擷取貼文內容

接下來，我們對貼文**右鍵>>檢查**，發現到內容放在一個`class="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q"`的`<div>`中。

![](https://i.imgur.com/6iN3jEM.jpg)

再往下看，每一行文字都是放在`dir="auto"`的`<div>`中。

![](https://i.imgur.com/RpwfNXn.jpg)

好，那麼程式碼就是這樣。

```python
# 定位文章標題
titles = soup.find_all(
    "div", class_="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q")
for title in titles:
    # 定位每一行標題
    posts = title.find_all("div", dir="auto")
    # 如果有文章標題才印出
    if len(posts):
        for post in posts:
            print(post.text)

    print("-" * 30)
```

執行結果：

![](https://i.imgur.com/v1Q4IXK.png)


## 下載圖片

呀咧呀咧，發現今天的內容有點太少了，再加碼講個下載圖片好了。

首先，我們觀察到Facebook的圖片有兩種，一種是單純一張圖片，另一種是相簿，然後這兩種的class分別是`"i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm bixrwtb6"`和`"i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm"`。

所以就用`find_all()`搜尋所有的圖片吧! 將兩種class放在list中就可以了。

```python
images = root.find_all(
    "img", class_=["i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm bixrwtb6", "i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm"])
```

下載圖片前，我們要先取得圖片的來源位置，就放在`src`屬性中，並且用requests將圖片內容給抓下來。接著，我們要在我們的電腦中開啟新檔來存這個圖片，因為我們知道圖片其實就是由很多pixel所組成的二進位檔案，所以模式要設為**wb**。最後，將圖片內容寫進檔案就完成了!

因為檔名如果相同的話會被覆蓋過去，所以給每張圖片一個流水號。另外，因為圖片應該會滿多的，所以將圖片集中儲存在images這個資料夾內。

```python
# 下載圖片
images = root.find_all(
    "img", class_=["i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm bixrwtb6", "i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm"])
if len(images) != 0:
    for index, image in enumerate(images):
        img = requests.get(image["src"])
        with open(f"images/img{index+1}.jpg", "wb") as file:
            file.write(img.content)
        print(f"第 {index+1} 張圖片下載完成!")
```

成果展示：

![](https://i.imgur.com/vWfbxO1.gif)

[完整原始碼連結](https://github.com/AndyChiangSH/2021-IT-30days/blob/main/Projects/04_Selenium_facebook/facebook_crawler.py)


## 小結

今天繼續昨天的Facebook爬蟲，用更進階的技巧模擬使用者下滑的動作，後來又回到熟悉的BeautifulSoup解析原始碼，取得貼文的內容以及下載圖片~

Selenium部分就介紹到這邊，其實還有很多東西可以玩，不過就給大家自己去探索囉! 明天要來講另外一種進階的爬蟲方式 -- AJAX，敬請期待~~

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。