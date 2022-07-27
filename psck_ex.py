import requests
import json

#####

payload = {"type": 0, "sort": "add_time", "p": 7, "ps": 40}
payloadHeader = {
    'Host': 'www.psck.net',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}
url = "https://www.psck.net/api/?con=api&act=diskList&lang=null"
r = requests.post(url, data=payload, headers=payloadHeader).json()
s = r['data']['list']
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(s, f, ensure_ascii=False)
