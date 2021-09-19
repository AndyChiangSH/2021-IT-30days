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

root = BeautifulSoup(response.text, "html.parser")
links = root.find_all("div", class_="title")    # 文章標題
for link in links:
    page_url = "https://www.ptt.cc"+link.a["href"]
    print(page_url)

    response = rs.get(page_url)
    result = BeautifulSoup(response.text, "html.parser")
