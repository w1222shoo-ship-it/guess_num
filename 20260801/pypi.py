import requests
import xml.etree.ElementTree as xmltree
from collections import deque
from datetime import datetime, date

url = 'https://pypi.org/rss/updates.xml'

result = requests.get(url)
element = xmltree.fromstring(result.text)   # 字串 → XML 樹

xmltree.dump(element)                       # 印出整棵樹看結構

list =deque([])

for item in element.findall('./channel/item'):
    for b in item:                          # title, link, description, pubDate...
        print(b.tag, b.text)
        if b.tag == 'pubDate' :
            date = datetime.strptime(b.text, '%a, %d %m %Y %H:%M:%S %z')
            print(date)
    print()                                 # 每筆之間空一行