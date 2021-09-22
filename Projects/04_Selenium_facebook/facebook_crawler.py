import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# 你的資訊
url = "https://www.facebook.com/"
email = "YOUR EMAIL"
password = "YOUR PASSWORD"

# 防止跳出通知
chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.notifications": 2
}
chrome_options.add_experimental_option("prefs", prefs)

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options)

# 最大化視窗
driver.maximize_window()
# 進入Facebook登入畫面
driver.get(url)

# 填入帳號密碼，並送出
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_name("login").click()

time.sleep(5)

# 進入木棉花專頁
driver.get("https://www.facebook.com/emuse.com.tw")

time.sleep(5)

# 往下滑3次，讓Facebook載入文章內容
for x in range(3):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("scroll")
    time.sleep(5)

root = BeautifulSoup(driver.page_source, "html.parser")

# 定位文章標題
titles = root.find_all(
    "div", class_="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q")
for title in titles:
    # 定位每一行標題
    posts = title.find_all("div", dir="auto")
    # 如果有文章標題才印出
    if len(posts) != 0:
        for post in posts:
            print(post.text)

    print("-" * 30)

# 建立資料夾
if not os.path.exists("images"):
    os.mkdir("images")

# 下載圖片
images = root.find_all(
    "img", class_=["i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm bixrwtb6", "i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm"])
if len(images) != 0:
    for index, image in enumerate(images):
        img = requests.get(image["src"])
        with open(f"images/img{index+1}.jpg", "wb") as file:
            file.write(img.content)
        print(f"第 {index+1} 張圖片下載完成!")

# 等待5秒
time.sleep(5)
# 關閉瀏覽器
driver.quit()
