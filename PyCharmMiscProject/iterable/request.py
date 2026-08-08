import urllib.request as ur

url = 'https://www.python.org'
resp = ur.urlopen(url)

print(resp.geturl())        # 網址
print(resp.status)          # 200 表示成功
print(resp.getheaders())    # 表頭

data = resp.read()
print(data)                 # b'<!doctype html>...'  ← 前面有個 b
print(data.decode('utf-8')) # 轉成字串才看得懂