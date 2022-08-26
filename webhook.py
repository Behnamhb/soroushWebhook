import json
import requests


headers = {'Content-Type':'application/json',
        'Accept':'application/json'}


message = {'to':'{YOUR_CHANNEL_TOKEN}','type':'TEXT','body':'HI from behnam','majorType':'CHANNEL'}
message = json.dumps(message)
resp = requests.post('https://bot.splus.ir/{YOUR_BOT_TOKEN}/sendMessage',data=message,headers=headers)
print(resp)
print(resp.text)
