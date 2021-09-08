# Day 03：專案01 - 超簡單個人履歷02 | HTML基本元素

###### tags: `2021 IT鐵人賽`

大家早安阿! 來到我們冒險的第三天了，今天我要繼續來介紹HTML的其他常用元素，還沒看過[昨天的](https://)建議先看完再來看這篇。

## HTML基本元素(續)

### `<img>`

圖片，src屬性為圖片路徑，alt屬性則是圖片無法正常顯示時，預設顯示的文字。

```html
<img src="./cat.jpg" alt="cat" style="width:400px">
```

顯示結果為：

![](https://i.imgur.com/R3eHonf.jpg)

獻上可愛貓貓圖，有貓就給讚，對吧XD

![](https://i.imgur.com/SfznWaA.jpg)

圖片無法正常顯示時，顯示alt的文字。

當然git也可以顯示。

```html
<img src="./rainbow.gif" alt="cat" style="width:400px">
```

![](https://i.imgur.com/BYMjCj0.gif)

> 因為截圖就表示不出來gif的效果了，所以我這邊是直接放git的連結上來，你在你的電腦裡應該也會看到類似效果。

### 表格
HTML中，表格是一個複合的元素，是由好幾個標籤所組成的。

* `<table>`：標示這是一個表格
* `<caption>`：表格標題名稱
* `<thead>`：表頭區域
* `<tbody>`：表格本體區域
* `<tr>`：一列
* `<th>`：表頭欄位
* `<td>`：一般欄位

```
<table>
    <caption>2年1班</caption>
    <thead>
        <tr>
            <th>姓名</th>
            <th>成績</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>王小明</td>
            <td>50</td>
        </tr>
        <tr>
            <td>陳小美</td>
            <td>90</td>
        </tr>
        <tr>
            <td>林阿妙</td>
            <td>75</td>
        </tr>
    </tbody>
</table>
```

顯示結果為：

![](https://i.imgur.com/VjLU5WD.jpg)

如果想要顯示邊框，則在`<head>`裡面加上這個：

```
<style>
    table, th, td {
        border: 1px solid black;
    }
</style>
```

這個用到CSS的內部載入，明天就會講到了。

顯示結果為：

![](https://i.imgur.com/q4utMoC.jpg)

另外，想要合併表格欄位，使用的是`colspan`屬性，數字表示合併幾格。

```
<tr>
    <td colspan=2>林阿妙</td>
</tr>
```

顯示結果為：

![](https://i.imgur.com/Qtdmc3g.jpg)

有關表格的詳細介紹請看[這裡](https://developer.mozilla.org/zh-TW/docs/Web/HTML/Element/table)

### 清單

HTML的清單分成**無序清單**以及**有序清單**。

#### 無序清單

* `<ul>`：標示這是一個無序清單。
* `<li>`：清單中的一項。

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

顯示結果為：

![](https://i.imgur.com/pDHmI8s.jpg)

type屬性可以設定無序清單樣式。

* `disc`：實心圓(預設)
* `circle`：空心圓
* `square`：正方形

```html
<ul>
    <li type="disc">HTML</li>
    <li type="circle">CSS</li>
    <li type="square">JavaScript</li>
</ul>
```

顯示結果為：

![](https://i.imgur.com/56qKiaT.jpg)

或者是巢狀無序清單，瀏覽器會自動切換清單樣式。

```html
<ul>
    <li>HTML</li>
    <ul>
        <li>head</li>
        <li>body</li>
        <ul>
            <li>h1</li>
        </ul>
    </ul>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

顯示結果為：

![](https://i.imgur.com/kDiuTLC.jpg)

#### 有序清單

* `<ol>`：標示這是一個有序清單。
* `<li>`：清單中的一項。

```html
<ol>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ol>
```

顯示結果為：

![](https://i.imgur.com/IvnibLK.jpg)

也可以用`type`屬性設定有序清單樣式。

* `1`：阿拉伯數字(預設)
* `A`：大寫英文字母
* `a`：小寫英文字母
* `I`：大寫羅馬數字
* `i`：小寫羅馬數字

```html
<ol>
    <li type="1">HTML</li>
    <li type="A">CSS</li>
    <li type="I">JavaScript</li>
</ol>
```

顯示結果為：

![](https://i.imgur.com/YOLVEJX.jpg)

`start`屬性設定從數字幾開始數。

```html
<ol start="10">
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ol>
```

顯示結果為：

![](https://i.imgur.com/i0GYkoh.jpg)

當然，也可以是巢狀有序清單，但是瀏覽器**不會**自動切換清單樣式。

```html
<ol>
    <li>HTML</li>
    <ol>
        <li>head</li>
        <li>body</li>
        <ol>
            <li>h1</li>
        </ol>
    </ol>
    <li>CSS</li>
    <li>JavaScript</li>
</ol>
```

顯示結果為：

![](https://i.imgur.com/qLA6FAZ.jpg)

希望改變樣式也很簡單，只要利用上面講過的`type`屬性就好了。

```html
<ol>
    <li>HTML</li>
    <ol type="a">
        <li>head</li>
        <li>body</li>
        <ol type="i">
            <li>h1</li>
        </ol>
    </ol>
    <li>CSS</li>
    <li>JavaScript</li>
</ol>
```

顯示結果為：

![](https://i.imgur.com/GpUa9Pn.jpg)

## 補充：Live Server

這邊介紹一個非常方便的VScode外掛 - [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)。這個外掛會在本地端開啟你的網頁，而且會隨著檔案修改更新網頁，非常適合在開發測試階段使用。

### 使用方法

到VScode側邊欄的Extension，搜尋Live Server，找到後點下去，應該會看到這個畫面：

![](https://i.imgur.com/jMwDdUN.jpg)

因為我已經下載過了，所以沒有install的按鈕，沒下載過的話應該會有。

回到檔案總覽，對著你的html檔案點擊右鍵，然後點 "Open with live Server"，就會在瀏覽器上開啟你的網頁了!

![](https://i.imgur.com/9wrEfsA.jpg)

會看到liver server的host是使用127.0.0.1，也就是[localhost](https://zh.wikipedia.org/wiki/Localhost)，表示的確是本地端的檔案。port會隨機分配，這部分不用特別理他。

![](https://i.imgur.com/jtBJHMd.jpg)

另外，live server會使用你預設的瀏覽器開啟，如果想換成其他瀏覽器，請點上方 **File >> Perferences >> Settings**，然後搜尋 "Live Server"，找到下圖的設定位置。

![](https://i.imgur.com/bYdsqWb.png)

預設是null，可以在下拉式選單選擇你要的瀏覽器。

## 小結

今天延續了昨天的HTML基本元素介紹，多介紹了圖片、表格、清單這三種元素，另外補充了VScode實用的外掛 - Live Server，以後就可以很方便的測試你的網頁了!

HTML的介紹就到這邊，是不是很快就學會了呢~ 明天起，我就會開始代入CSS，來美化網頁了哦(~~我們的網頁終於有衣服穿了~~)，那麼，我們明天見~

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。