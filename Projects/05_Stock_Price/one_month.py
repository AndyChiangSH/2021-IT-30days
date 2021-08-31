import requests
import json
import pandas as pd

# 台灣證券交易所，個股日成交資訊
url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20210801&stockNo=0050"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

# 取得股票資料json字串
response = requests.get(url, headers=headers)
# print(response.text)

# 從json字串轉為python的字典格式
json_data = json.loads(response.text)
datas = json_data["data"]
fields = json_data["fields"]

# 存成Pandas的Dataframe
df = pd.DataFrame(datas, columns=fields)
print(df)

# 轉成csv檔
df.to_csv("./month_stock.csv", encoding="big5")
# 轉成xlsx檔
df.to_excel("./month_stock.xlsx", encoding="big5")
# 轉成html檔
df.to_html("./month_stock.html")