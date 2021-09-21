import time
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

# 進入聯合新聞網專頁
driver.get("https://www.facebook.com/crazyck101")

time.sleep(5)

# 往下滑3次，讓Facebook載入文章內容
for x in range(3):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("scroll")
    time.sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")

# 定位文章標題
titles = soup.find_all(
    "div", class_="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q")
for title in titles:
    # 定位每一行標題
    posts = title.find_all("div", dir="auto")
    # 如果有文章標題才印出
    if len(posts):
        for post in posts:
            print(post.text)

    print("-" * 30)

# 等待10秒
time.sleep(10)
# 關閉瀏覽器
driver.quit()
