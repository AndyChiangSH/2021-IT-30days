# Day 24：專案06 - 股市趨勢圖01 | 單月股市API、Pandas

各位早安，今天是第24天，但其實爬蟲的技巧大致上已經教得差不多了，而且我猜會看我的文章的人，應該都想知道爬蟲還可以做哪些應用吧，所以我想鐵人賽的最後幾天，就來做點有趣的專案，順便介紹一些方便的工具給各位~

說到爬蟲，股市價格幾乎是最常見的應用了，雖然爬蟲可以幫你省下很多時間，但抓下來的資料往往是一大堆數字，讓人看得頭昏眼花，這時如果將資料畫成圖表的話，股價的趨勢就可以一目瞭然了。

那麼，我們就來**繪製股市趨勢圖**吧!

![](https://i.imgur.com/EV9SbXa.jpg)
> 圖片來源：https://unsplash.com/photos/fiXLQXAhCfk

## 台灣證券交易所API

首先，資料來源是[台灣證券交易所](https://www.twse.com.tw/zh/)的[個股日成交資訊](https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html)，選擇年份月份和股票代碼後按查詢，底下就會出現該股票當月的成交資訊了。我們發現載入時網站並沒有重新刷新，所以這應該也和昨天的KKBOX一樣，用AJAX技術載入資料。

![](https://i.imgur.com/B0vLwIo.jpg)

打開**F12>>Network**並重新查詢一次，果不其然被我們找到傳遞資料的API了，名稱為`STOCK_DAY?response=json...`。

![](https://i.imgur.com/SXUDxot.jpg)


> **小訣竅：**
> 在尋找API時，只篩選**Fetch/XHR**，可以大幅縮減要尋找的範圍。
> ![](https://i.imgur.com/BMBiS5a.jpg)


其實這個API的參數很單純，**date**表示某年月份的股市資料，**stockNo**則表示股票代碼。

![](https://i.imgur.com/6STF2Aq.jpg)


因為9月還沒過完，為了資料的完整性，我就挑2021年8月作為例子，股票代碼就隨便挑一個 元大台灣50(0050)。

跟昨天一樣抓取資料：

```python
# 台灣證券交易所，個股日成交資訊
url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20210801&stockNo=0050"

# 取得股票資料json字串
response = requests.get(url)
print(response.text)
```

日期至少要在當月之前，不然會回傳這個訊息：

```
{"stat":"查詢日期大於今日，請重新查詢!"}
```

股票代碼也要是真實存在的，不然會回傳這個訊息：

```
{"stat":"很抱歉，沒有符合條件的資料!"}
```

正確情況下，回傳的資料為json格式的字串，一樣使用`json.loads()`轉成python可用的型態。且待會要用到`data`和`field`這兩個資料。

```python
# 從json字串轉為python的字典格式
json_data = json.loads(response.text)
datas = json_data["data"]
fields = json_data["fields"]
```

## Pandas

說到Pandas，你第一個會聯想到什麼? 

...foodpanda嗎? 我看你是餓了吧XD

![](https://i.imgur.com/oVwGFH3.png)

[**Pandas**](https://pandas.pydata.org/)是Python的一個支援**數據操縱和分析**的套件，它的名字衍生自術語「面板數據」(panel data)。Pandas使用特別的資料結構DataFrame儲存資料，並支援多種格式的匯入與匯出，高度的優化讓Pandas在處理數據上非常快速，因此經常在資料探勘(Data Mining)和機器學習(Machine Learning)領域中使用。

現在我們就要將剛才抓到的股市資料存成Pandas的DataFrame，並匯出成csv檔。其實要存成csv檔也可以用昨天教的csv writer，但我想說改教點新的東西，讓大家了解更多Python實用的套件，對大家來說也比較好。

你可能會想說：「為什麼要儲存下來，每次程式都從API抓資料不就好了嗎?」

會儲存下來有三種考量：
1. 台灣證券交易所可不是隨便你爬，他如果發現你太頻繁地呼叫API，就會將你的IP給Ban掉，短時間內你都抓不到資料了(不要不信，我真的被Ban過)
2. 節省網路使用量
3. 像是單月股價這種資料，基本上不太會有變動，所以使用儲存的資料根本就沒差。

那要怎麼將資料轉成DataFrame呢?

```python
# 存成Pandas的Dataframe
df = pd.DataFrame(datas, columns=fields)
print(df)
```

你沒看錯，就是這麼簡單!

因為資料本身就是由List組成的二維陣列，而columns代表橫的欄位，`fields`原本就排好了，所以直接當建構元的參數就好。

![](https://i.imgur.com/AGu4tPJ.png)

印出來大概是這樣，會發現其實已經有點像CSV的格式了。

### Pandas匯出

Pandas有個超讚的優點不得不說，只要將資料整理成DataFrame，只要使用一個函數，就能將資料匯出，而且還支援多種格式，是不是超方便的呢!!

底下示範將資料存成`.csv`檔，excel用的`.xlsx`檔，以及網頁的`.html`檔。另外也支援`.json`和`.sqlite`檔。

```python
# 轉成csv檔
df.to_csv("./month_stock.csv", encoding="big5")
# 轉成xlsx檔
df.to_excel("./month_stock.xlsx", encoding="big5")
# 轉成html檔
df.to_html("./month_stock.html")
```

結果：

`.csv`
![](https://i.imgur.com/sBsB0lt.jpg)

`.xlsx`
![](https://i.imgur.com/wysMmvZ.png)

`.html`
![](https://i.imgur.com/rzKDKfm.png)


## 小結

今天是股市趨勢圖的第一天，進度從台灣證券交易所取得單月股市資料，並將資料轉成Pandas的DataFrame，最後匯出成檔案! 明天沒意外應該會來講怎麼取得整年的資料，我們明天再見~

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。