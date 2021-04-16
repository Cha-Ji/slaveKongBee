import pyupbit
import time
import datetime

import Model.Price
import Model.Key
import Controller.Trade
import indicate


def setDate():
    now = datetime.datetime.now()
    mid = datetime.datetime(now.year, now.month,
                            now.day) + datetime.timedelta(hours=33)
    return now, mid


def sellSignal(now, mid):
    # 09시 일괄 판매
    if mid < now < mid + datetime.timedelta(seconds=10):
        return True

    return False


def buySignal(current_price, target_price, ma5):

    # 변동성을 돌파하지 못했다면
    if target_price > current_price:
        return False

    # 상승장이 아니라면
    if ma5 > current_price:
        return False

    return True


def init():
    ticker = indicate.getSignalTicker()
    upbit = Model.Key.getKey()
    for b in upbit.get_balances():
        print(b['currency'], ": ", b['balance'])
    print(*upbit.get_balances())

    target_price = Model.Price.getTargetPrice(ticker)
    ma5 = Model.Price.getYesterdayMa5(ticker)
    now, mid = setDate()

    while True:
        try:
            now = datetime.datetime.now()
            current_price = pyupbit.get_current_price(ticker)

            # update date & sell
            if sellSignal(now, mid):
                target_price = Model.Price.getTargetPrice(ticker)
                ma5 = Model.Price.getYesterdayMa5(ticker)
                mid = setDate()[1]
                Controller.Trade.sell_crypto_currency(upbit)
                ticker = indicate.getSignalTicker()

            # 매수 조건
            if buySignal(current_price, target_price, ma5):
                Controller.Trade.buy_crypto_currency(upbit, ticker)
        except:
            print('에러')

        time.sleep(1)
        print("now: ", current_price, "target: ",
              max(ma5, target_price), "time: ", now.month, "월", now.day, "일", now.hour, "시", now.minute, "분")


init()
