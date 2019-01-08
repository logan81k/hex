import json
from datetime import datetime, timedelta
from time import sleep

import requests

with open('./upbit_listed_tokens.txt', 'r') as f:
    line = f.readlines()
upbit_listed_tokens = [x.strip() for x in line]

start = "20181202"  # 2018년 12월 1일 부터 -> 20181202
end = "20190101"  # 2018년 12월 31일 까지 -> 20190101

start_date = datetime.strptime(start, '%Y%m%d')
end_date = datetime.strptime(end, '%Y%m%d')
delta = end_date - start_date

with open('./upbit_listed_tokens_price.txt', 'a') as f:
    f.truncate(0)

    for token in upbit_listed_tokens:
        for d in range(delta.days + 1):
            closing_day = (start_date + timedelta(d) - timedelta(days=1))
            day = str((start_date + timedelta(d)).date())
            url = "https://api.upbit.com/v1/candles/days"
            querystring = {"market": f"KRW-{token}", "to": f"{day}T00:00:00+09:00"}
            response = requests.request("GET", url, params=querystring)
            json_response = json.loads(response.text)
            print(f"{closing_day.date()},{token},{json_response[0]['trade_price']}")
            f.write(f"{closing_day.date()},{token},{json_response[0]['trade_price']}\n")
            sleep(1)
        f.flush()
