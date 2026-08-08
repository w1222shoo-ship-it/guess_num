import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.python.org'

def getnews(url):
    page = requests.get(url).text
    doc = soup(page, 'html.parser')

    items = doc.find_all('div', {'class': 'shrubbery'})   # 所有區塊
    for item in items:
        if 'Latest News' in item.h2.text:                 # 只要「最新消息」那一塊
            ys = item.find_all('li')
            for y in ys:
                print(list(y))
                date  = y.time['datetime']    # <time> 的 datetime 屬性
                link  = y.a['href']           # <a> 的網址
                title = y.a.string            # <a> 的文字
                print(date, title, link)

getnews(url)