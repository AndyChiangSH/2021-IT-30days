# Day 28：專案07 - 天氣小助理02 | LINE Notify

###### tags: `2021 IT鐵人賽`

![](https://i.imgur.com/Vmv4g5d.png)
> 圖片來源：https://3c.ltn.com.tw/news/45392

現在已經是人手一機的時代了，基本上大家每天起來後一定會做的事情就是打開手機檢查訊息，其中LINE又幾乎是每個人都有的通訊軟體，比起將訊息印在終端機或存成txt檔，傳送LINE訊息肯定是更方便且更容易接收訊息的選擇。今天就來使用LINE Notify，將氣象資料用LINE傳給我吧!

## LINE Notify

![](https://i.imgur.com/bF17kZB.png)

LINE Notify是LINE一個特殊的官方帳號，是一個專門用來推送訊息的LINE機器人，特點是只要去申請一個服務提供者，就會以LINE Notify的帳號主動推送訊息給使用者! 而且最大的優點在於，他不像LINE Bot要收費，LINE Notify推送訊息是**完全免費**的! 適合用於傳送客戶通知或現有服務的錯誤訊息。

底下就來教你如何使用LINE Notify。

1. 來到[LINE Notify](https://notify-bot.line.me/zh_TW/)網頁，登入你的LINE帳號。

![](https://i.imgur.com/1ExCCGN.jpg)

2. 登入後，點「個人頁面」。

![](https://i.imgur.com/ZpfvN9a.jpg)

3. 點發行存取權障底下的「發行權杖」。

![](https://i.imgur.com/SIK7Gc0.jpg)

4. 輸入權杖名稱(通常是填功能名稱，像是**天氣小助理**)，底下選擇要推送訊息到哪個聊天室，如果只給自己看的話就選擇「透過1對1聊天接收LINE Notify的通知」，填完後按「發行」。

![](https://i.imgur.com/e3fLhoh.jpg)

5. 發行後顯示權杖，**請務必將這個權杖記住**，不然離開這頁後就不會再顯示囉!

![](https://i.imgur.com/V4dLFMj.jpg)

6. 畫面上會出現目前申請的權杖，如果未來這個權杖不小心外流了，可以來這裡解除。

![](https://i.imgur.com/k1lMkg8.jpg)


## 傳送測試訊息

取得權杖後就可以試著傳送訊息了! LINE Notify使用POST的方式將權杖以及訊息送到LINE Notify的API，接著再將訊息傳給這個權杖所綁定的使用者。

程式碼如下：

```python
import requests

def line_notify():

    token = "你的權杖"
    message = "Hello! 這是測試文字!"

    # line notify所需資料
    line_url = "https://notify-api.line.me/api/notify"
    line_header = {
        "Authorization": 'Bearer ' + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    line_data = {
        "message": message
    }

    requests.post(url=line_url, headers=line_header, data=line_data)


if __name__ == '__main__':
    line_notify()

```

結果：

![](https://i.imgur.com/OiIYsoJ.jpg)


## 傳送天氣訊息

再來結合昨天的氣象資訊，回傳氣象通知的訊息吧!

因為要傳的參數有點多，所以我們將資料打包成tuple，雖然說傳遞上比較安全，但麻煩的就是要記住每個參數的索引值。

```python
line_notify(tuple([location, start_time, end_time, weather_state, rain_prob, min_tem, comfort, max_tem]))
```

因為也有無法取得氣象資訊的情況(status code不等於200)，就傳一個空的tuple就好。

```python
line_notify(tuple())
```

再來就只要將資料依序填入訊息字串中就好了，這部分不需要跟我一模一樣，你也可以客製化自己的訊息! 另外，如果收到的是空tuple，就是沒有取得資料的情況，所以回傳錯誤訊息就好。

感覺訊息太過死板嗎? 我們可以加上一些簡單的條件判斷，在下雨機率很高、很冷或很熱的時候，給你一句暖心的提醒! ~~假裝是女朋友的提醒，安慰一下孤單寂寞覺得冷的心QQ~~

```python
def line_notify(data):

    token = "你的權杖"
    message = ""

    if len(data) == 0:
        message += "\n[Error] 無法取得天氣資訊"
    else:
        message += f"\n今天{data[0]}的天氣: {data[3]}\n"
        message += f"溫度: {data[5]}°C - {data[7]}°C\n"
        message += f"降雨機率: {data[4]}%\n"
        message += f"舒適度: {data[6]}\n"
        message += f"時間: {data[1]} ~ {data[2]}\n"

        if int(data[4]) > 70:
            message += "提醒您，今天很有可能會下雨，出門記得帶把傘哦!"
        elif int(data[7]) > 33:
            message += "提醒您，今天很熱，外出要小心中暑哦~"
        elif int(data[5]) < 10:
            message += "提醒您，今天很冷，記得穿暖一點再出門哦~"

    # line notify所需資料
    line_url = "https://notify-api.line.me/api/notify"
    line_header = {
        "Authorization": 'Bearer ' + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    line_data = {
        "message": message
    }

    requests.post(url=line_url, headers=line_header, data=line_data)
```

結果還不錯哦!

![](https://i.imgur.com/yQOwmcT.jpg)

你也可以更改參數，試試看暖心提醒是否有發揮功能。

例如，將下雨機率改成90%：

![](https://i.imgur.com/jVa4eRJ.jpg)

最高溫改成35度：

![](https://i.imgur.com/o0jblFw.jpg)

最低溫改成5度：

![](https://i.imgur.com/KsKCgzF.jpg)


## 小結

今天使用LINE Notify推送氣象資訊的LINE訊息，也加上了暖心的提醒語，小明的問題應該已經解決了吧?

這時你才察覺到一個嚴重的問題，目前程式都是在我們的電腦上運行，而且要我按執行後才會推送訊息，但總不可能叫我電腦隨時都開著，而且每天六點爬起來按執行吧? 就算小明是我好朋友，但還是沒有比睡眠時間來的重要，那這下該怎麼辦呢?

明天就要教你將程式部署到HEROKU雲端主機上，並每天固定時間執行哦! 明天教的內容真的超實用(認真推)，不看就虧大了!

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。
