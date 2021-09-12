import requests

response = requests.get("https://www.ptt.cc/bbs/C_Chat/index.html")
print(response.text)
print(response.status_code)