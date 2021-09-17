# Day 08：Python基本介紹01 | 環境架設、Hello Python!

###### tags: `2021 IT鐵人賽`

到目前為止，我們已經學了網頁前端的HTML和CSS，但在開始爬蟲前還有一個很重要的東西要學，那就是Python。

因此接下來幾天我會開始介紹Python的基礎語法，那我們就開始吧!

## Python是什麼?

![](https://i.imgur.com/zy1QVH7.png)

> [Python](https://zh.wikipedia.org/wiki/Python)是一種廣泛使用的直譯式、進階和通用的程式語言。
> 
> Python的設計哲學強調程式碼的可讀性和簡潔的語法，尤其是使用空格縮排劃分程式碼塊。相比於C或Java，Python讓開發者能夠用更少的代碼表達想法。不管是小型還是大型程式，該語言都試圖讓程式的結構清晰明瞭。
> 
> -- 維基百科

看完還是霧煞煞嗎? 那我們來看這段影片：

<!-- {%youtube Y8Tko2YC5hA %} -->

> 因為GitHub不支援嵌入Youtube影片，因此連結我就放在底下了：
> https://www.youtube.com/watch?v=Y8Tko2YC5hA

以上影片大概說明了幾個Python的優點：

1. **簡潔的語法**：完成一樣的工作，Python的程式碼就是比其他程式語言少。
2. **直覺、好入門**：Python的語法比較貼近人類的語言，使得Python成為很適合程式新手入門的語言。
3. **非常多應用**：你可以使用Python統計資料、繪製圖表、開發應用程式...等等，以及我之後要教你的 - 網頁爬蟲。
4. **廣大的社群**：使用Python的人越來越多，也就意味著有更多的資源、套件可以使用，這大大提升了開發上的便利性。'

以上幾點就是為什麼大家那麼喜歡用Python，以及你現在為什麼要學Python的理由。

## 環境架設

首先需要建立Python的開發環境，用於管理所有下載的套件，我這邊使用Anaconda來建立開發環境。

### Anaconda

![](https://i.imgur.com/HAfrllk.png)

[Anaconda](https://zh.wikipedia.org/wiki/Anaconda_(Python%E5%8F%91%E8%A1%8C%E7%89%88))是 Python 及 R 語言的一個免費開源發行版本，主要用於資料科學(Data Science)、機器學習(Machine Learning)等領域，可對許多套件(Packages)進行管理，超過7,500個資料科學及機器學習套件提供查找及安裝，管理環境也相當容易，是目前全世界最受歡迎的 Python 資料科學平台，全球擁有超過2000萬用戶。

Anaconda3 目前有三種版本，分別是個人版(Individual Edition)、團隊版(Team Edition)及企業版(Enterprise Edition)，這裡使用免費的個人版就夠用了。

### 安裝教學

1. 首先到[Anaconda個人版](https://www.anaconda.com/products/individual)，滑到下方Anaconda Installers的地方，依照你的作業系統選擇下載的版本，範例是下載Windows 64bits的版本，點擊後會開始下載到你的電腦上(檔案稍大，需要等一會兒)。

![](https://i.imgur.com/epCN7FN.jpg)

2. 下載完後點開執行檔，按Next

![](https://i.imgur.com/8n8gcrm.jpg)

3. 問你同不同意授權，就像平常一樣沒仔細看就按Agree。

![](https://i.imgur.com/SwirYfV.jpg)

4. 詢問安裝對象，這邊照著建議選擇Just me就好。

![](https://i.imgur.com/mgkBQrK.jpg)

5. 選擇下載路徑，檔案大小有2.9GB，要注意自己硬碟的容量。

![](https://i.imgur.com/YOnajwR.jpg)

6. 除非有特殊需求，不然這些設定都不用改，完成後按Install。

![](https://i.imgur.com/Ym5tLPz.jpg)

7. 下載完後，就一直Next直到Finish。
8. 打開開始，應該會在最近新增看到Anaconda資料夾，裡面有一些載好的程式。

![](https://i.imgur.com/aAQfing.png)

9. 下載完成了!

### 套件管理

1. 打開Anaconda Prompt，打開是一個CLI介面。
 
![](https://i.imgur.com/LhcdSAV.jpg)

2. 打上指令`pip list`，顯示所有已經安裝的套件。

![](https://i.imgur.com/xL7ieMx.jpg)

3. 指令`pip install 模組名稱`，安裝模組和它的相關模組(安裝要一段時間)，已經下載過了也會告訴你，之後要安裝套件就是這樣安裝。

![](https://i.imgur.com/h8DEtLI.jpg)

### Python版本檢查

輸入指令`python -V`或`python --version`，如果出現版本號碼就是成功了!

![](https://i.imgur.com/v7EQVI4.jpg)

## Hello Python!

下載Anaconda的同時其實也下載了幾個內建的IDE(整合開發環境)和Editor(編輯器)，像是Spyder、Jupyter Notebook...等等

但我個人不太喜歡用Spyder，因為打開都要等好久@@。Jupyter Notebook雖然好用，但對新手來說也不太友善，所以我習慣還是使用VScode進行開發。當然你已經習慣了其他編輯器也OK，開發上不會差太多。

### VScode外掛

#### Python

[Python套件](https://marketplace.visualstudio.com/items?itemName=ms-python.python)提供Python語法自動補全和除錯。

在VScode側邊欄位Extensions的地方搜尋 "Python"，找到由Microsoft開發的套件後安裝下來。

![](https://i.imgur.com/BRdqlly.jpg)

#### Code Runner

[Code Runner套件](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)可以執行多種程式語言，包括Python。

在VScode側邊欄位Extensions的地方搜尋 "Code Runner"，找到後安裝下來。

![](https://i.imgur.com/9BuIlvX.jpg)

### Python直譯器 (Interperter)

因為Python是一種直譯式語言，所以接下來，我們要告訴VScode，我們要用哪個Python的直譯器執行。

1. 按`Ctrl+Shift+P`，然後搜尋 "Python: Select Interperter"

![](https://i.imgur.com/WjL8CIN.jpg)

2. 然後選擇你要的編譯器，因為我們是透過Anaconda下載Python，所以選擇 "("base": conda)" 這一個。

![](https://i.imgur.com/jC2TGD1.jpg)

3. 左下角如果有出現直譯器名稱，那就是完成啦!

![](https://i.imgur.com/7oDkyjQ.jpg)

### Hello

我們的第一個Python程式從印出 "Hello Python!" 開始!

1. 左方Explorer中，按下**Open Folder**，然後選擇任意一個你想放程式碼的資料夾。

![](https://i.imgur.com/wAhRKZw.jpg)

2. 打開後，按下**New File**按鈕，檔案名稱命名為`hello.py`。VScode會自動將副檔名為`.py`的檔案視為Python程式碼。

![](https://i.imgur.com/53I4zBJ.jpg)

3. 在中間編輯區域輸入以下程式，輸入完後按`Ctrl+S`存檔。

```
print("Hello Python!")
```

`print()`是Python的函數，功能是在terminal印出內容。

4. 存檔完後要執行程式碼，有兩種方法：

* 按`Ctrl+F5`
* 按`Ctrl+Alt+N`或點**右上角的三角形按鈕**。

![](https://i.imgur.com/O7nuPCb.jpg)

5. 執行後如果在下方區塊看到`Hello Python!`，恭喜你，你完成了你的第一個Python程式了!

![](https://i.imgur.com/nJIRiDp.jpg)


## 同場加映：我個人很推薦的幾個外掛

以下這些外掛都是改變VScode外觀的，不裝不會影響程式執行，但裝了會讓你的奇模子變好~

* [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer)：將括號用顏色區分，更好辨識括號。
* [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)：讓側邊導航欄的檔案顯示比較好看的圖示。
* [One Dark Pro](https://marketplace.visualstudio.com/items?itemName=zhuangtongfa.Material-theme)：改變VScode的顏色風格，黑色風格不但省電也比較不傷眼。

## 小結

今天我們介紹Python這個最熱門、最潮的程式語言，告訴你為什麼要學Python後，帶領你安裝Python的開發環境 - Anaconda以及最後在VScode上使用Python印出Hello Python!

接下來幾天，我會開始從Python的基本語法教起，請大家拭目以待，我們明天準時再會~

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。