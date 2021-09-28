# Day 23：專案05 - KKBOX風雲榜02 | AJAX

###### tags: `2021 IT鐵人賽`

![](https://i.imgur.com/r6y8qkN.png)


昨天已經找到的KKBOX用來傳資料的API，也知道各個參數的意義了，今天就實際將資料抓下來吧!

## 歌曲資訊

回到昨天那個API，是用JSON格式傳遞資料，資料的格式大致如下：

![](https://i.imgur.com/ZPaPdoX.jpg)

我們可以發現新歌的資料都放在 "newrelease" 之下，一個element就是一首歌的資訊，另外，每首歌的資訊也以key:value的形式整理的很清楚。

接著，就用之前教過的`requests.get(url)`直接取得API回傳的資料，但回傳的型態是json字串，所以再用Python本身內建的`json.loads()`函數轉成Python的list和dict資料型態。

```python
# KKBOX華語新歌日榜
url = "https://kma.kkbox.com/charts/api/v1/daily?category=297&lang=tc&limit=50&terr=tw&type=newrelease"
# 取得歌曲資訊json檔
response = requests.get(url)
# 將json字串轉為Python的字典型態
data = json.loads(response.text)
```

既然已經轉成list和dict的型態了，再根據剛才觀察API得知的架構，要篩選資料就非常簡單，直接來看程式碼：

```python
song_list = data["data"]["charts"]["newrelease"]
# 取得每首歌的排名、曲名、連結、作者、時間
for song in song_list:
    song_rank = song["rankings"]["this_period"]
    song_name = song["song_name"]
    song_url = song["song_url"]
    song_artist = song["artist_name"]
    song_timestamp = int(song["release_date"])
    # 從timestamp轉為日期格式
    song_date = time.strftime(
        "%Y-%m-%d", time.localtime(song_timestamp))

    print("排名:", song_rank)
    print("歌名:", song_name)
    print("連結:", song_url)
    print("作者:", song_artist)
    print("發行日期:", song_date)
```

發行時間的部分比較特別，因為資料提供的是時間戳記timestamp，所以要另外用`time.strftime()`函數從timestamp轉為人類習慣的日期格式(年-月-日)。

> **時間戳記(Unix timestamp)**
> 是一種統一的時間標記方式，代表從1970/01/01累積到現在的秒數，透過這個[轉換器](https://www.epochconverter.com/)可以從timestamp轉成人類習慣的時間標記方式，反過來也可以。
> 另外有一件有趣的事，因為有些系統的timestamp用32-bits的int儲存，所以在2038/01/19時這個timestamp就會overflow，又被稱為Year 2038 problem。

執行結果：

![](https://i.imgur.com/Yz2IKn0.png)

## 歌詞

剛才的資訊裡面有一項是連結，而這個連結剛好就是歌詞的連結，隨便挑一首歌，對歌詞的部分**右鍵>>檢查**，發現歌詞就在`class="lyrics"`的`<div>`中。

因此，要得到歌詞這樣寫就好了。

```python
song_response = requests.get(song_url)
soup = BeautifulSoup(song_response.text, "html.parser")
lyric = soup.find("div", class_="lyrics").text
print("歌詞:", lyric)
```

執行結果(抓歌詞因為要get新的網頁，所以會稍微慢一點)：

![](https://i.imgur.com/XmZ2QPB.png)


## 儲存csv檔

儲存資料常用的副檔名除了`.txt`或`.json`之外，`.csv`也是常用的儲存格式，像是excel。

因為這次的資料很格式化，剛好就很適合儲存為csv檔。

首先，開啟一個csv檔，編碼記得要為**big5**，不然只會出現亂碼。`newline=''`則可以避免一些錯誤。

接著，引用Python內建的csv套件，然後建立一個writer物件，用writer物件的`writerow()`寫入一行資料，`writerow()`的參數一定是一個list，list中放要寫入的資料。

歌詞字太多了，放在csv中會很不好看，所以我就不存歌詞了。

```python
import csv

with open('songs.csv', 'w', newline='', encoding="big5") as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)
    # 寫入一列資料
    writer.writerow(["排名", "歌名", "作者", "發行日期", "連結"])
    
    ...
    
    writer.writerow([song_rank, song_name, song_artist, song_date, song_url])
```

結果：

![](https://i.imgur.com/w0uhPye.jpg)

## 換個API

還記得昨天講過各個參數的含意嗎? 其實這裡只要將url後面的參數稍微修改就可以得到其他歌曲種類的排行榜哦!

例如：將category改成390，結果就會是西洋歌曲排行榜。

![](https://i.imgur.com/LZ1ROnH.png)


## 小結

今天告訴你怎麼用Python將API的資料抓下來，並轉成在Python中方便使用的型態，篩選出歌曲資訊後，再利用資訊中的連結取得歌詞，最後將這些資料儲存為csv檔!

這個專案就到這邊，希望你已經學到如何使用AJAX的動態網頁取得資料了，並應用在其他類似的網站上。爬蟲就是這樣，熟能生巧而已，只要爬得多了，自然會有種感覺告訴你該怎麼做。

明天的專案比較大型，預計會分成三天講完，那麼我們明天見~~

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。