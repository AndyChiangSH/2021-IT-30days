# Day 16：專案03 - PTT 八卦版爬蟲01 | cookie

###### tags: `2021 IT鐵人賽`

![](https://i.imgur.com/79FhOqr.png)

## 偷看一下專案長怎樣

我預期的專案想要完成這幾件事：
1. 取得八卦版每篇**文章的標題、作者和發文時間**。
2. 取得**文章內容**。
3. 取得底下的**留言**，並依照**標籤**分類。
4. 整理資料並匯出成**json**檔案。

![](https://i.imgur.com/kbhBPSU.jpg)


既然昨天已經成功抓到C_Chat板的文章標題了，那八卦板應該依樣畫葫蘆就好了吧?

```python
import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://www.ptt.cc/bbs/Gossiping/index.html")  # 改成八卦板的網址
root = BeautifulSoup(response.text, "html.parser")  # 解析原始碼

links = root.find_all("div", class_="title")    # 文章標題
for link in links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白
```

**結果... 什麼事都沒有發生😱😱** 

怎麼會這樣呢? 我們進[八卦板](https://www.ptt.cc/bbs/Gossiping/index.html)找一下原因到底出在哪裡。

第一次進八卦板時，首先是看到這個畫面，詢問你是否滿18歲，相信大家對這個都不陌生，小時候看到這個一定都是點 "我同意" 對吧😏，點下去後才會到文章列表。

![](https://i.imgur.com/8HOiGFG.png)

所以我猜測之所以會失敗，大概就是因為抓到的是這個畫面而不是文章列表。我們把抓到的原始碼印出來，驗證看看我的猜測是不是對的。

```python
response = requests.get(
    "https://www.ptt.cc/bbs/Gossiping/index.html")  # 改成八卦板的網址
root = BeautifulSoup(response.text, "html.parser")  # 解析原始碼
print(root.prettify())
```

結果果然是抓到這頁了!

![](https://i.imgur.com/6ICtBDi.png)


## Cookie

現在我們知道問題出在哪了，但重點是，我們要怎麼解決這個問題呢? 難道就束手無策了嗎?

先別急著放棄，我們再進PTT八卦板一次，這時你可能會發現，第二次進八卦板時，就不會再問你是否滿18歲了，這是為什麼呢??

我們打開 **F12>>Application>>Cookies**，仔細觀察進PTT八卦板的過程中發生了什麼事。

![](https://i.imgur.com/LiVKv1b.jpg)

> 如果不是第一次進八卦板，請先點右上角的這個圖示清除cookie。清除後再重整一次。
> 
> ![](https://i.imgur.com/aLHwEYB.jpg)

第一次進八卦板時，看到的應該就是詢問是否滿18歲的畫面。然後當我按下 "我同意" 時，cookie會多出一個 over18=1，這就是PTT存在瀏覽器中，記錄我是否點過滿18的cookie。

![](https://i.imgur.com/Dz53JA8.jpg)

再來觀察 **Network>>index.html>>Headers>>cookie**，會發現PTT就是把cookie包裝在Headers中發送出去的。

![](https://i.imgur.com/Fx7fEhw.jpg)

所以我們可以推測，PTT的伺服器應該是在我們點"我同意"時，在我們的瀏覽器中存下了over18=1的cookie，並在請求文章列表的同時，將這個cookie一同送給伺服器做驗證，伺服器驗證OK後就會回傳正確的文章列表回來了。

![](https://i.imgur.com/KXyWvMk.jpg)

現在，解決方法就非常清楚，我們只要**讓程式模擬使用者，發送一個一樣的cookie**，就能順利讓伺服器回傳文章列表了!

程式碼不用改太多，只要多加上cookie和headers。

```python
import requests
from bs4 import BeautifulSoup

my_headers = {"cookie": "over18=1"}  # cookie設定

response = requests.get(
    "https://www.ptt.cc/bbs/Gossiping/index.html", headers=my_headers)  # 放在headers欄位中傳送
root = BeautifulSoup(response.text, "html.parser")  # 解析原始碼

links = root.find_all("div", class_="title")    # 文章標題
for link in links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白
```

執行結果：

![](https://i.imgur.com/ih550HZ.jpg)

果然就成功了!!!

最後來簡單介紹一下cookie：

> Cookie（複數形態：Cookies），又稱「小甜餅」。類型為「小型文字檔案」，指某些網站為了辨別使用者身分而儲存在用戶端（Client Side）上的資料（通常經過加密）。
> 
> -- [維基百科](https://zh.wikipedia.org/wiki/Cookie)

簡單來說，cookie就是伺服器暫存在用戶端(client)這邊的便利貼，上面記錄了你之前的所做過的事情，之後在發相同的請求時，就會連同cookie帶給伺服器，好讓伺服器知道你做過什麼事。

![](https://i.imgur.com/6dc6h4J.png)

## 現在看起來不錯，但好像少了些什麼?

一段時間後你可能會發現，當每次向伺服器送出請求(Request)時，都必須補上cookie，伺服器才會正確的傳回網頁，這是一件很麻煩的事啊，有沒有更好的做法呢?

會這麼問當然就是有啦，想知道嗎? 嘿嘿...明天就會告訴你了~😏

## 小結

今天介紹了PTT八卦板怎麼使用cookie記錄你是否曾經點過 "我同意"，並讓程式模仿使用者做一模一樣的事情。

明天的內容相當精采(會有很多梗圖哦)，千萬別錯過~~

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。