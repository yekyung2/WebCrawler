import requests
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


url = "https://tech.kakao.com/blog/"
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, "html.parser")
links = soup.select("div.wrap_post > ul > li > a.link_post")

data = {}

for link in links:
    print(link.text)
    print(link.get("href"))

with open(os.path.join(BASE_DIR, "result.json"), "w+") as json_file:
    json.dump(data, json_file)
