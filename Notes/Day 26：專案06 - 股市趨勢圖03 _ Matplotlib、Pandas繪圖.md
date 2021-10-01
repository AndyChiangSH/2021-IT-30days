# Day 26：專案06 - 股市趨勢圖03 | Matplotlib、Pandas繪圖

###### tags: `2021 IT鐵人賽`

![](https://i.imgur.com/EynHGuX.jpg)
> 圖片來源：https://unsplash.com/photos/mcAUHlGirVs

前兩天已經將各股日成交資料存成`.csv`檔了，接著就來利用這些資料繪製出趨勢圖吧~

## 匯入Pandas

還記得前天我們將Pandas的DataFrame匯出成csv只靠一個函數嗎? 現在反過來將csv匯入成DataFrame一樣也只需要一個函數哦! 是不是超好用呢😎

試著將前天匯出的三種檔案`.csv`、`.xlsx`、`.html`都匯入成DataFrame看看。匯入的參數大致上和匯出一樣，頂多就編碼要注意一下。

```python
import pandas as pd

# 讀取csv
df1 = pd.read_csv("./month_stock.csv", encoding="big5")
print(df1)

# 讀取excel
df2 = pd.read_excel("./month_stock.xlsx")
print(df2)

# 讀取html
df3 = pd.read_html("./month_stock.html", encoding="utf8")
print(df3)
```

既然可以匯入csv了，就可以用前天儲存的csv檔繪製趨勢圖了! 繪製趨勢圖我會介紹兩種方法：**Matplotlib**和**Pandas**。


## Matplotlib繪圖

[**Matplotlib**](https://zh.wikipedia.org/wiki/Matplotlib)是Python繪製數據圖的套件，待會就要用這個套件將股價繪製成趨勢圖。

Anaconda已經有[matplotlib套件](https://pypi.org/project/matplotlib/)了，沒有的話一樣用pip下載。

```
pip install matplotlib
```

載完後就引進你的專案中，但因為matplotlib太長了，通常會減寫成`plt`。

```
import matplotlib.pyplot as plt
```

再來，篩選出畫趨勢圖需要的資料，要**日期**、**最高價**、**最低價**、**收盤價**這幾個欄位。

```python
# 篩選我們要的資料
date = df["日期"]
high_price = df["最高價"]
low_price = df["最低價"]
end_price = df["收盤價"]
```

`plt.plot()`這個函數就是在圖上繪製一條折線，第一個參數當作x軸，第二個參數當作y軸。因此我們以時間作為x軸，分別畫出以**最高價**、**最低價**和**收盤價**為y軸的折線。

```python
# 繪圖
plt.plot(date, high_price)
plt.plot(date, low_price)
plt.plot(date, end_price)
```

接著加上圖片的一些屬性，待會再用圖說明每個屬性的作用。

```python
plt.xlabel("日期")    # x軸標籤
plt.ylabel("價格")    # y軸標籤
plt.legend(["最高價", "最低價", "收盤價"], loc="lower right")    # 圖示，共有左下、左上、右下、右上四個方位
plt.title("110年8月股市趨勢圖")    # 主標題
plt.grid(True)    # 是否有網格?
```

最後，用`plt.show()`顯示圖片!

```python
# 顯示圖片
plt.show()
```

![](https://i.imgur.com/2acYGaU.jpg)

![](https://i.imgur.com/6nJybpY.jpg)

上方功能列可以執行縮放、拖曳、儲存等動作。

> Matplotlib預設並沒有支援中文字體，因此中文字會變成像下圖這樣的亂碼。
> ![](https://i.imgur.com/zq2YdYl.jpg)
> 解決方法可以參考[這篇教學](https://pyecontech.com/2020/03/27/python_matplotlib_chinese/)。

如果是希望自動存成圖片，請使用`plt.savefig()`這個函數，**記得一定要放在`plt.show()`之前，不然會存空白的圖!**

```
# 存成圖片(一定要放前面!)
plt.savefig("matplotlib_chart.png")
```

雖然說matplotlib預設會給每條線不同顏色，但如果不滿意預設的顏色，還是能夠客製化的。

`color`參數表示線條顏色，用[hex色碼](https://www.shutterstock.com/zh-Hant/blog/how-hex-colors-work)表示，可以到[這裡](https://htmlcolorcodes.com/color-picker/)挑顏色。  
`linewidth`參數表示線條寬度，數字越大越粗。  
`linestyle`參數則表示線條樣式，參數值可以參考[官方文件](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html)。

```python
plt.plot(date, high_price, color="#ff2121")
plt.plot(date, low_price, color="#00bd42", linewidth=5)
plt.plot(date, end_price, color="#005de0", linestyle="dashed")
```

![](https://i.imgur.com/ynacQV7.jpg)


## Pandas繪圖

嘿嘿~其實Pandas本身就有繪圖功能囉，那你可能會想，那我還學Matplotlib幹嘛?? 事實上，Pandas的繪圖功能有一部份也是依靠Matplotlib的，所以還是要學啦~

Pandas在繪圖前要先把資料整理成DataFrame的型態，雖然匯入的資料本身就是DataFrame了，但是我們只需要其中一部分的資料而已，因此我們要先將我們要的欄位篩選出來，跟上面一樣，要**日期**、**最高價**、**最低價**、**收盤價**這四個欄位。

接著，要定義一個欄位當作x軸，這邊當然就是用日期欄位。

```python
# 篩選我們要的資料
chart_df = df[["日期", "最高價", "最低價", "收盤價"]]
# 將日期設為x軸
chart_df.set_index("日期", inplace=True)
print(chart_df)
```

資料整理完後，繪圖就變得很簡單，只需要用`plot()`這個函數，屬性設定一下就可以了!

```python
# 繪圖
chart = chart_df.plot(xlabel="日期", ylabel="價格", title="110年8月股市趨勢圖", legend=True)
plt.grid()
```

> 中文字體問題的解決方法和Matplotlib一樣，請參考上方說明。

最後存檔和顯示圖片的方法與Matplotlib一致。

```python
# 存成圖片(一定要放前面!)
plt.savefig("pandas_chart.png")
# 顯示圖片
plt.show()
```

結果如下：

![](https://i.imgur.com/9rH8Etu.jpg)

趨勢圖就完成了! 至於後續要怎麼應用就看各位的想像力啦!

[專案完整程式碼](https://github.com/AndyChiangSH/2021-IT-30days/tree/main/Projects/06_Stock_price)


## 小結

今天一開始先教大家怎麼從匯入csv檔，然後使用Matplotlib和Pandas這兩種不同方法將股市資料繪製成趨勢圖。

股市趨勢圖的專案就到這邊! 明天開始會教你如何做出天氣小助手，每天早上通知你今天的天氣情形，大家敬請期待~

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。
