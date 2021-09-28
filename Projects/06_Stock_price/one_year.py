import requests
import json
import pandas as pd

year_df = pd.DataFrame()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

# 從1到12月
for m in range(1, 13):
    url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2020{0:02d}01&stockNo=0050".format(m)
    print(url)

    # 取得股票資料json字串
    response = requests.get(url, headers=headers)
    # print(response.text)

    # 從json字串轉為python的字典格式
    json_data = json.loads(response.text)
    datas = json_data["data"]
    fields = json_data["fields"]

    # 存成Pandas的Dataframe
    month_df = pd.DataFrame(datas, columns=fields)
    # print(month_df)

    # 合併於整年的Dataframe
    year_df = year_df.append(month_df, ignore_index=True)

print(year_df)
# 轉成csv檔
year_df.to_csv("./year_stock.csv", encoding="big5")
