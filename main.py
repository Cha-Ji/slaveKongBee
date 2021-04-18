import pyupbit
import time
import datetime

import Model.Price
import Model.Key
import Controller.Trade


def setDate():
    # given: datetime module
    # when: in tommorw
    #   or: init program
    # then: set now, mid(tommorw)

    # today 9'o clock
    now = datetime.datetime.now() - datetime.timedelta(hours=9)

    # tommorw 9'o clock
    mid = datetime.datetime(now.year, now.month,
                            now.day) + datetime.timedelta(1)
    return now, mid


def sellSignal(now, mid):
    # given: signal, date
    # when: catch signal
    #  and: reset today
    # then: return True

    # if tommorw 9'o clock
    if mid < now < mid + datetime.timedelta(seconds=10):
        return True

    return False


def buySignal(current_price, target_price, ma5):
    # given: signal
    # when: catch signal
    # then: return True

    # target = (yesterday[high] - yesterday[low]) * 0.5
    if target_price > current_price:
        return False

    # ma5 = moving average in 5 days
    if ma5 > current_price:
        return False

    return True


def init():
    # --------show balance--------------------
    # given: key, ticker
    # when: init
    # then: print balance
    ticker = "KRW-BTC"
    upbit = Model.Key.getKey()
    for b in upbit.get_balances():
        print(b['currency'], ": ", b['balance'])
    # ---------------------------------------

    # -------buy indicator--------------------
    # given: yesterday price list
    # when: call get target
    # then: get ma5 & larry-price
    target_price = Model.Price.getTargetPrice(ticker)
    ma5 = Model.Price.getYesterdayMa5(ticker)
    print("larry:", target_price)
    print("ma5:", ma5)
    print("current:", pyupbit.get_current_price(ticker))
    # ---------------------------------------

    # -------sell indicator------------------
    # given: datetime
    # when: init
    # then: get now and tommorow
    now, mid = setDate()
    # ---------------------------------------

    # ----------init today result-------------
    buy = 0
    # ---------------------------------------

    # ---------------------------------------
    # ------check signal every seconds-------
    while True:
        try:
            now = datetime.datetime.now() - datetime.timedelta(hours=9)
            current_price = pyupbit.get_current_price(ticker)

            # ---------------sell----------------
            # given: datetime
            # when: now + 1day + 9hours
            # then: sell & update(datetime, buy_signal)
            #  and: print(krw)
            if sellSignal(now, mid):
                target_price = Model.Price.getTargetPrice(ticker)
                ma5 = Model.Price.getYesterdayMa5(ticker)
                mid = setDate()[1]
                Controller.Trade.sell_crypto_currency(upbit)
                print("잔고:", upbit.get_balance("KRW"))
                print("오늘의 구매내역:", buy)
            # ---------------------------------------

            # -------------buy---------------
            # given: current_price, target_price, ma5
            # when: current_price > max() & krw > 10000
            # then: buy_crypto_currency(all-in)
            if buySignal(
                current_price, target_price, ma5
            ) and (
                upbit.get_balance("KRW") > 10000
            ):
                buy = Controller.Trade.buy_crypto_currency(upbit, ticker)
            # ---------------------------------------
        except:
            print('에러')
        time.sleep(1)
    # ---------------------------------------


init()
