# PTT八卦版爬蟲

from bs4 import BeautifulSoup
import requests
import json

# 基本參數
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
payload = {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}
data = []   # 全部文章的資料
num = 0

# 用session紀錄此次使用的cookie
rs = requests.session()
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)

# 爬取兩頁
for i in range(2):
    # get取得頁面的HTML
    # print(url)
    response = rs.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    # 找出每篇文章的連結
    links = soup.find_all("div", class_="title")
    for link in links:
        # 如果文章已被刪除，連結為None
        if link.a != None:

            article_data = {}   # 單篇文章的資料
            page_url = "https://www.ptt.cc/"+link.a["href"]

            # 進入文章頁面
            response = rs.get(page_url)
            result = BeautifulSoup(response.text, "html.parser")
            # print(soup.prettify())

            # 找出作者、標題、時間、留言
            main_content = result.find("div", id="main-content")
            article_info = main_content.find_all(
                "span", class_="article-meta-value")

            if len(article_info) != 0:
                author = article_info[0].string  # 作者
                title = article_info[2].string  # 標題
                time = article_info[3].string   # 時間
            else:
                author = "無"  # 作者
                title = "無"  # 標題
                time = "無"   # 時間

            # print(author)
            # print(title)
            # print(time)

            article_data["author"] = author
            article_data["title"] = title
            article_data["time"] = time

            # 將整段文字內容抓出來
            all_text = main_content.text
            # 以--切割，抓最後一個--前的所有內容
            pre_texts = all_text.split("--")[:-1]
            # 將前面的所有內容合併成一個
            one_text = "--".join(pre_texts)
            # 以\n切割，第一行標題不要
            texts = one_text.split("\n")[1:]
            # 將每一行合併
            content = "\n".join(texts)

            # print(content)
            article_data["content"] = content

            # 一種留言一個列表
            comment_dic = {}
            push_dic = []
            arrow_dic = []
            shu_dic = []

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

                # print(push_tag, push_userid, push_content, push_time)

                dict1 = {"push_userid": push_userid,
                         "push_content": push_content, "push_time": push_time}
                if push_tag == "推 ":
                    push_dic.append(dict1)
                if push_tag == "→ ":
                    arrow_dic.append(dict1)
                if push_tag == "噓 ":
                    shu_dic.append(dict1)

            # print(push_dic)
            # print(arrow_dic)
            # print(shu_dic)
            # print("--------")

            comment_dic["推"] = push_dic
            comment_dic["→"] = arrow_dic
            comment_dic["噓"] = shu_dic
            article_data["comment"] = comment_dic

            # print(article_data)
            data.append(article_data)
            num += 1
            print("第 "+str(num)+" 篇文章完成!")

    # 找到上頁的網址，並更新url
    url = "https://www.ptt.cc/"+soup.find("a", string="‹ 上頁")["href"]

# print(data)
# 輸出JSON檔案
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)
