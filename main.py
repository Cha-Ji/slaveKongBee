import pyupbit
import time
import datetime

import Model.Price
import Model.Key
import Controller.Trade


def updateDate():
    now = datetime.datetime.now()
    mid = datetime.datetime(now.year, now.month,
                            now.day) + datetime.timedelta(1)
    return now, mid


upbit = Model.Key.getKey()
now, mid = updateDate()
ticker = "BTC"
ma5 = Model.Price.getYesterdayMa5(ticker)
target_price = Model.Price.getTargetPrice(ticker)

while True:
    try:
        now = datetime.datetime.now()
        # update date & sell
        if mid < now < mid + datetime.timedelta(seconds=10):
            target_price = Model.Price.getTargetPrice(ticker)
            mid = updateDate()[1]
            ma5 = Model.Price.getYesterdayMa5(ticker)
            Controller.Trade.sell_crypto_currency(upbit, ticker)

        # buy
        current_price = pyupbit.get_current_price("KRW-" + ticker)
        if (current_price > target_price) and (current_price > ma5):
            Controller.Trade.buy_crypto_currency(upbit, ticker)
            True
    except:
        print('에러')
    time.sleep(1)
