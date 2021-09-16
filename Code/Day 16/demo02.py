import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://www.ptt.cc/bbs/Gossiping/index.html")  # 改成八卦板的網址
root = BeautifulSoup(response.text, "html.parser")  # 解析原始碼
print(root.prettify())
