import requests
from bs4 import BeautifulSoup


kakao = requests.get("https://tech.kakao.com/blog/")
kakao_soup = BeautifulSoup.find_all("div", {"class": "tit_post"})


for t in kakao_soup:
    title = t.find("a")
    date = t.find("span", {"class": "txt_date"})
    pre_text = t.find("p", {"class": "desc_post"})

    print(title)
    print(link)
    print(date)
    print(pre_text)