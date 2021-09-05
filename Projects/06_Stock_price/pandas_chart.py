import pandas as pd
import matplotlib.pyplot as plt

# 讀取csv
df = pd.read_csv("./month_stock.csv", encoding="big5")
# print(df)

# 篩選我們要的資料
chart_df = df[["日期", "最高價", "最低價", "收盤價"]]
# 將日期設為x軸
chart_df.set_index("日期", inplace=True)
print(chart_df)

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

# 繪圖
chart = chart_df.plot(xlabel="日期", ylabel="價格", title="110年8月股市趨勢圖", legend=True)
plt.grid()

# 存成圖片(一定要放前面!)
plt.savefig("pandas_chart.png")
# 顯示圖片
plt.show()
