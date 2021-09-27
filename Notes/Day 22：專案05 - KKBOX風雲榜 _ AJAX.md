# Day 22：專案05 - KKBOX風雲榜 | AJAX

###### tags: `2021 IT鐵人賽`

歐嗨喲~ 大家昨天有睡飽嗎? 今天又是一個新的專案，當然一樣是爬蟲，但是我完全不用BeautifulSoup一樣可以取得資料，這是怎麼做到的? 好奇嗎? 就讓我們看下去吧!

## KKBOX 華語新歌日榜

今天要來爬的是KKBOX的[華語新歌日榜](https://kma.kkbox.com/charts/daily/newrelease?terr=tw&lang=tc)，可以看到這個網站底下列出了當天新歌的排行榜。

![](https://i.imgur.com/MbMQCsO.png)

你心中一定想說：「反正你一定又是叫我**右鍵>>檢查**對不對?」

NONONO~ 要是這麼簡單就不用我教了，不信你可以試試看直接用requests抓，看看抓不抓的到。

```python
url = "https://kma.kkbox.com/charts/daily/newrelease?terr=tw&lang=tc"
response = requests.get(url)
root = BeautifulSoup(response.text, "html.parser")
print(root.prettify())
```

的確會有回應，但你會發現你不管怎麼找，都找不到你要的資料。這是為什麼呢🤔 ?

答案其實前天就講過了，只是我沒說出來而已。沒錯，KKBOX也是一個**動態網站**，他用的是名叫**AJAX**的技術。


## 什麼是AJAX?

![](https://i.imgur.com/CsHT3xx.png)

> **AJAX**即「**Asynchronous JavaScript and XML**」（非同步的JavaScript與XML技術），指的是一套綜合了多項技術的瀏覽器端網頁開發技術。
> 
> 傳統的Web應用允許使用者端填寫表單（form），當送出表單時就向網頁伺服器傳送一個請求。伺服器接收並處理傳來的表單，然後送回一個新的網頁，但這個做法浪費了許多頻寬，因為在前後兩個頁面中的大部分HTML碼往往是相同的。由於每次應用的溝通都需要向伺服器傳送請求，應用的回應時間依賴於伺服器的回應時間。這導致了使用者介面的回應比本機應用慢得多。
>
> 與此不同，AJAX應用可以僅向伺服器傳送並取回必須的資料，並在客戶端採用JavaScript處理來自伺服器的回應。因為在伺服器和瀏覽器之間交換的資料大量減少，伺服器回應更快了。同時，很多的處理工作可以在發出請求的客戶端機器上完成，因此Web伺服器的負荷也減少了。
> 
> -- [維基百科](https://zh.wikipedia.org/wiki/AJAX)

傳統的網頁應用上，如果想要改變網頁上部分的資料，就一定要將整個網頁重新渲染才行。而AJAX的做法就是只向伺服器取得部分的資料，並使用JavaScript將資料寫上去，這樣的優點是在用戶端和伺服器間傳遞的資料比較少，而且處理速度也會比較快。

資料傳遞的格式通常是用XML或JSON。

回到KKBOX的例子，就是使用AJAX技術匯入資料的。KKBOX先傳給我們一個**只有HTML框架的空殼**，**再用JavaScript將資料填上去**，最後才是我們所見的網頁。


## AJAX 爬蟲

講再多還不如實際操作一次，首先到[KKBOX 華語新歌日榜](https://kma.kkbox.com/charts/daily/newrelease?terr=tw&lang=tc)的網站，**F12**打開開發人員選單，接著到**Network**並重新整理。就會看到網站實際上發送了哪些request和收到哪些response。

> 如果原本已經有東西，請先按clear清除。
> 
> ![](https://i.imgur.com/7OYNWD3.jpg)

第一個檔案的名字就跟網站的URL一樣，從**preview**就可以看出沒有任何資料，這就是我剛才講的空殼，這下就不難理解為什麼用requests怎麼樣都抓不到了吧😏

![](https://i.imgur.com/ioluVYk.jpg)


但我們要的資料究竟在哪裡呢? 前面說過資料通常是以XML或JSON格式傳送，因此我們要向下找出比較可疑的request，畢竟每個網站資料傳送的名稱都不同，這部分就比較憑經驗了。

總之，最後找到是 `daily?category=297&date=2021-09-22...` 這個檔案，要如何驗證呢? 只要preview有出現我們要的資料就好囉!

![](https://i.imgur.com/v5sK4iA.jpg)

KKBOX是用JSON格式傳送，JSON的部分[Day19](https://ithelp.ithome.com.tw/articles/10270992)有講過，沒看過的建議看一下。KKBOX還很貼心地都把資料都整理好了呢，我們就心懷感激地拿來用吧~~

我們還可以觀察到這個request是用GET的method傳遞參數的，多切換幾頁後，大致上就可以猜出參數代表的含意。

![](https://i.imgur.com/iIYKVxi.jpg)

* **category**：分類，華語是297，西洋是390，日語是308
* **date**：日期，哪一天的排行榜
* **limit**：回傳排名前N名的資料
* **type**：歌曲類型，新歌or單曲

只要抓到這個規則後，以後想要什麼資料就直接改GET的參數就行了。

這種根據參數傳回資料的request又稱作[API](https://medium.com/codingbar/api-%E5%88%B0%E5%BA%95%E6%98%AF%E4%BB%80%E9%BA%BC-%E7%94%A8%E7%99%BD%E8%A9%B1%E6%96%87%E5%B8%B6%E4%BD%A0%E8%AA%8D%E8%AD%98-95f65a9cfc33)(Application Programming Interface)，簡單講就是在用戶端和伺服器間傳遞資料的媒介，好比餐廳中位於客人和廚房間的服務生。

其實現在這種動態網站還滿多的，經常用API的形式來交換前端和後端的資料，甚至有API設計的風格規範[RESTful API](https://zh.wikipedia.org/wiki/%E8%A1%A8%E7%8E%B0%E5%B1%82%E7%8A%B6%E6%80%81%E8%BD%AC%E6%8D%A2)，像是GET就是用來取得資料，就當作是補充，有興趣不妨多研究看看。

## 小結

今天教了動態網頁常用到的技術--**AJAX**，了解KKBOX是先傳HTML的空殼，之後再用JavaScript填上資料，並找到KKBOX用來傳遞資料的request，直接取得資料。明天就來講怎麼使用Python將這些資料抓下來吧!

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。