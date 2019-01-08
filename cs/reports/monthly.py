from datetime import datetime, timedelta
from time import sleep

import requests
from bs4 import BeautifulSoup

with open('./listed_token_mapping.txt', 'r') as f:
    mapping = f.read()
listed_token_mapping = eval(mapping)

headers = ['Date', 'Rate']
for k, v in listed_token_mapping.items():
    headers.append(k)
    headers.append(k + '(KRW)')

start = "20181201"
end = "20181231"
closing_prices = {}
for symbol, slug in listed_token_mapping.items():
    print(symbol + '/', end='')
    symbol_krw = symbol + '(KRW)'
    if symbol not in closing_prices:
        closing_prices[symbol] = {}
        closing_prices[symbol_krw] = {}

    response = requests.get(f"https://coinmarketcap.com/currencies/{slug}/historical-data/?start={start}&end={end}")
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.select('tbody .text-right')
    for row in rows:
        date = str(datetime.strptime(row.select_one('.text-left').text, '%b %d, %Y').date())
        close = row.select_one('td:nth-child(5)').text
        if date not in closing_prices[symbol]:
            closing_prices[symbol][date] = {}
            closing_prices[symbol_krw][date] = {}

        closing_prices[symbol][date] = close
        closing_prices[symbol_krw][date] = ''
    sleep(3)

print(closing_prices)
print('- end to calculate closing price')
print(','.join(headers))

start_date = datetime.strptime(start, '%Y%m%d')
end_date = datetime.strptime(end, '%Y%m%d')
delta = end_date - start_date

for d in range(delta.days + 1):
    day = str((start_date + timedelta(d)).date())
    print(day + ',,', end='')
    for header in headers[2:]:
        if header in closing_prices:
            token = closing_prices[header]
            if day in token:
                print(token[day], end='')
        print(',', end='')
    print('')



