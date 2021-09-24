import requests
from bs4 import BeautifulSoup

url = "https://kma.kkbox.com/charts/daily/newrelease?terr=tw&lang=tc"
response = requests.get(url)
root = BeautifulSoup(response.text, "html.parser")
print(root.prettify())
