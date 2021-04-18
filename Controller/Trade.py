import pyupbit


def buy_crypto_currency(upbit, ticker):
    # given: key
    # when: catch buy signal
    # then: buy ticker market price (all-in)
    #  and: return buy info
    krw = upbit.get_balance("KRW")
    # 시장가 전량 매수
    buy = upbit.buy_market_order(ticker, krw - krw * 0.05)
    return buy

    # --------------지정가 매수-------------------
    # orderbook = pyupbit.get_orderbook(ticker)
    # 제일 싸게 파는 가격
    # sell_price = orderbook[0]['orderbook_units'][0]['ask_price']
    # unit = krw/float(sell_price)  # 내 돈 / 개당 가격
    # -------------------------------------
    # 시드가 커지면 지정가를 활용하자.


def sell_crypto_currency(upbit):
    # given: key
    # when: catch sell signal
    # then: sell all
    #  and: print result
    balences = upbit.get_balances()
    if len(balences) > 1:
        print("전량 매도")
        for ticker in balences[1:]:
            unit = upbit.get_balance(ticker['balance'])
            print(upbit.sell_market_order(ticker['currency'], unit))

    # --------------지정가 매도-----------------------
    # unit = upbit.get_balance(ticker)  # 코인 잔고
    # # orderbook = pyupbit.get_orderbook(ticker)
    # # buy_price = orderbook[0]['orderbook_units'][0]['bid_price']  # 제일 싸게 파는 가격

    # print(upbit.sell_market_order(ticker, unit))
    # --------------------------------------------
