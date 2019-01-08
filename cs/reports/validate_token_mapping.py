import json

import requests

with open('./listed_tokens.txt', 'r') as f:
    line = f.readlines()
listed_tokens = [x.strip() for x in line]

with open('./listed_token_mapping.txt', 'r') as f:
    mapping = f.read()
listed_token_mapping = eval(mapping)

headers = {'Content-Type': 'application/json', 'X-CMC_PRO_API_KEY': '340098de-0c2e-430c-9573-9ba23e707875'}
response = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/map', headers=headers)
json_response = json.loads(response.text)
coin_market_tokens = json_response['data']

coin_market_tokens_dict = {}
for token in coin_market_tokens:
    symbol = token['symbol']
    slug = token['slug']
    if symbol in listed_tokens:
        if symbol not in coin_market_tokens_dict:
            coin_market_tokens_dict[symbol] = []
        coin_market_tokens_dict[symbol].append(slug)

for k, v in coin_market_tokens_dict.items():
    if k in listed_token_mapping:
        if v[0] != listed_token_mapping[k]:
            print(f"{k}: listed_token: {listed_token_mapping[k]} <=> {v}")


