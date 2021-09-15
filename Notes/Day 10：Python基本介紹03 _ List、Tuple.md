# Day 10：Python基本介紹03 | List、Tuple

###### tags: `2021 IT鐵人賽`

各位早安阿~ 不知不覺間已經來到鐵人賽第十天，也就是過完1/3了呢，想想還真是快。只不過今天就開學了，希望開學後還能堅持下去每天發文😅。

## Collections(容器)

回想一下昨天的情況都是一個變數(Variable)對應到一個資料(Data)對吧? 但如果我們想要存的是好幾筆資料呢? 這時候就要用到Collections了。Python提供四種Collections，分別是**List、Tuple、Set、Dictionary**，每個Collection都有各自的特色和使用時機。因為篇幅有限，今天我們先講前兩個**List和Tuple**：

## List(列表)

List(列表)是一個**有序、可更改、可重複**的一群資料，你可以把它想像成我有一個糖果罐，你按照順序地把一一糖果放進去，你可以隨時拿取這個容器裡的糖果，也可以更改容器裡的糖果口味。

![](https://i.imgur.com/aVCfGpA.png)


### 容器 - 糖果罐

要如何產生一個糖果罐呢? 需要以下指令：

```python
candyCan = ["apple", "strawberry", "grape", "mango"]
```

List是使用 **方括號** 包圍住，並用 **逗號** 區隔每筆資料。
也可以使用`list()`將產生空的List，或將其他容器轉為List。

以上面的例子為例：你產生了一個糖果罐 (List)，並且裡面已經有四種口味的糖果 (資料) 了，分別是apple, strawberry、grape和mango。

Python很方便，只要使用 `print(List名稱)` 就可以顯示List的內容。

### 糖果罐有幾顆糖果?

還記得昨天教的嗎? 使用 `len()` 函式就可以囉。

### 資料型態是...?

像昨天一樣使用 `type()` 檢查，就會發現List的資料型態是一個新的形態，就叫做 `<class 'list'>`。

```python
# demo01
candyCan = ["apple", "strawberry", "grape", "mango"]

print(candyCan)
print(len(candyCan))
print(type(candyCan))
```

執行結果：

```
['apple', 'strawberry', 'grape', 'mango']
4
<class 'list'>
```

### 如何取出糖果?

#### 使用索引值(index)

就如同剛才所說的，List是有序的一群資料，所以資料就像在排隊一樣，每個資料都有一個編號，也就是索引值。

**索引值從0開始(這對寫程式來說非常非常非常重要! 你想要寫程式的話，就一定要先接受這個概念)**，所以第一個資料的索引值是0，第二個資料的索引值是1，其他依此類推。

假如我們現在想要 `strawberry`，它是第二筆資料，所以它的索引值是1，那麼指令就會是：

```python
print(candyCan[1])
```

執行結果：

```
strawberry
```

如果索引值是負的，則代表倒數第幾個。

```python
print(candyCan[-1])
```

執行結果：

```
mango
```

#### 使用區段

就像昨天 Slicing String 一樣，`[n:m]` 表示從n取到m-1，返回一個新的List。

```python
print(candyCan[1:3])
```

執行結果：

```
['strawberry', 'grape']
```

ps. 事實上，你也可以將字串想像成由字元所組成的List，方法大致上是共通的。

### 檢查資料有沒有在List中

使用 `data in list`  來檢查資料有沒有在List中，有則回傳 `True`，沒有則回傳 `False`。

```python
print("apple" in candyCan)
print("banana" in candyCan)
```

執行結果：

```
True
False
```

### 如何改變糖果口味?

很簡單，只要將 `list[index] = newDate` 這樣就好。

```python
candyCan[1] = "peach"
print(candyCan)
```

執行結果：

```
['apple', 'peach', 'grape', 'mango']
```

### 如何增加新的糖果?

#### 添加資料(append)

使用 `append()` 將資料放在List最後面。

```python
candyCan.append("banana")
print(candyCan)
```

執行結果：

```
['apple', 'strawberry', 'grape', 'mango', 'banana']
```

#### 插入資料(insert)

使用 `insert()` 將資料插入List中指定的索引值，原位置的資料會被往後移。

```python
candyCan.insert(1, "orange")
print(candyCan)
```

執行結果：

```
['apple', 'orange', 'strawberry', 'grape', 'mango']
```

#### 合併資料(extend)

使用 `extend()` 將兩個List合併在一起，就像字串的Concatenation。

```python
newCandy = ["banana", "orange"]
candyCan.extend(newCandy)
print(candyCan)
```

執行結果：

```
['apple', 'strawberry', 'grape', 'mango', 'banana', 'orange']
```

### 使用時機

List的使用時機非常的廣，基本上只要你是想存放一堆資料，而且會經常更改其中的值的時候，就很適合使用List。


## Tuple(元組)

Tuple(元組)是一個**有序、不可更改、可重複**的一群資料，特性上跟List滿像的，但差在Tuple不能夠隨意更改裡面的資料。想像Tuple是一個上鎖的糖果罐，只能夠從糖果罐外面查看有什麼糖果，但沒辦法新增、更改和移除裡面的糖果。

```python
candyCan = ("apple", "strawberry", "mango", "peach", "grape")
```

Tuple(元組) 是使用 **圓括號** 包圍住，並用 **逗號** 區隔每筆資料。
也可以使用`tuple()`將產生空的Tuple，或將其他容器轉為Tuple。

不能更改是什麼意思? 看一下以下的例子：

```python
candyCan[1] = "banana"
```

執行後出現這個錯誤訊息：

```
Traceback (most recent call last):
  File "d:\雲端\Code\2021-IT-30days\Code\Day 10\demo08.py", line 3, in <module>
    candyCan[1] = "banana"
TypeError: 'tuple' object does not support item assignment
```

Python就很明確地告訴你了，Tuple不能任意更改資料。

但還是可以查看裡面有什麼資料。

```python
print(candyCan)
print(len(candyCan))

print(candyCan[0])
print(candyCan[1:3])
```

執行結果：

```
('apple', 'strawberry', 'mango', 'peach', 'grape')
5
apple
('strawberry', 'mango')
```

不過基本上List大部分的函式Tuple都不能用，Tuple唯二的函式為 `count()` 和 `index()`，`count()` 用來計算指定資料的數量，`index()` 用來尋找指定資料的索引值。

```python
print(candyCan.count("mango"))
print(candyCan.index("mango"))
```

執行結果：

```
1
2
```

### 使用時機

基本上Tuple用於傳送一組資料時相當好用，因為其不可更改的特性，可以保證資料不會在傳送途中被不小心更改到。

## 小結

今天我們學到Python總共有四種Collections，分別是List、Tuple、Set、Dictionary，通常用於處理好幾筆資料的時候，而我們今天特別講其中兩種，List和Tuple。

- **List** 具有**有序、可更改、可重複**之特性，我們可以輕易的新增、移除、更改List中的資料。
- **Tuple** 具有**有序、不可更改、可重複**之特性，我們不能更改Tuple中的資料，需要先將Tuple轉回List才可以修改。

明天我們會學到Python剩下的兩種Collections，**Set和Dictionary**，敬請期待~

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。