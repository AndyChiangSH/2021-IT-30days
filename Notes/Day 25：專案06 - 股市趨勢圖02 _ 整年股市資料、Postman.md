# Day 25：專案06 - 股市趨勢圖02 | 整年股市資料、Postman

###### tags: `2021 IT鐵人賽`

複習一下昨天的進度 - 我們取得單月的個股日成交價的資料，並在電腦中儲存成csv檔。

目前都只有單月的個股日成交價，但如果想要一整年的個股日成交價時，該怎麼辦呢?

![](https://i.imgur.com/Es9i9jm.jpg)


可惜的是，台灣證券交易所並沒有提供一整年的個股日成交價API，不過沒關係，既然沒有一整年的，我們自己將某一年1月到12月的資料合併起來不就是一整年了嗎?

第一步就來觀察API的參數，不過在那之前，我先推薦一個測試API時很方便的工具 - **Postman**。

## Postman

![](https://i.imgur.com/Pjq1rud.png)


[Postman](https://www.postman.com/)是一套專門在測試API的軟體，輸入API的URL和參數後送出，就會回傳API的資料回來，並幫你整理成比較好看的樣子，除了GET之外，也有POST等其他方法可以使用，堪稱**測試API的神器**!

Postman目前有**網頁版**跟**電腦版**，偶爾測試的話網頁版就夠用了，但如果想要更進階的功能，可能就要考慮載電腦版。我這次先用網頁版做示範。

1. 到Postman官網，註冊一個新帳號。
2. 登入後，點左上角「Workspace」，建立一個新的Workspace，如果已經有Workspace了，也可以直接進入下面的清單中的Workspace。

![](https://i.imgur.com/apnakv8.jpg)

3. 進入Workspace後，點「+」符號新增request。

![](https://i.imgur.com/mZFaHhw.jpg)

4. 將昨天API的網址貼上去，就會發現底下將參數都列出來了。確認參數無誤，方法選擇GET後按「Send」送出。

![](https://i.imgur.com/T2YYa5F.jpg)

5. 送出後底下就會出現response，選擇「Pretty」可以讓回傳的JSON資料比較好閱讀。檢查資料是否正確。

![](https://i.imgur.com/FVwsRmd.jpg)

6. 要改變參數也很簡單，直接改參數欄位中的值就好了。比方說，date改成20210701，再次送出後，得到的就是7月的資料了。

![](https://i.imgur.com/T7Izc1p.jpg)

7. 不管在改參數還是檢視資料都勝過在VScode上操作，所以才說是測試API神器阿!
8. 補充：更扯的功能，左邊有個「`</>`」的符號，點擊後下拉式選單選擇「Python-Requests」，就幫你產生這段程式碼出來了，連一點點的code都不用自己寫XD

![](https://i.imgur.com/YJmnE60.jpg)

![](https://i.imgur.com/WSU9wvE.jpg)


## 整年股市

經過測試後，我們發現月份是由「date」這個參數所決定的，因此如果想要一口氣抓下從1月到12月的股市資料，程式碼就長這樣：

```python
# 從1到12月
for m in range(1, 13):
    url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2020{0:02d}01&stockNo=0050".format(m)
    print(url)

    # 取得股票資料json字串
    response = requests.get(url, headers=headers)
    # print(response.text)

    # 從json字串轉為python的字典格式
    json_data = json.loads(response.text)
    datas = json_data["data"]
    fields = json_data["fields"]
```

我抓2020年一整年的股市資料。為了滿足API的格式要求，我用`{0:02d}`搭配`.format(m)`，作用是固定長度為2，不夠補0，比方說1就會變01。

接著，將每個月的資料存成Pandas的DataFrame型態。

```python
# 存成Pandas的Dataframe
month_df = pd.DataFrame(datas, columns=fields)
```

然後，將每個月的DataFrame合併成一個整年的DataFrame。`ignore_index=True`讓合併後資料的index是連續的。

```python
# 合併於整年的Dataframe
year_df = year_df.append(month_df, ignore_index=True)
```

最後只要把整年的DataFrame儲存成`.csv`檔就完成了!

```python
# 轉成csv檔
year_df.to_csv("./year_stock.csv", encoding="big5")
```

結果：

![](https://i.imgur.com/zNXxTBT.gif)


## 小結

回顧一下今天教的內容，首先介紹了測試API的神器 - Postman，以及簡單的操作教學，再來利用Postman測試股市API，找出參數上的規律，最後利用這個規律一口氣把整年的股市資料給抓下來。

明天就是這個專案的最後一天，將利用這兩天得到的資料繪製成趨勢圖! 大家千萬別錯過明天的內容哦!😁😁

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。