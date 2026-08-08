from bs4 import BeautifulSoup as soup

from bs4 import BeautifulSoup as soup

fin = open('test.html', 'r', encoding='utf-8')
s = fin.read()
htm = soup(s, 'html.parser')

print(htm.title.prettify())      # 排版後的 <title> 區塊
print(htm.title.contents)        # ['網頁標題']
print(htm.title.contents[0])     # 網頁標題
print(htm.title.name)            # title
print(htm.title.string)          # 網頁標題

print(htm.meta)                  # 第一個 <meta> 標籤
print(htm.meta['content'])       # 它的 content 屬性值

# 找出所有 <td>
for item in htm.find_all('td'):
    print(item)

# 只找 class 為 table_head 的 <td>
for item in htm.find_all('td', {'class': 'table_head'}):
    print(item)

# 找 class 為 table_siteurl 的 <td>，取出裡面 <a> 的網址
for item in htm.find_all('td', {'class': 'table_siteurl'}):
    print(item.a['href'])

fin.close()