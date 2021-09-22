# Day 17：專案03 - PTT 八卦版爬蟲02 | session、post

###### tags: `2021 IT鐵人賽`

昨天教到使用cookie讓伺服器記得我們曾經做過哪些事，但缺點就是每次Request都要加上cookie才行，非常麻煩。今天就來講怎麼使用session解決這個問題吧~

但在講session之前，我們要先知道為什麼每次Request都要加上cookie?

## 網路的世界

現在網路通訊大多採用HTTP協定，而HTTP是一個「無狀態」的協定。什麼意思呢？就是每一次 request 都是一個「獨立的」request，彼此之間不會有任何紀錄和關聯。所以 Server 那邊也不會保存任何狀態，每一次 request 都視為一個新的 request。

換句話說，你可以把伺服器想成是一個喪失記憶能力的人，每一次你去找他的時候，他都當作是第一次見到你，完全不記得你以前曾經找過他。

就會發生這種事...

![](https://i.imgur.com/bnOHaaD.jpg)

這就是每次Request都要加上cookie的原因，解決方法就是用剛才提到的session~

## 什麼是session?

session的英文意思是 *持續一段時間的狀態*，是一個讓HTTP協定的request變成「有狀態」的機制，有狀態之後才能完成很多功能，像是：登入系統、購物車等等。

要實現session機制可以利用許多方法，其中一種就是用cookie。

還記得昨天這張圖嗎? 利用cookie讓使用者和伺服器間保有狀態的這個機制(或流程)就叫做session。

![](https://i.imgur.com/5CeSZmz.jpg)

想更進一步了解cookie和session的觀念，可以參考這篇文章：  
[白話 Session 與 Cookie：從經營雜貨店開始](https://hulitw.medium.com/session-and-cookie-15e47ed838bc)

## 如何使用session?

Requests內建session物件，使用`session()`函數開啟一段session，便會自動記錄session期間所存的cookie，讓伺服器保留這段session的狀態。

```python
rs = requests.session()
```

剛才我們每次request都要送cookie過去，非常的麻煩，所以才改成用session。但這邊出現一個問題，我們該怎麼讓伺服器對使用者設定cookie呢? 這就要回頭複習剛剛進八卦板的流程了。

1. 先進入 "詢問你是否滿18歲" 的畫面
2. 然後你按了 "我同意"
3. 瀏覽器存下 "over18的cookie"
4. 進入文章列表

先打開 **F12>>Network**，接著完成上述的流程後，應該會看到一個名稱叫over18的request，點開來後可以觀察到request的網址和方法，滑到最下面可以看到他傳了什麼資料。


![](https://i.imgur.com/1fEZZ1D.jpg)

![](https://i.imgur.com/Fv5nvC6.jpg)

可以看到request方法不是剛才用的**GET**而是**POST**，所以接下來就要講GET跟POST到底有什麼不同?

## GET vs. POST

GET和POST都是http協定下所規範的請求方法([request methods](https://developer.mozilla.org/zh-TW/docs/Web/HTTP/Methods))，兩者經常用於向伺服器請求資源，不過兩者在參數(資料)的傳送上採用不同的方法。

### GET
將資料全部寫在URL中，就像你寫明信片一樣，傳遞上較不安全。

GET加上參數的格式：`https://www.example.com/index.html?key1=value1&key2=value2`

### POST
將資料寫在內部，就像你寫信然後裝進信封袋一樣，傳遞上比較安全且傳遞的資訊可以比較多。

所以在點下 "我同意" 按鈕的時候，事實上就是向PTT的伺服器發出一個POST的請求，並帶上`from`和`yes`這兩個資料，伺服器接收到這個POST請求後，就會回應要求瀏覽器設定over18=1的cookie了!

仔細看剛才over18的request，在**Response Headers**有一個欄位是set-cookie，就是在設定cookie。

![](https://i.imgur.com/N817a57.jpg)


## 程式實作

既然原理都知道了，接下來就讓程式模仿使用者做一模一樣的事情就好啦!

```python
import requests
from bs4 import BeautifulSoup

# post要傳的資料
payload = {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}

# 用session紀錄此次使用的cookie
rs = requests.session()
# post傳遞資料
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)
# 再get一次PTT八卦板首頁
response = rs.get("https://www.ptt.cc/bbs/Gossiping/index.html")
print(response.status_code)

root = BeautifulSoup(response.text, "html.parser")
links = root.find_all("div", class_="title")    # 文章標題
for link in links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白
```

執行結果：

![](https://i.imgur.com/uzJp49Z.jpg)

結果跟昨天一樣，但會發現這次在GET的時候就不需要帶上cookie了，因為session會自動幫你帶上。

所以，**好session，不用嗎?**

![](https://i.imgur.com/EnQ9D9k.png)

最後再提一下寫爬蟲時應該具備的觀念。

## 爬蟲重要觀念

**>>> 讓程式模擬真人的行為 <<<**

因為爬蟲會造成伺服器的負擔，所以大部分網站都不歡迎別人來爬他們的網站，因此多數網站都會設下許多障礙阻止爬蟲。

想當然，魔高一尺道高一丈，身為一個工程師，就要想盡辦法**讓你的程式看起來像是真人**，以騙過伺服器的眼睛。


## 小結

今天提到了利用session的機制，讓http協定下的request保有狀態，以及使用POST方法讓伺服器對瀏覽器設定cookie，最後提到爬蟲的重要觀念。今天多數的內容都滿抽象的，但對爬蟲來說都是非常重要的觀念，希望大家看完今天的文章後可以好好吸收，之後在爬蟲會幫助你更加順利。

我原本以為我已經很懂cookie和session的概念，但為了寫這篇文章去查一下資料才發現原來有部分的觀念搞錯了! 後來把這些資料全部讀完吸收後才來寫文章，所以這篇文章的觀念應該都是正確的，不用擔心啦~

這也是為什麼我常常鼓勵人要寫文章的原因，因為有時候自以為正確的觀念，在教人時才發現自己根本就沒有搞清楚。**透過寫文章的方式，便能夠更清楚顯示出自己的弱點在哪裡**。

好啦，題外話就講到這，現在已經可以抓到文章列表了，所以明天就來講怎麼進到文章中，抓下標題、作者等資訊吧!

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。