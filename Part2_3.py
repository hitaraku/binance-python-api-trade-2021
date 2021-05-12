import binance.client

api_key = "<API KEYを入力>"
api_secret = "<API SECRETを入力>"

client = binance.client.Client(api_key, api_secret)

print(client.get_all_tickers())