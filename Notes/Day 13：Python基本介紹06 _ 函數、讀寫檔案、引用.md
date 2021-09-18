# Day 13：Python基本介紹06 | 函數、讀寫檔案、引用

###### tags: `2021 IT鐵人賽`

早安安! 今天是Python基本介紹的最後一天了~ 6天真的太短了，有好多東西想講但都講不完 ಥ⌣ಥ，因此我打算今天就把幾個之後爬蟲會用到的幾個技巧介紹完，內容可能有點雜，請多見諒。

## 函數(Function)

![](https://i.imgur.com/4kalQJL.png)

函數最基礎的定義就是：給定一個輸入x，經過function後，得到一個輸出f(x)。

大家國中學過的一元多項式，就是一個簡單的函數，舉例：

y = x^2+2x+1

這是一個一元二次的多項式，如果我們x代入2，y就等於2^2^+2*2+1 = 9，也可以寫成函數形式f(2) = 9。

了解完函數後，其實Python的函數也差不了太多，也是一個輸出得到一個輸入，只是輸入跟輸出的型態更自由了!

Python中使用`def`宣告函數，後面接函數名稱以及參數。

並使用`函數名稱(參數1, 參數2, ...)`呼叫參數。

那麼，請你告訴我，底下這個算不算是一個函數呢?

```python
def hello():
    print("Hello, World!")

hello()
```

執行結果：

```
Hello, World!
```

這當然也是函數囉，只不過沒有輸出和輸入，單純印出 "Hello World" 而已。

順帶一提，因為Python是直譯式語言，是從頭開始直譯下來的，所以函數一定要定義在呼叫前面哦!

我們試著輸入參數：

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Andy")
```

執行結果：

```
Hello, Andy!
```

這邊我們傳入字串"Andy"作為參數`name`，於是在函數中印出 "Hello, Andy!"。

這次寫個函數，輸入兩個數字，回傳兩個數字的總和：

```python
def sum(x, y):
    return x+y
    
print(sum(1, 2))
```

結果：

```
3
```

Python使用`return`作為函式的回傳，讀到`return`後就會跳出函數了並回傳數值。所以上面例子，我們傳入1和2，最後函數就回傳1+2 = 3。

使用時機是將**重複性高的工作寫成函數**，可以大大提升程式碼的重用性和精簡度。

## 讀寫檔案(I/O)

Python讀寫檔案使用`open()`這個函數，語法為`open(檔案名稱, 模式)`。

```python
file = open("demo_en.txt", "r")
```

檔案名稱沒有特別寫的話就是相對位置，起始位置為程式所在的資料夾，寫完整路徑的話就是絕對位置。

模式主要有三種，讀(r\)、寫(w)、添加(a)，以及二進位模式。

* **r**：唯讀模式，只能讀取檔案
* **w**：寫入模式，如果檔案不存在會建立新檔，如果存在則**覆蓋**掉之前的內容。
* **a**：添加模式，如果檔案不存在會建立新檔，如果存在則**添加**在之前的內容之後。
* **rb、wb、ab**：加上b後就是二進位模式，通常用於讀取圖片。

如果檔案中有中文字，則要將編碼設定成**utf-8**，否則會出錯。

```
file = open("demo_ch.txt", "r", encoding="utf-8")
```

開始檔案後使用`read()`函數讀取所有內容。

別忘了檔案操作完後一定要關檔哦，不關會導致更改沒有存檔，而且也浪費了記憶體。關檔用到`close()`函數。

```python
file = open("demo_en.txt", "r")

content = file.read()
print(content)

file.close()
```

另外，`readlines()`可以依照行讀取整個檔案，回傳是一個List，每一個element就是一行字。

```python
file = open("demo_en.txt", "r")

lines = file.readlines()
print(lines)

file.close()
```

執行結果：

```
['Country road, take me home\n', 'To the place I belong\n', 'West Virginia, mountain mamma']
```

我發現歌詞中少了一句，所以我要用**添加模式(a\)**+`write()`函數補上漏掉的那一句。

```python
file = open("demo_en.txt", "a")

file.write("Take me home, country road\n")

file.close()
```

如果常常忘記關檔怎麼辦，Python有提供with的寫法，離開範圍是就會自動關檔了，是不是很貼心呢! 我個人也比較建議這個寫法。

```python
with open("demo_en.txt", "r") as file:
    content = file.read()
    print(content)
```


## 引用(import)

前面有提到，Python之所以受歡迎，很大的原因是因為他擁有廣大的社群，提供非常多的套件和資源可以使用，你如果夠厲害也可以自己寫套件回饋給社群，而我們現在就要學怎麼使用這些套件。

Python本身內建就包含很多套件了，另外Anaconda本身也預先載好了很多常用的套件，如果還是沒有你要的，還是可以使用Python的套件管理工具(pip)進行安裝。

只要 `import+模組名稱` 就可以在程式碼中使用了，我們這邊先拿內建就有的math套件做例子，使用math套件中的`log()`函數取1024以2為底的log：

```python
import math
print(math.log(1024, 2)) # 10
```

你可能覺得寫math太麻煩，可以用 `as` 改成縮寫。

```python
import math as m
print(m.log(1024, 2))
```

或者你不想要引用整個套件，你只想要引用math套件中的`log()`函數而已，可以用 `from` 的方式寫。

```python
from math import log
print(log(1024, 2))
```

之後爬蟲會用到很多套件，到時候再一一做介紹。

## 小結

今天是Python基礎介紹的最後一天，我整理了幾個之後專案會用到的重點，像是**函數、讀寫檔案、引用**，希望能快速讓你對Python有點認識。

前幾天都在介紹Python多少覺得有點悶(我自己也寫得很悶)，不過別擔心，明天我們就要開始進入文章的重頭戲 - **網頁爬蟲**!! 想學網頁爬蟲的朋友千萬別錯過明天我要和你分享的內容囉~

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。