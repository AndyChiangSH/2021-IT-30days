# Day 15：專案02 - PTT C_chat版爬蟲02 | BeautifulSoup

###### tags: `2021 IT鐵人賽`

大家安安，歡迎來到鐵人賽的第15天! 不知不覺已經過完一半了，再努力堅持下去吧!

昨天已經將網站的原始碼抓下來了，然而我們只需要原始碼中特定的幾筆資料而已，所以今天就來講如何解析原始碼，篩選出我們要的資料。

## BeautifulSoup

BeautifulSoup是Python的套件之一，Anaconda預設也已經載好了，如果不是Anaconda環境的人，一樣使用pip安裝下來。

```
// CMD
pip install beautifulsoup4
```

安裝完後就可以在程式碼中引用了。

```python
from bs4 import BeautifulSoup
```

接下來要使用BeautifulSoup解析原始碼，但因為PTT C_Chat版內容太多了，比較不好講解，所以我這邊用`crawl_me.html`作為示範，也可以複製到你的電腦跟著一起做。

```html
<!-- crawl_me.html -->
<!DOCTYPE html>
<html>
<body>
    <div class="main">
        <img src="source.jpg" alt="">
        <h1 class="heading">Heading 1</h1>
        <h2 id="this" class="heading">Heading 2-1</h2>
        <h2 class="heading">Heading 2-2</h2>
        <h2 class="heading">Heading 2-3</h2>
        <div class="container">
            <p>This is a paragraph</p>
        </div>
    </div>
</body>
</html>
```

## 解析原始碼

BeautifulSoup有提供兩種解析器，一種是`html.parser`，另一種是`xml`，因為現在抓到的是HTML，所以選`html.parser`。

解析原始碼後，會返回一個DOM tree的物件，初始位置在文件的root，之後就是對這個物件去操作。

`prettify()`這個函數可以將DOM tree以比較美觀的方式印出。

```python
# 讀檔
response = ""
with open("crawl_me.html", "r", encoding="utf8") as file:
    response = file.read()

# BeautifulSoup解析原始碼
soup = BeautifulSoup(response, "html.parser")
print(soup.prettify())
```

部分執行結果：

![](https://i.imgur.com/xNW8Xn9.png)


## 定位節點

原始碼解析完後是一個樹狀的結構，每一個標籤都代表了一個節點，我們要先定位到想要的節點後，才能取得他的文字或屬性。以下提供四種定位方法

### find()

`find()`函數可以定位符合標籤的第一個節點。

```python
h1 = soup.find("h1")
print(h1)
```

```
<h1 class="heading">Heading 1</h1>
```

也可以定位指定的屬性值。

使用class屬性定位，但因為在Python中已經有`class`保留字了，所以改用`class_`

```python
container = soup.find("div", class_="container")
print(container)
```

```
<div class="container">
<p>This is a paragraph</p>
</div>
```

用id屬性定位。

```python
this = soup.find("h2", id="this")
print(this)
```

```
<h2 class="heading" id="this">Heading 2-1</h2>
```

### find_all()

`find_all()`定位符合標籤的所有節點，回傳的是一個列表。

```python
h2s = soup.find_all("h2")
print(h2s)
print(h2s[1])   # 使用索引值
```

```
[<h2 class="heading" id="this">Heading 2-1</h2>, <h2 class="heading">Heading 2-2</h2>, <h2 class="heading">Heading 2-3</h2>]
<h2 class="heading">Heading 2-2</h2>
```

如果想定位多個標籤，則將標籤打包成一個列表就好了。limit屬性則可以限制數量。

```python
h1_h2s = soup.find_all(["h1", "h2"], limit=3)
print(h1_h2s)
print(len(h1_h2s))
```

```
[<h1 class="heading">Heading 1</h1>, <h2 class="heading" id="this">Heading 2-1</h2>, <h2 class="heading">Heading 2-2</h2>]
3
```

### select_one()

`select_one()`使用CSS選擇器的語法來定位節點，忘記CSS選擇器的人可以到 [Day 04](https://ithelp.ithome.com.tw/articles/10261728) 複習一下。

```python
h1 = soup.select_one("h1")
print(h1)

p = soup.select_one("div.container") # class定位
print(p)

this = soup.select_one("h2#this") # id定位
print(this)
```

```
<h1 class="heading">Heading 1</h1>

<div class="container">
<p>This is a paragraph</p>
</div>

<h2 class="heading" id="this">Heading 2-1</h2>
```

結果和`find()`是一樣的。


### select()

`select()`其實就是使用CSS選擇器語法的`find_all()`啦。回傳是一個列表。

```python
h2s = soup.select("h2")
print(h2s)
print(h2s[1])
```

```
[<h2 class="heading" id="this">Heading 2-1</h2>, <h2 class="heading">Heading 2-2</h2>, <h2 class="heading">Heading 2-3</h2>]
<h2 class="heading">Heading 2-2</h2>
```

## 取得文字

定位到指定的節點後，可以使用`text`或`string`取得文字，或者也可以用`getText()`。

```python
h1 = soup.find("h1")
print(h1.getText())
print(h1.text)
print(h1.string)
```

```
Heading 1
Heading 1
Heading 1
```

## 取得屬性值

對於有屬性值的節點，就用`get("屬性")`或類似字典的方式`["屬性"]`取得屬性值。

我要`<img>`標籤中的`src`屬性值：

```python
img = soup.find("img")
print(img["src"])
print(img.get("src"))
```

```
source.jpg
source.jpg
```


## PTT C_Chat板爬蟲

知道BeautifulSoup如何定位節點和取得文字後，我們就實際來爬爬看PTT C_Chat板每篇文章的標題吧!

目標：PTT C_Chat板的文章標題(紅框圈起來的部分)。

![](https://i.imgur.com/DAqkwV2.jpg)

首先，我們對文章標題 **右鍵>>檢查**，右邊會跳出開發人員介面顯示文章標題在原始碼中的位置。

稍微觀察一下，我們會發現所有的文章標題都在class="title"的div中。

![](https://i.imgur.com/xl3rbDb.jpg)

所以很簡單，程式碼就這樣寫：

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.ptt.cc/bbs/C_Chat/index.html") # 取得C_Chat的HTML原始碼
root = BeautifulSoup(response.text, "html.parser")  # 解析原始碼

links = root.find_all("div", class_="title")    # 文章標題
for link in links:
    print(link.text.strip()) # strip()用來刪除文字前面和後面多餘的空白
```

結果：

![](https://i.imgur.com/z8ZaPEd.png)

第一次爬蟲就完成啦~ 是不是很簡單呢(≧▽≦)


## 小結

今天介紹Python解析HTML原始碼的套件 -- BeautifulSoup，學了幾個定位節點和取得文字的方法，最後現學現賣，爬取PTT C_Chat板的文章標題!

明天我們改成爬PTT八卦板，是不是跟C_Chat板一樣簡單呢? 嘿嘿...明天就知道囉 `ψ(｀∇´)ψ`

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。