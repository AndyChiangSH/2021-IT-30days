import csv
import json
import time
import requests
from bs4 import BeautifulSoup

# KKBOX華語新歌日榜
url = "https://kma.kkbox.com/charts/api/v1/daily?category=390&lang=tc&limit=50&terr=tw&type=newrelease"

# 取得歌曲資訊json檔
response = requests.get(url)
# print(response.status_code)
# print(response.text)

# 將json字串轉為Python的字典型態
data = json.loads(response.text)
song_list = data["data"]["charts"]["newrelease"]
with open('songs.csv', 'w', newline='', encoding="big5") as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)
    # 寫入一列資料
    writer.writerow(["排名", "歌名", "作者", "發行日期", "連結"])
    # 取得每首歌的排名、曲名、連結、作者、時間
    for song in song_list:
        song_rank = song["rankings"]["this_period"]
        song_name = song["song_name"]
        song_url = song["song_url"]
        song_artist = song["artist_name"]
        song_timestamp = int(song["release_date"])
        # 從timestamp轉為日期格式
        song_date = time.strftime(
            "%Y-%m-%d", time.localtime(song_timestamp))

        print("排名:", song_rank)
        print("歌名:", song_name)
        print("作者:", song_artist)
        print("發行日期:", song_date)
        print("連結:", song_url)

        writer.writerow(
            [song_rank, song_name, song_artist, song_date, song_url])

        # # 從歌曲連結取得歌詞
        # song_response = requests.get(song_url)
        # soup = BeautifulSoup(song_response.text, "html.parser")
        # lyric = soup.find("div", class_="lyrics").text
        # print("歌詞:", lyric)

        print("-" * 30)

print("END of program!")
