# Day 20：專案04 - Facebook爬蟲01 | ChromeDriver、Selenium

###### tags: `2021 IT鐵人賽`

![](https://i.imgur.com/giY4ZhF.jpg)
> 圖片來源：https://unsplash.com/photos/m_HRfLhgABo

安安，今天是第20天了哦，離結束只剩最後1/3了，感覺時間過得真快呢~ 而且今天又是新的專案了哦! 這次要教的是我自己覺得非常有趣的**Selenium**，讓你的爬蟲技巧再多一招!

前幾天爬PTT八卦板的時候，都是先用requests套件取得網頁的原始碼再做分析，這樣的方法之所以成立，是因為PTT八卦板是屬於**靜態網頁**，意思是網頁畫面一次就全部渲染好了，之後不會再有更動。但有些網站不是這樣(尤其是新的網站)，比方說以Facebook為例，為了載入的效能，Facebook不會一口氣就將所有的貼文都顯示出來，而是你滾輪往下滑時，貼文才會一個個載入，這種網站就稱之為**動態網頁**。

![](https://i.imgur.com/lf5cvl8.gif)

這下子前面教的方法就不管用了阿，沒錯，所以這時就出現了新的方法 -- **Selenium**。

## Selenium

![](https://i.imgur.com/G1iVPCW.png)

[Selenium](https://www.selenium.dev/documentation/webdriver/) 是用於自動化 Web 瀏覽器的工具，可以協助測試人員做自動化測試，也是可以抓網頁內容的動態網頁爬蟲，常搭配 BeautifulSoup 解析 HTML 網頁原始碼。

換句話說，Selenium可以透過指令，模擬出使用者瀏覽網頁的行為，包括：點擊按鈕、輸入文字、滑動滾輪等。

![](https://i.imgur.com/4MYz95G.png)

Selenium主要有三項產品，分別是WebDriver、IDE和Grid，我們要用WebDriver來完成自動化的控制。

Selenium IDE也是滿方便的工具，用於錄製網頁腳本，並提供回放功能，但我沒有實際用過，有興趣的人可以研究看看。

因為Anaconda預設沒有Selenium套件，所以要先下載。

```
pip install selenium
```

## WebDriver

為了讓Selenium可以自動化控制瀏覽器，我們必須先安裝瀏覽器的驅動程式(driver)，這裡提供兩種方式，選一個自己習慣的方式就好。

我都以Chrome瀏覽器為例，其他瀏覽器麻煩自己Google找一下 😅。

### 自己下載

1. 首先，到**Chrome設定>>關於Chrome**，記住自己的版本號碼。

![](https://i.imgur.com/KzGeLOB.jpg)

2. 到[這裡](https://sites.google.com/chromium.org/driver/)下載正確版本的ChromeDriver，只要版本開頭的數字相同就好。

![](https://i.imgur.com/APEo1IU.jpg)

3. 選擇你的作業系統(Window只有32bits的版本，但也不影響使用)。

![](https://i.imgur.com/3FUKdvU.jpg)

4. 下載完後解壓縮，將`chromedriver.exe`移到與程式相同的目錄下。
5. Python程式碼。

```python
from selenium import webdriver
import time

# 開啟下載的chromedriver
driver = webdriver.Chrome("./chromedriver")

# 等待10秒
time.sleep(10)
# 關閉瀏覽器
driver.quit()
```

6. 執行後如果出現這個畫面，並顯示"受到自動測試軟體控制"，就是成功了。

![](https://i.imgur.com/ccQ4TRN.jpg)


### webdriver_manager自動下載

1. 我們要用[webdriver_manager](https://pypi.org/project/webdriver-manager/)這個套件，但Anaconda預設也沒有，所以要先下載。

```
pip install webdriver-manager
```

2. Python程式碼

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# 等待10秒
time.sleep(10)
# 關閉瀏覽器
driver.quit()
```

3. 成功後的結果和第一種是一樣的。

webdriver_manager的優點在於它會自動根據你的Chrome下載正確的版本，就不必擔心版本的問題了。兩種方法大同小異，但我個人比較喜歡用第二種就是了。

## 登入Facebook

下一步就是要登入Facebook，還記得我說過**爬蟲就是要模擬真人的行為嗎**? 想想看我們平常登入的流程是怎樣?

1. 到臉書登入頁
2. 輸入帳號、密碼
3. 按登入按鈕

所以，我們只要讓程式做一樣的事就好了!

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# 你的資訊
url = "https://www.facebook.com/"
email = "YOUR EMAIL"
password = "YOUT PASSWORD"

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(
    ChromeDriverManager().install())

# 最大化視窗
driver.maximize_window()
# 進入Facebook登入畫面
driver.get(url)

# 填入帳號密碼，並送出
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_name("login").click()

# 等待10秒
time.sleep(10)
# 關閉瀏覽器
driver.quit()
```

我來解釋一下為何要這樣寫：

先用 `get(URL)` 進到Facebook登入畫面，因為帳號和密碼的輸入框的id分別是"email"和"pass"，所以用`find_element_by_id()`定位後，再用`send_keys()`模擬使用者輸入帳密。

登入按鈕的name屬性為login，定位後再用`click()`模擬使用者點擊。

但你可能會發現登入後會跳出一個通知，這會害你沒辦法做後續的爬蟲，前面的部分加上以下的設定後，就不會再跳通知了。

![](https://i.imgur.com/DZbljVa.jpg)


```python
# 防止跳出通知
chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.notifications": 2
}
chrome_options.add_experimental_option("prefs", prefs)

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options)
```


## 小結

今天教了怎麼使用Selenium這個套件模擬使用者的行為，以及兩種WebDriver的下載方式，最後利用這些技巧讓瀏覽器自動登入Facebook。明天一樣是Selenium的教學，就來講怎麼爬取每篇貼文的標題吧!

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。