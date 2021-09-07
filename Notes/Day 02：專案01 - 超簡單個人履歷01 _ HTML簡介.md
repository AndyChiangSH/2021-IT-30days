# Day 02：專案01 - 超簡單個人履歷01 | HTML簡介

###### tags: `2021 IT鐵人賽`

## 專案介紹

這個專案會帶你使用HTML和CSS，打造專屬於你的[個人履歷網頁](https://andychiangsh.github.io/2021-IT-30days/Projects/01_My_first_resume/main.html)。

預覽圖：

![](https://i.imgur.com/c70RxWk.jpg)

首先，我們從HTML入門吧!

## HTML是什麼?
**HTML**全名是**HyperText Markup Languag**，中文是**超文本標記語言**，是一種用於建立網頁的標準標記語言。HTML是一種基礎技術，常與CSS、JavaScript一起被眾多網站用於設計網頁、網頁應用程式以及行動應用程式的使用者介面。網頁瀏覽器可以讀取HTML檔案，並將其渲染成視覺化網頁。

簡單來說，HTML就像是網頁的骨架，決定了網頁該長什麼樣子。CSS則像網頁的衣服，決定了網頁的顏色以及圖案，而JavaScript則像大腦，處理更複雜的邏輯運算和觸發事件。

因此我們要做網頁的第一步就是要先將骨架打造出來。

ps. HTML只是一種標記語言，並不是程式語言! 以後別人問你會什麼程式語言，千萬別說HTML，這可是會被笑的...

## HTML元素
HTML全部都是由 **元素(elements)** 所組成的，而元素包含了 **標籤(tags)** 與 **內容(content)**。

元素就像一塊塊積木一樣，組成了整個網頁架構，以下是單一一個元素：

![](https://i.imgur.com/x7X1TRF.png)

1. **Opening tag**：起始標籤，`<>`內放入標籤名稱。
2. **Closing tag**：結尾標籤，`<>`內放入和起始標籤一致的標籤名稱，而且要在名稱前加上/符號，和Opening tag形成一對。
3. **Content**：標籤內容。

### 屬性
加入屬性可以為元素提供更多資訊，ex：字型、顏色等等...。

![](https://i.imgur.com/9IBJo4j.png)

格式為: `"屬性名稱" = "屬性值"`

這邊的class屬性是將標籤分類(就想成放在同一個箱子裡)，之後爬蟲經常會用到，就先記起來吧!

## HTML架構
一個網頁的基本架構如下：

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>my first html</title>
  </head>
  <body>
    <p>Hello, HTML!</p>
  </body>
</html>
```

1. `<head>`：標頭，包含網頁的基本設置，不會顯示在畫面上，ex：網頁標題、字元編碼...。
2. `<body>`：主體，包含了所有會顯示於網頁瀏覽者眼前的內容，ex：文字、圖片...。

在瀏覽器上的顯示結果為：

![](https://i.imgur.com/W5JKock.jpg)

## DOM tree

看完剛才的HTML架構後，你可能會發現這有點像樹狀的結構，沒錯! 其實這個有點像樹狀的結構就被稱為DOM tree。

DOM全名為Document Object Model，中文是文件物件模型。實際上就是將所有HTML所有的元素(包括文字、圖片、容器)視作樹上的節點，最後結合成樹狀的結構，就像下圖這樣。

![](https://i.imgur.com/2ANvEQW.png)

通常有四種節點：

1. **Document**：所有HTML文件的起點，就像是樹的樹根。
2. **Element**：所有的元素，像是`<body>`、`<p>`都是。
3. **Text**：被元素所包起來的文字。
4. **Attribute**：元素所擁有的屬性，像是`class`、`style`等等。

節點底下包含的節點我們稱為該節點的**子節點**，而上一層的節點稱為該節點的**父節點**。

所以說上圖`<body>`的子節點是`<a>`和`<h1>`，而父節點是`<html>`。

## HTML基本元素

對架構有了解後，接下來介紹幾個經常用到的HTML元素，這些元素都是放在`<body>`中。

### `<h1>`~`<h6>`
標題，從標題一到標題六，文字從大到小，通常用於文章的主標題和副標題。

```html
<h1>This is heading1</h1>
<h2>This is heading2</h2>
<h3>This is heading3</h3>
<h4>This is heading4</h4>
<h5>This is heading5</h5>
<h6>This is heading6</h6>
```

顯示結果為：

![](https://i.imgur.com/EJDG4EP.jpg)

### `<p>`
段落，通常用於文字內容，優點在於文章超出邊界時會自動換行。

```html
<p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed id felis a lectus scelerisque bibendum. Donec
    mollis mollis rhoncus. Integer nec molestie lacus. In dapibus velit non augue pulvinar eleifend. Ut sit amet
    lobortis dui, ut facilisis elit. Quisque vulputate felis at arcu hendrerit eleifend. Donec elementum vel massa a
    fermentum. Vivamus eget cursus massa. Morbi elementum metus a eros euismod elementum. Nunc commodo felis urna,
    vel lacinia velit lobortis vel. Mauris efficitur augue nec aliquet consequat. Vestibulum sed convallis purus,
    vel tempor urna. Cras ornare ex est, eu malesuada diam suscipit nec.
</p>
```

顯示結果為：

![](https://i.imgur.com/wgVZaKm.jpg)

範例文字是使用很經典的[英文亂文產生器](https://www.lipsum.com/)產生出來的。

### `<br>`
換行，基本上就等同於 "\n"。

```
<p>
    Hi!<br>
    Hello<br>
    你好<br>
</p>
```

顯示結果為：

![](https://i.imgur.com/26e89a9.jpg)

這時你可能會覺得奇怪，前面不是說要一個起始標籤搭配一個結尾標籤嗎? 怎麼這裡只有一個標籤?

事實上，有些HTML標籤的確只有一個標籤而已，待會還會再看到更多例子。

### `<a>`
超連結，用於連結其他網址，href屬性加上連結網址。

```html
<a href="https://ithelp.ithome.com.tw/">IT邦幫忙首頁</a>
```

顯示結果為：

![](https://i.imgur.com/EgqLN4n.jpg)

點擊之後會傳到IT邦幫忙的首頁。

### `<div>`
區塊，或者說一個空的容器，可以在區塊中加入其他元素。

```html
<div style="background-color:blue; color:white; width:400px; height:200px;">
      <p>inside the div</p>
</div>
```

顯示結果為：

![](https://i.imgur.com/WCmv5Ew.jpg)

設定一個高200px、寬400px、背景藍色、文字白色的區塊。

### `<span>`
文字的區塊，包住文字並提供更多資訊。

```html
<p>this color is <span style="color: blue;">BLUE</span></p>
```

![](https://i.imgur.com/hxaS5iL.jpg)

只有將 "BLUE" 設為藍色，其他字依然是黑色。

### `<hr>`
分隔線，通常用於分隔區域。

```
<hr style="background-color:blue; height: 2px">
```

顯示結果為：

![](https://i.imgur.com/vhpyptM.jpg)

一條藍色寬度為2px的分隔線。

## 小結
今天的部分就到這邊，稍微總結一下今天學了什麼。首先從HTML的基本架構開始，知道了HTML是由各種元素所組成的，接著介紹了幾個常用的元素，像是標題、段落、超連結...等等。

明天我會再介紹更多的HTML元素，以及補充介紹VScode的實用套件，就讓我們拭目以待~~

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。