import requests
from bs4 import BeautifulSoup


url = "https://tech.kakao.com/blog/"
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, "html.parser")
links = soup.select("div.wrap_post > ul > li > a.link_post")


for link in links:
    print(link.text)
    print(link.get("href"))
