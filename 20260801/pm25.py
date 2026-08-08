import requests
import json

url = 'https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=4c89a32a-a214-461b-bf29-30ff32a61a8a&limit=1000&sort=datacreationdate desc&format=JSON'

result = requests.get(url, verify=False)   # verify=False 忽略 https 憑證檢查
data = json.loads(result.text)             # JSON → Python 串列

for item in data:
    print(item['county'], item['site'],item['pm25'],item['itemunit'], item['datacreationdate'])