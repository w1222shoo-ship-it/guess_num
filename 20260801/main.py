import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.python.org'

def is_http(link):
    """判斷是不是 http/https 開頭的完整網址"""
    return link is not None and link.startswith('http')

def links(url):
    page = requests.get(url).text
    htm = soup(page, 'html.parser')
    alinks = [item.get('href') for item in htm.find_all('a')]  # 抓出所有 href
    return [x for x in alinks if is_http(x)]                   # 只留完整網址

print('找出網址為 ' + url + ' 的 http 與 https 開頭的超連結')
for link in links(url):
    print(link)