# Day 06：專案01 - 超簡單個人履歷05 | CSS版面佈局、Flex

###### tags: `2021 IT鐵人賽`

昨天講完的CSS的文字和區塊屬性後，今天要接續介紹版面佈局的屬性，以及一個非常好用的佈局容器 - Flex，上完這堂課，你的網頁佈局就可以更加彈性囉~ 那麼，我們廢話不多說，就開始今天的介紹吧!

## CSS版面佈局

首先，你按**F12**打開開發人員工具，應該會在 **Elements >> Styles** 滑到最底下看到這個畫面(Chrome一定有，其他瀏覽器不確定)：

![](https://i.imgur.com/ED5MMEU.png)

記好這個圖，因為他就是CSS版面佈局的概念圖。

我們看這個圖，發現他像箭靶一樣一圈圈的包圍起來，主要有三層，**從外到內分別是margin、border和padding**。border我們昨天已經說過了，所以接下來我只著重在介紹margin和padding這兩個屬性該如何使用。

### margin

margin，又稱外距。顧名思義就是元素外側到其他元素或邊界的距離，通常用於在兩個元素間留下空間，畢竟東西都緊貼在一起也不好看對吧?

我們就用以下例子認識margin：

HTML(都同一個，之後例子我就不放了)：
```html
<div class="outside">
    <div class="inside"></div>
</div>
```

CSS：
```css
.outside {
    width: 200px;
    height: 200px;
    background-color:rgb(138, 138, 138);
    margin: 50px;
}
.inside {
    width: 100px;
    height: 100px;
    background-color:rgb(92, 92, 92);
}
```

顯示結果為：

![](https://i.imgur.com/DdPNF4w.png)

我們按F12打開開發者工具，點上方的紅框的圖示，接著將游標移動到淺灰色的方塊上，就會顯示如同上方的畫面。

我們可以看到橘色的部分代表margin，往淺灰色的方塊上下左右推了50px的空間。

![](https://i.imgur.com/ztmVGqT.jpg)

另外，margin的簡易寫法為：

```css
margin: 上 / 右 / 下 / 左
或 margin: 上下 / 右左
```

順便分享個有趣的小訣竅，**將左右margin都設為auto時，區塊就會自動水平置中哦!**

```css
margin: 0px auto
```

![](https://i.imgur.com/XclDdgO.png)


### padding

padding，又稱內距。和margin很像，不同點在於padding是向元素內側預留空間。通常用於避免內部元素太過貼近外側邊界。

CSS：
```css
.outside {
    width: 200px;
    height: 200px;
    background-color:rgb(138, 138, 138);
    padding: 10px;
}
.inside {
    width: 100px;
    height: 100px;
    background-color:rgb(92, 92, 92);
}
```

顯示結果為：

![](https://i.imgur.com/JwLXoGw.png)

綠色的部分就是padding，淺灰色從邊界向內推了10px。

padding的簡易寫法跟margin一樣，就不多說了。

### margin & padding

margin和padding是不會互相吃掉的，是什麼意思呢? 比方說我下面的例子，外容器向內推20px，內容器向外推20px，所以內外容器就隔了40px。

![](https://i.imgur.com/AYKkMZN.png)

![](https://i.imgur.com/lUHWsYH.png)

但是margin和margin就不同了，下面例子有兩個容器，上容器往下推20px，下容器往上推20px，照理來說要隔40px才對吧? 但事實上不是，上下的margin被互相吃掉了，所以實際上只隔20px而已，這點要特別小心。

![](https://i.imgur.com/QM8kfSd.png)

![](https://i.imgur.com/P8VqXoB.png)

總之，margin和padding切記不要隨意亂套一大堆，很容易導致版型整個跑掉，所以加入margin或padding前要很清楚自己要幹什麼再去做。

## CSS Flex

Flex是CSS相當方便的一個佈局容器，雖然是一個比較新的技術，但大部分的瀏覽器都可以相容，請安心使用^^

### Flex外容器和內元件

首先我們稱外層的容器叫外容器，容器內的元件叫內元件，像像面的圖。

![](https://i.imgur.com/5f2AZok.jpg)

在外容器加上 `display: flex;`，就成為Flex容器囉!

接著介紹幾個外容器常見的屬性：

### flex-direction

預設的軸線方向。

![](https://i.imgur.com/SR0sVtz.jpg)

設定主軸的方向，共有四個屬性值：row、row-reverse、column、column-reverse。

![](https://i.imgur.com/bu86who.jpg)

![](https://i.imgur.com/3Xd0697.jpg)

### flex-wrap

超出邊界時是否要換行，屬性值有wrap(換行)和nowrap(不換行)。

![](https://i.imgur.com/yb9bHei.jpg)

### justify-content

設定主軸對齊方式。

![](https://i.imgur.com/CpSakpY.jpg)

### align-items

和`justify-content`不同，用來設定交錯軸對齊方式。

![](https://i.imgur.com/A1Ca7nr.jpg)

其實還有其他的屬性沒有講，但這部分上網查就有了。

想了解更多可以參考這兩篇文章：

* [圖解：CSS Flex 屬性一點也不難](https://wcc723.github.io/css/2017/07/21/css-flex/)
* [MDN-CSS彈性盒子用法](https://developer.mozilla.org/zh-TW/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)

### 實用小工具

這裡偷偷告訴你一個[好用的小工具](https://codepen.io/peiqun/pen/WYzzYX)，改變左邊欄位的屬性值，觀察看看有什麼變化吧!

另外，瀏覽器按F12打開開發人員介面，`display: flex;`後方會有一個圖案，點下去之後有好幾個屬性選項，就可以在瀏覽器上預覽Flex的效果了(原始碼不會改變)，在開發時候非常好用!

![](https://i.imgur.com/cHZh7Px.jpg)

## 小結

今天我們整理了CSS幾個實用的排版技巧，首先是margin和padding，以及後來的Flex容器，用圖形的方式希望有讓你比較好理解。

CSS就在這邊告一段落，接著我會實際說明個人履歷的程式碼，明天你就會做出專屬於你的個人履歷囉，千萬不要錯過!

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。