# Day 29：專案07 - 天氣小助理03 | Heroku雲端平台

###### tags: `2021 IT鐵人賽`

![](https://i.imgur.com/6sp6kAN.png)
> 圖片來源：https://www.lohaslife.cc/archives/18537

昨天最後遇到的問題是，目前電腦都是在我們的電腦上執行，而且是手動觸發的，有沒有辦法自動化的完成這個任務呢?

答案是有的，今天將接續前兩天的內容，將天氣小助理的專案部屬到Heroku雲端平台上，建議讀者先看完前兩天的文章再來看這篇哦!


## Heroku

![](https://i.imgur.com/B2cNanv.png)

[Heroku](https://zh.wikipedia.org/wiki/Heroku)是一個平台即服務(PaaS)的雲端平台，支援多種程式語言，包括Ruby、Node.js、Java、Python...。如果是第一次聽到雲端平台的人，可以將它想像成有一台遠端且永遠都是開機狀態的電腦，你可以將你的程式透過網路上傳至這台電腦，並由它幫你執行程式。

接下來教你如何將專案部屬到Heroku上，在此之前要先將天氣小助理的專案完成，這裡有[專案完整原始碼](https://github.com/AndyChiangSH/2021-IT-30days/blob/main/Projects/07_Weather_assistant/app.py)提供參考。

### 安裝Git

Git是一個分散式的版本控制系統，平常除了幫助開發者進行版本控制外，也要透過Git將專案推送到Heroku的Git Repository，進行專案的管理以及部署。

到[Git官網](https://git-scm.com/)，根據作業系統安裝最新版本的Git。

![](https://i.imgur.com/JAvMD7B.jpg)

安裝完成後，在CMD輸入`git --version`，有出現版本號碼就表示有安裝成功。

![](https://i.imgur.com/rEja7sP.jpg)


### 安裝Heroku CLI

Heroku利用Git部署專案，並提供了CLI(Command-Line Interface)，透過指令操作Heroku雲端平台，讓部署流程更加容易。


來到[Heroku Dev Center](https://devcenter.heroku.com/)，點下方的「The Heroku CLI」。

![](https://i.imgur.com/RJqjRV7.jpg)

找到「Download and install」，根據你的作業系統做安裝。

![](https://i.imgur.com/pUPOyXA.jpg)

下載的是一個執行檔，執行後依照步驟安裝即可。

![](https://i.imgur.com/y79wHfa.jpg)

安裝完成後，在CMD輸入`heroku`驗證是否安裝成功。

![](https://i.imgur.com/xhdHmKG.png)


### 註冊Heroku帳號

但是要有帳號才能進行部署，所以先回到Heroku Dev Center，點擊「Sign up」註冊帳號。

![](https://i.imgur.com/4LTiQLE.jpg)

註冊好了之後，因為我們再來會使用**Heroku Scheduler**這個額外的服務，因此需要填寫信用卡的資料，不過不用太擔心，再免費額度用完之前都是不會花到你半毛錢的。

點擊頭像後，點「Account settings」。

![](https://i.imgur.com/8KA6gKi.jpg)

選擇「Billing」，新增你的信用卡資訊。

![](https://i.imgur.com/qm2U6lL.jpg)


### 建立Heroku應用程式

接著，我們要在Heroku雲端平台上建立應用程式，來存放我們天氣小助手的專案。

先在CMD輸入`heroku login`登入Heroku。執行後會導向一個Heroku登入網頁。

![](https://i.imgur.com/U3rVfvR.jpg)

登入完關掉網頁回到CMD，就已經登入完成了。

接著建立應用程式，特別注意應用程式的名稱不可以重複。

```
heroku create <你的應用程式名稱>
```

完成後會產生一組**應用程式的連結**和**遠端Git Repository**，待會的專案就是要推送到這個Repository上。

![](https://i.imgur.com/K1fDGe5.png)

建立一個新資料夾，將專案程式放在資料夾中，為了呼叫方便，於是將程式名稱改名為`app.py`。

為了讓Heroku平台知道這個專案需要安裝那些套件，新增`requirements.txt`檔來紀錄套件和版本的要求。照理來說要建立一個虛擬環境，安裝完必要套件後，用`pip freeze > requirements.txt`產生，但處理起來滿花時間的，這邊就直接提供這個專案`requirements.txt`的內容吧!

```
requests
certifi>=2017.4.17
idna<3,>=2.5
chardet<5,>=3.0.2
urllib3<1.27,>=1.21.1
```

下一步，在CMD上移動到專案資料夾的位置，並建立本地端的Repository。

```
cd /你的專案資料夾路徑
git init
```

接著，使用以下四個指令，將專案推送到Heroku雲端平台。有用過git的人應該明白這就是將本地Repository推送到遠端Repository的過程。

```
git add .  # 將專案加入到本地端Repository
git commit -m "first commit"  # 新增版本紀錄
heroku git:remote -a <你的應用程式名稱>  # 將Heroku雲端平台的Repository切換到你的應用程式
git push heroku master  # 將專案推送到Heroku雲端平台的Repository
```

最後一個指令要等待Heroku安裝一些東西，需要一點時間，完成後如果出現這個畫面，就表示成功推送專案到雲端平台了!。

![](https://i.imgur.com/y4q81ML.png)

### 應用程式測試

回到Heroku的Dashboard，應該就已經有剛才建好的應用程式了。

![](https://i.imgur.com/ZqnoX2l.jpg)

要測試的話，點「More」並選擇「Run console」。

![](https://i.imgur.com/man9cm7.jpg)

輸入`python app.py`，有收到訊息就成功了!

![](https://i.imgur.com/OrzkyR6.jpg)

![](https://i.imgur.com/eTNPKQN.png)


### 建立Heroku Scheduler

真的是最後一步了! 我們要使用**Heroku Scheduler**這個服務，達成每天固定時間執行專案的任務。

在專案中「Resource」下方「Add-ons」搜尋Heroku Scheduler，並點擊它。

![](https://i.imgur.com/S7enyDB.jpg)

下一個視窗中，選擇「Standard-Free」(免費版)。

![](https://i.imgur.com/JbPZliO.jpg)

接著點擊「Heroku Scheduler」服務，在新的分頁中，點擊「Create job」。

![](https://i.imgur.com/OI6jxia.jpg)

選擇排程的時間，因為我們希望**每天固定時間執行**，所以選擇「Every day at...」，後面接執行時間，要注意到Heroku Scheduler採用UTC(世界協調時間)，所以台灣的時間要減8小時才是UTC時間，像專案中希望每天早上6點執行，時間就要設定為**晚上10點**。

執行的指令就和剛才測試的一樣，完成設定後按「Save job」。

![](https://i.imgur.com/aItKTuG.jpg)

排程會列在這邊，未來想修改或刪除都可以。

![](https://i.imgur.com/wdPHdtL.jpg)

最後要做的事就是去睡覺，等待明天一早起來的通知啦~

![](https://i.imgur.com/TWOaX8S.png)
> 圖片來源：https://unsplash.com/photos/uy5t-CJuIK4

參考文章：[[Python爬蟲教學]教你如何部署Python網頁爬蟲至Heroku雲端平台](https://www.learncodewithmike.com/2020/08/deploy-python-scraper-to-heroku.html)


## 小結

故事的結尾，小明來找你道謝，他說他至從有了天氣小助理之後，每天出門前都會收到通知，再也沒有忘記帶雨傘過了。而且因為有暖心提醒，讓他覺得有人在關心他，甚至會開始期待明天的提醒，或許是因為這樣，整個人的氣色也變好了，真是可喜可賀可喜可賀~

我們來複習一下這三天做了什麼事，前天是使用氣象資料的API，昨天是推送LINE Notify訊息，今天則是將專題部署到Heroku雲端平台和設定時間排程器!

天氣小助理的專案到這邊結束，這也是最後一個專案。明天就是鐵人賽最後一天了，我打算做個總複習和寫點完賽心得，那麼，我們明天不見不散!

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。