import pyupbit
import time
import datetime

import Model.Price
import Model.Key
import Controller.Trade


def sellSignal():
    # given: datetime module
    # when: catch signal
    # then: return True

    # if 9'o clock
    now = datetime.datetime.now()
    if now.hour == 9 and now.minute == 0 and (0 <= now.second <= 10):
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

    # falling coin

    return True


def init():
    # --------debug setting-------------------
    DEBUG = True
    ticker = "KRW-BTC"
    # --------show balance--------------------
    # given: key, ticker
    # when: init
    # then: print balance
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
    # given:
    # when:
    # then:

    # ---------------------------------------

    # ----------init today result-------------
    buy = 0
    # ---------------------------------------

    # ---------------------------------------
    # ------check signal every seconds-------
    while True:
        try:
            current_price = pyupbit.get_current_price(ticker)

            # ---------------sell----------------
            # given: datetime
            # when: 9:00.00 ~ 9:00.10
            # then: sell & update(buy_signal)
            #  and: print(krw)
            if sellSignal():
                target_price = Model.Price.getTargetPrice(ticker)
                ma5 = Model.Price.getYesterdayMa5(ticker)

                if not DEBUG:
                    Controller.Trade.sell_crypto_currency(upbit)
                else:
                    print("sell all", ticker)

                print("잔고:", upbit.get_balance("KRW"))
                print("오늘의 구매내역:", buy)
                time.sleep(10)
            # ---------------------------------------

            # -------------buy---------------
            # given: current_price, target_price, ma5
            # when: current_price > max()
            # then: buy_crypto_currency(all-in)
            elif buySignal(current_price, target_price, ma5):

                if not DEBUG:
                    buy = Controller.Trade.buy_crypto_currency(upbit, ticker)
                else:
                    print("buy:", ticker)
                    print("price:", current_price)
                    print("target:", target_price)
            # ---------------------------------------
        except:
            print('에러')
        time.sleep(1)
    # ---------------------------------------


init()
