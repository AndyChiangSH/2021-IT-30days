# Day 19：專案03 - PTT 八卦版爬蟲04 | 留言、換頁、json

###### tags: `2021 IT鐵人賽`

各位早阿，今天就接續昨天的部分，繼續抓取留言和匯出成json檔吧!

## 留言區

觀察一下PTT的留言區，可以看到留言分成三種，分別是"推"、"噓"和"→"，每則留言都有標籤、作者、內容和時間這些資訊，接下來就是要取得這些資訊並依照標籤分類。

![](https://i.imgur.com/qG1ONYZ.jpg)

隨便對一則留言**右鍵>>檢查**，發現留言是在`class="push"`的`<div>`內，資訊則分別在`class="push-tag"、"push-userid"、"push-content"、"push-ipdatetime"`中。

因此程式碼就很單純：

```python
# 抓出所有留言
comments = main_content.find_all("div", class_="push")
for comment in comments:
    push_tag = comment.find(
        "span", class_="push-tag").string   # 分類標籤
    push_userid = comment.find(
        "span", class_="push-userid").string  # 使用者ID
    push_content = comment.find(
        "span", class_="push-content").string   # 留言內容
    push_time = comment.find(
        "span", class_="push-ipdatetime").string   # 留言時間
```

為了分類，我建立三個list，分別存放"推"、"→"、"噓"三種標籤。

```python=
push_dic = []
arrow_dic = []
shu_dic = []
```

再來就用字典型式將所有資料塞好塞滿，然後再依照標籤分類就好囉~

```python=
dict1 = {"push_userid": push_userid, "push_content": push_content, "push_time": push_time}
if push_tag == "推 ":
    push_dic.append(dict1)
if push_tag == "→ ":
    arrow_dic.append(dict1)
if push_tag == "噓 ":
    shu_dic.append(dict1)
```


## 自動換頁

現在雖然可以抓下文章清單中的資料了，但只有第一頁的文章而已，要怎麼樣才能抓其他頁的文章呢??

想一下，我們想要看上一頁時，會做什麼事?
廢話! 當然就是按 "上頁" 按鈕阿!

對上方導覽列的 "上頁" 按鈕**右鍵>>檢查**，上一頁的連結就在`string="‹ 上頁"`的`<a>`中。

![](https://i.imgur.com/5cyNOug.png)

更新url變數，然後用for迴圈想抓幾頁就抓幾頁!

```python
url = "https://www.ptt.cc/"+soup.find("a", string="‹ 上頁")["href"]
```

## json

目前都只是將抓到的資料印在terminal上，如果之後要用到這些資料做後續分析的話，就很不方便了，所以我們要將資料轉成json格式並存在電腦中。

json畢竟是第一次提到，還是來介紹一下什麼是json。

> JSON（JavaScript Object Notation）是由道格拉斯·克羅克福特構想和設計的一種輕量級資料交換格式。其內容由屬性和值所組成，因此也有易於閱讀和處理的優勢。
> JSON是獨立於程式語言的資料格式，其不僅是JavaScript的子集，也採用了C語言家族的習慣用法，目前也有許多程式語言都能夠將其解析和字串化，其廣泛使用的程度也使其成為通用的資料格式。
> 
> -- [維基百科](https://zh.wikipedia.org/wiki/JSON)

![](https://i.imgur.com/nBJIfcb.png)

另外，python和json格式上有很高的對應關係。底下是兩者各自對應到的物件。

![](https://i.imgur.com/TBjpKm9.png)

所以，我們要做的前置作業就是把資料整理好，以利將其轉成json檔。剛才也看到了python和json格式上的對應關係，這裡只要將資料整理成由list和dictionary所組成的複合型態就好了。

json資料的架構：

![](https://i.imgur.com/UcDkXSq.png)

程式碼：

```python
data = []   # 全部文章的資料
article_data = {}   # 單篇文章的資料
comment_dic = {}   # 所有留言

article_data["author"] = author
article_data["title"] = title
article_data["time"] = time
article_data["content"] = content
comment_dic["推"] = push_dic
comment_dic["→"] = arrow_dic
comment_dic["噓"] = shu_dic
article_data["comment"] = comment_dic

data.append(article_data)
```

更佛心的是，Python內建有json套件，利用`dump()`這個函數就能將其轉成json格式並匯出囉！

```python=
# 輸出JSON檔案
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file)
```

執行後，在同個目錄下就會出現`data.json`這個檔案，用記事本打開後如果有東西那就是成功了。

不過看到的應該是一大串編碼，沒辦法知道資料是不是對的，這邊偷偷告訴你一個好康的，到 [json editor](https://jsoneditoronline.org/) 這個網站，幫你將json資料轉為樹狀顯示，就可以很方便的確認資料是否正確~

![](https://i.imgur.com/hc5Dv4z.png)

點 "Open from disk" 就可以匯入剛才的json檔囉。

![](https://i.imgur.com/CrwQU3b.jpg)


[完整程式碼](https://github.com/AndyChiangSH/2021-IT-30days/blob/main/Projects/03_PTT_Gossiping/crawler.py)請到GitHub上面看~ (不想貼出來佔空間了)

## 小結

PTT八卦板爬蟲就教到這邊，希望大家看完後對爬蟲都已經有一些基礎的認知了，明天起就會搭配專題介紹**比較進階的爬蟲技巧**，讓你體會到爬蟲真正的強大之處，我認為應該是比較有趣的部分，大家敬請期待~

---

如果喜歡這系列文章麻煩幫我按Like加訂閱，你的支持是我創作最大的動力~

本系列文章以及範例程式碼都同步更新在[GitHub](https://github.com/AndyChiangSH/2021-IT-30days)上，後續會持續的更新，如果喜歡也麻煩幫我按個星星吧~

有任何問題或建議，都歡迎在底下留言區提出，還請大家多多指教。
