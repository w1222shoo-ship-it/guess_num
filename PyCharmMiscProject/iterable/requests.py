import requests

url = 'https://www.python.org'
data = requests.get(url)

print(data.encoding)     # utf-8
print(data.status_code)  # 200
print(data.headers)
print(data.text)         # 已經是字串，不用 decode