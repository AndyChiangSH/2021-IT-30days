import requests
from bs4 import BeautifulSoup
import json
import time

# KKBOX華語新歌日榜
url = "https://kma.kkbox.com/charts/api/v1/daily?category=297&lang=tc&limit=50&terr=tw&type=newrelease"

# 取得歌曲資訊json檔
response = requests.get(url)
# print(response.status_code)
# print(response.text)

# 將json字串轉為Python的字典型態
data = json.loads(response.text)
song_list = data["data"]["charts"]["newrelease"]
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
    print("連結:", song_url)
    print("作者:", song_artist)
    print("發行日期:", song_date)

    # 從歌曲連結取得歌詞
    song_response = requests.get(song_url)
    soup = BeautifulSoup(song_response.text, "html.parser")
    lyric = soup.find("div", class_="lyrics").text
    print("歌詞:", lyric)

    print("-" * 30)

print("END of program!")
