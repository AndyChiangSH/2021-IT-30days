import pandas as pd
import matplotlib.pyplot as plt

# 讀取csv
df = pd.read_csv("./month_stock.csv", encoding="big5")
# print(df)

# 篩選我們要的資料
date = df["日期"]
high_price = df["最高價"]
low_price = df["最低價"]
end_price = df["收盤價"]

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

# 繪圖
plt.plot(date, high_price, color="#ff2121")
plt.plot(date, low_price, color="#00bd42", linewidth=5)
plt.plot(date, end_price, color="#005de0", linestyle="dashed")
plt.xlabel("日期")
plt.ylabel("價格")
plt.legend(["最高價", "最低價", "收盤價"], loc="lower right")
plt.title("110年8月股市趨勢圖")
plt.grid(True)

# 存成圖片(一定要放前面!)
plt.savefig("matplotlib_chart.png")
# 顯示圖片
plt.show()
