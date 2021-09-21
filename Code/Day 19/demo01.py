import requests
from bs4 import BeautifulSoup

# post要傳的資料
payload = {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}

# 用session紀錄此次使用的cookie
rs = requests.session()
# post傳遞資料
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)
# 再get一次PTT八卦板首頁
response = rs.get("https://www.ptt.cc/bbs/Gossiping/index.html")
print(response.status_code)

# 進入文章頁面
response = rs.get("https://www.ptt.cc/bbs/Gossiping/M.1631951246.A.BB8.html")
result = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

# 找出作者、標題、時間、留言
main_content = result.find("div", id="main-content")

# 將整段文字內容抓出來
all_text = main_content.text
# 以--切割，抓最後一個--前的所有內容
pre_texts = all_text.split("--")[:-1]
# 將前面的所有內容合併成一個
one_text = "--".join(pre_texts)
# print(one_text)

# 以\n切割，第一行標題不要
texts = one_text.split("\n")[1:]
# 將每一行合併
content = "\n".join(texts)
print(content)
