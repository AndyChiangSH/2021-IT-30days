import requests
from bs4 import BeautifulSoup

my_headers = {"cookie": "over18=1"}  # cookie設定

response = requests.get(
    "https://www.ptt.cc/bbs/Gossiping/index.html", headers=my_headers)  # 放在headers欄位中傳送
root = BeautifulSoup(response.text, "html.parser")  # 解析原始碼

links = root.find_all("div", class_="title")    # 文章標題
for link in links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白
