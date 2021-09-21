from selenium import webdriver
import time

# 開啟下載的chromedriver
driver = webdriver.Chrome("./chromedriver")

# 等待10秒
time.sleep(10)
# 關閉瀏覽器
driver.quit()
