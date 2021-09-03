import pandas as pd

# 讀取csv
df1 = pd.read_csv("./month_stock.csv", encoding="big5")
print(df1)

# 讀取excel
df2 = pd.read_excel("./month_stock.xlsx")
print(df2)

# 讀取html
df3 = pd.read_html("./month_stock.html", encoding="utf8")
print(df3)