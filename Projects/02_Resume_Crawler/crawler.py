from bs4 import BeautifulSoup

# 讀檔
response = ""
with open("main.html", "r", encoding="utf8") as file:
    response = file.read()

# BeautifulSoup解析原始碼
soup = BeautifulSoup(response, "html.parser")

# 找到姓名
# name = soup.find("h1")
# print(name)

# # 找到所有分類標題
# titles = soup.find_all("h2")
# print(titles)
# for title in titles:
#     print(title)

# # 找到所有分類標題和英文標題
# titles = soup.find_all(["h2", "h3"], limit=5)
# for title in titles:
#     print(title)

# # class定位
# name = soup.find("div", class_="name")
# print(name)

# # id定位
# avatar = soup.find("div", id="avatar")
# print(avatar)

# # select_one
# name = soup.select_one("div.name h1")
# print(name)

# # select
# titles = soup.select("h2")
# for title in titles:
#     print(title)

# 尋找parent和sibling
# skill = soup.find("li", id="this")
# print(skill)
# print(skill.find_previous_sibling("li"))
# print(skill.find_next_sibling("li"))
# print(skill.find_parent())

# 取得文字
name = soup.find("h1")
print(name.getText())
print(name.text)
print(name.string)

# 找到Email、電話等資訊
# infos = soup.find("div", class_="info").find_all("li")
# for info in infos:
#     print(info.text.strip())

# # 取得屬性值
img = soup.find("div", id="avatar").img
print(img["src"])
