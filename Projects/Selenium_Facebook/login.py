from selenium import webdriver
import time

# 你的資訊
url = "https://www.facebook.com/"
email = "andy10801@gmail.com"
password = "andygood"

# 防止跳出通知
chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.notifications": 2
}
chrome_options.add_experimental_option("prefs", prefs)

# 開啟下載的chromedriver
driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)

# 最大化視窗
driver.maximize_window()
# 進入Facebook登入畫面
driver.get(url)

# 填入帳號密碼，並送出
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_name("login").click()

# 登入後等待10秒
time.sleep(10)
# 關閉瀏覽器
driver.quit()
