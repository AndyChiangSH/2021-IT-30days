from bs4 import BeautifulSoup

# 讀檔
response = ""
with open("crawl_me.html", "r", encoding="utf8") as file:
    response = file.read()

# BeautifulSoup解析原始碼
soup = BeautifulSoup(response, "html.parser")
# print(soup.prettify())

# find h1
# h1 = soup.find("h1")
# print(h1)

# # find by class
# container = soup.find("div", class_="container")
# print(container)

# # find by id
# this = soup.find("h2", id="this")
# print(this)

# find_all h2
# h2s = soup.find_all("h2")
# print(h2s)
# print(h2s[1])   # 使用索引值

# # find_all h1 and h2
# h1_h2s = soup.find_all(["h1", "h2"], limit=3)
# print(h1_h2s)
# print(len(h1_h2s))


# # select_one
# h1 = soup.select_one("h1")
# print(h1)

# select
# h2s = soup.select("h2")
# print(h2s)
# print(h2s[1])

# # select by class
# p = soup.select_one("div.container")
# print(p)

# # select by id
# this = soup.select_one("h2#this")
# print(this)

# 尋找parent和sibling
# this = soup.find("h2", id="this")
# print(this)
# print(this.find_previous_sibling())
# print(this.find_next_sibling())
# print(this.find_parent())

# # 取得文字
# h1 = soup.find("h1")
# print(h1.getText())
# print(h1.text)
# print(h1.string)

# # 取得屬性值
# img = soup.find("img")
# print(img["src"])
# print(img.get("src"))
