# Day 11：Python基本介紹04 | Set、Dictionary

###### tags: `2021 IT鐵人賽`

おはよう～昨天我們介紹完了四種Collections的其中兩種 - **List、Tuple**，而今天要接續介紹另外兩種 - **Set、Dictionary**。


## Set(集合)

Set是**無序、沒有索引值且沒有重複的成員**的容器，可以想成紀錄糖果口味的清單，因為口味不能重複，所以只有唯一一個。

```python
candyFlavor = {"apple", "strawberry", "mango", "mango"}
print(candyFlavor)
```

Set是用 **大括號** 所包圍，並用 **逗號** 區隔每筆資料。
也可以使用`set()`將產生空的Set，或將其他容器轉為Set。

執行結果：

```
{'mango', 'apple', 'strawberry'}
```

這邊可以注意到"mango"只有唯一一個，而且順序每次都是隨機的。

### 增加新口味

使用`add(data)`在集合中新增資料。

```python
candyFlavor.add("orange")
print(candyFlavor)
```

顯示結果：

```
{'mango', 'apple', 'strawberry', 'orange'}
```

### 移除口味

使用`remove(data)`移除集合中的資料。

```python
candyFlavor.remove("orange")
print(candyFlavor)
```

顯示結果：

```
{'mango', 'apple', 'strawberry'}
```

### 合併集合

將兩個集合合併，重複的元素只會出現唯一一個，就像是你國中學的兩個集合取聯集這樣。

```python
newFlavor = {"apple", "banana"}
candyFlavor.update(newFlavor)
print(candyFlavor)
```

執行結果：

```
{'apple', 'banana', 'mango', 'strawberry'}
```

可以看的出來 "apple" 只有一個。

### 使用時機

Set因為有不可重複的特性(使用hashtable實現)，所以相當適合用於不希望有重複值的場合，像是：水果種類，人名...，可省去檢查是否有重複值的成本。

## Dictionary(字典)

Dictionary也是**無序、沒有索引值且沒有重複的成員**的容器，和Set差別在於資料以一對對的Pair所組成，Pair的語法是`key: value`，一個key對應一個value，key不一定要是字串，但必須是唯一的。
也可以使用`dict()`將產生空的Dictionary。

```python
candyNumber = {"apple": 5, "strawberry": 10, "mango": 3}
```

簡單點可以想像成紀錄糖果口味以及數量的清單，key是糖果口味，value是該口味的數量。

### 藉由口味存取數量

語法是`dict[key]`，利用key來存取數量。`dict[key] = value`就可以改變數量。

```python
print(candyNumber["apple"])
candyNumber["apple"] = 6
print(candyNumber)
```

執行結果：

```
5
{'apple': 6, 'strawberry': 10, 'mango': 3}
```

### 增加新口味和數量

也很簡單，只要給新的key就會產生新的資料。

```python
candyNumber["banana"] = 8
print(candyNumber)
```

執行結果：

```
{'apple': 6, 'strawberry': 10, 'mango': 3, 'banana': 8}
```

### 移除口味

使用`pop(key)`移除該key值的資料。

```python
candyNumber.pop("banana")
print(candyNumber)
```

執行結果：

```
{'apple': 6, 'strawberry': 10, 'mango': 3}
```

### 取得所有口味

使用`keys()`取得所有key值，回傳是所有key的List。

### 取得所有數字

使用`values()`取得所有value值，回傳是所有value的List。

### 取得所有資料

使用`item()`取得所有資料組，回傳是由`(key, value)`所組成的List。

```python
print(candyNumber.keys())
print(candyNumber.values())
print(candyNumber.items())
```

執行結果：

```
dict_keys(['apple', 'strawberry', 'mango'])
dict_values([6, 10, 3])
dict_items([('apple', 6), ('strawberry', 10), ('mango', 3)])
```

### 使用時機

Dictionary跟其他三種容器比較不同，他是複合型的資料型態，也就是由一組key對應到一個value，因此用途非常的廣泛，常用於紀錄兩筆數值間的關係，另外，之後爬蟲會提到的json格式也用到類似的格式，就先記起來吧!


## Collections總整理

Python提供四種Collections，分別是List、Tuple、Set、Dictionary，每個Collection都有各自的特色和使用時機，下面這些不用背起來，經常使用自然就會習慣了。

* **列表(List)**：有序且可更改的容器，允許重複的成員。
* **組合(Tuple)**：有序且不可更改的容器，允許重複的成員。
* **集合(Set)**：無序且未索引的容器，沒有重複的成員。
* **字典(Dict)**：無序且未索引的容器，沒有重複的成員，資料格式為`key: value`。

## 小結

今天介紹了最後兩種容器 - Set和Dictionary各自的特色和使用時機，希望看完這兩天的文章後能幫助你更靈活的使用容器儲存資料><。

因為如果將容器塞在同一天內容會太多，拆開來內容又太少，猶豫過後還是決定拆開來講，所以今天的篇幅比較少一點，請各位見諒OAO。

明天就要來講流程控制和迴圈了，我們明天見!

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。