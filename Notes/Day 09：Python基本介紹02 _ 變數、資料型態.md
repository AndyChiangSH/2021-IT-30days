# Day 09：Python基本介紹02 | 變數、資料型態

###### tags: `2021 IT鐵人賽`

## ⚠行前通知

考量到有些人可能還沒學過Python，然後我的主題又是定為**從HTML到Python爬蟲的30天之旅**，所以沒辦法，雖然簡單還是要交，因此接下來幾天我會用很基礎的角度來介紹Python，已經學過Python的人可能會覺得有點無聊，這部分可以先跳過，等到開始講爬蟲的部分再回來也沒關係(目前暫定是第13天的時候)。

預防針已經先打好了，那我們就開始吧!

## 輸出

稍微複習一下昨天的程式碼：

```python
print("Hello Python!")
```

昨天說過，`print()`是Python原本就有的函數，可以將`()`中的內容印在終端機(terminal)上。

## 變數

變數是存取資料數值的容器，Python和C語言不同，不需要事先宣告變數的資料型態，而是在初次賦予值的時候決定。

```python
# demo01
name = "Andy"
age = 20

print(name)
print(age)
```

執行結果：

```
Andy
20
```

這時候`name`變數的值就是"Andy"，而`age`變數的值就是20，這個值之後是可以改變的。

也可以將變數印在一起，像是這樣：

```python
# demo02
print("Hi! My name is "+name+", and I am "+age)
```

執行結果：

```
Traceback (most recent call last):
  File "d:\2021-IT-30days\Code\Day 09\02.py", line 4, in <module>
    print("Hi! My name is "+name+", and I am "+age)
TypeError: can only concatenate str (not "int") to str
```

咦? 可是怎麼跑出了錯誤訊息呢? 訊息的意思是 "只能str可以連接str(而不是int)"，這是什麼意思呢? 這部分就不得不提到**資料型態**了。


## 資料型態

對學習程式語言來說，資料型態是相當重要的觀念。一個變數只能是一種資料型態，而不同的資料型態可以做不同的事，並有不同的特性。

Python內建的資料型態大致可以分為三種：

* **文字：**`str` (字串)
* **數字：**`int` (整數),  `float` (浮點數)
* **布林值：**`bool` (真or假)

前面說過Python是在初次賦予值的時候決定變數的資料型態，所以是什麼資料型態取決於`=`之後的值。

使用`type()`函數可以顯示變數的資料型態為何。

```python
# demo03
a = 5
b = "Hello"
c = 0.15
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
```

執行結果：

```
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
```

## 資料型態轉換 (Casting)

將變數強制轉成我們要的變數型態。

- `int()`：將任何的資料型態轉為`int`
- `float()`：將任何的資料型態轉為`float`
- `str()`：將任何的資料型態轉為`string`

回到前面出錯的例子(demo02)，之所以會出錯是因為`+`只能連接字串和字串，而不能字串和數字，所以解決辦法很簡單，就是將整數轉為字串就好了。

```python
# demo04
print("Hi! My name is "+name+", and I am "+str(age))
```

執行結果：

```
Hi! My name is Andy, and I am 20
```


## 輸入

`input()`函數會將讀取你在終端機輸入的內容，而且一律存為字串型態。

另外，可以在`()`中加入提示，提示的文字會顯示在你的輸入的前面。

```python
# demo05
a = input()
b = input("Enter something! ")

print(a)
print(b)
print(type(a))
print(type(b))
```

執行結果：

```
>> 123
>> Enter something! asd
123
asd
<class 'str'>
<class 'str'>
```

現在你可以讓demo04變得更好!

```python
# demo06
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hi! My name is "+name+", and I am "+age)
```

執行結果：

```
>> Enter your name: Andy
>> Enter your age: 20
Hi! My name is Andy, and I am 20
```

這邊有一個小問題要問你們，**剛才的age要使用`str()`轉成字串型態，為什麼這裡就不用了呢?** 好好想一下並把答案寫在留言區吧!

## 字串

字串前面已經出現過了，但現在要講字串使用上更多的技巧。

### 字串長度

使用`len()`得到字串的長度，回傳的是一個數字。

### 第n個字元

將字串視為一個由字元所組成的列表(明天就會講)，每個數字都有索引值，索引值從0開始。

如果要取得第n個字元的話，就是`str[n-1]`。

### 切割字串

`str[n:m]`可以切割從n到m-1的子字串。

### 取代字串

`str.replace("A", "B")`將字串中所有的"A"都取代成"B"。

### 分割字串

`str.split(",")`用逗號將字串分割成好幾個小區塊，並回傳一個字串的陣列。

### 連接字串

`A+B`可以連接A和B字串。

```python
# demo07
a = "Why not to learn "
b = "Python?"

print(len(a))
print(a[2])
print(a[4:7])
print(a.replace("learn", "teach"))
print(a.split(" "))
print(a+b)
```

執行結果：

```
17
y
not
Why not to teach
['Why', 'not', 'to', 'learn', '']
Why not to learn Python?
```

## 數學運算子

數學運算子可以對數字型態的變數作簡單的數學運算，基本上就是你國小就會的加減乘除。

- `+`：加法
- `-`：減法
- `*`：乘法
- `/`：除法
- `%`：取餘數
- `**`：次方

```python
# demo08
x = 12
y = 4

print("x+y = "+str(x+y))
print("x-y = "+str(x-y))
print("x*y = "+str(x*y))
print("x/y = "+str(x/y))
print("x%y = "+str(x % y))
print("x**y = "+str(x**y))
```

執行結果：

```
x+y = 16
x-y = 8
x*y = 48
x/y = 3.0
x%y = 0
x**y = 20736
```

## 註解

不管是什麼程式語言，寫註解都是一個好習慣，不但可以幫助你日後看得懂當初在寫什麼東西，也可以避免被同事白眼w

Python有兩種註解，分別是單行和多行註解，功能上大同小異。

```python
# 這是單行註解

"""
這是多行註解
"""
```

## 小結

今天開始Python基礎教學，從一開始的變數和資料型態，到後來的字串和數學運算子。因為篇幅的關係，你可能會覺得今天教的東西有點雜，但這其實是為了讓你更快速的熟悉Python的語法哦!

明天要教的是Python的四種Collections，是非常好用的資料容器哦! 到底是哪四種呢? 就讓我們繼續 看 下 去~

一不小心發現Python有太多東西可以寫了，所以Python的介紹應該會往後延長一天，對期待Python爬蟲的朋友說聲抱歉😅。

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。