import binance.client 
import time
import re
import datetime

# for order on binance
from binance.enums import *

api_key = "<API KEYを入力>"
api_secret = "<API SECRETを入力>"

client = binance.client.Client(api_key, api_secret)

prices = client.get_all_tickers()
symbolLen = len(prices)

# 下落率
rateOfDecline = 3.0

# 現在価格、30分後の価格
beforePrices = [prices[i]['price'] for i in range(symbolLen)]
afterPrices = [0 for i in range(symbolLen)]

def buyCoin( symbol, afterPrice ):
    print("called buy")
    
    order = client.create_test_order(
        symbol=symbol,
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        price=afterPrice,
        quantity=1)
        
    print(order)
    return

while 1==1:
    time.sleep(1800)
    prices = client.get_all_tickers()
    for i in range(symbolLen):
        # 30分後の価格取得
        afterPrices[i] = prices[i]['price']
        # 30分前の価格と現在の価格を比較して、下落率・上昇率を計算
        pricePropotion = 100 - (float(afterPrices[i]) / float(beforePrices[i])) * 100
        # それぞれの銘柄で指定したパーセンテージ下落していたら買いを入れる。
        if pricePropotion > rateOfDecline :
            if re.search(r'BTC', prices[i]['symbol']):
                #買いを入れたときの時間
                print('time: ' + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + ' , ticker: ' + prices[i]['symbol'] + ' , PricePropotion: ' + str(pricePropotion) + ' , ' + afterPrices[i] + ' , ' + beforePrices[i])
                #買い注文
                afterPrice = round(float(afterPrices[i]), 8)
                if afterPrice > 0.0001:
                    print(afterPrice)
                    buyCoin(prices[i]['symbol'], afterPrice)
                break
                
    for i in range(symbolLen):
        beforePrices[i] = prices[i]['price']
