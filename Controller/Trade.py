import pyupbit


def buy_crypto_currency(upbit, ticker):
    krw = upbit.get_balance("KRW")
    if upbit.get_balance(ticker) == 0 and krw > 10000:  # 이미 샀으면 반복제거
        buy = upbit.buy_market_order(ticker, krw - krw * 0.05)
        print("구매 가격: ", buy['price'])
        print("구매 잔고: ", buy['volume'])
    # orderbook = pyupbit.get_orderbook(ticker)
    # 제일 싸게 파는 가격
    # sell_price = orderbook[0]['orderbook_units'][0]['ask_price']
    # unit = krw/float(sell_price)  # 내 돈 / 개당 가격


def sell_crypto_currency(upbit):
    balences = upbit.get_balances()
    if len(balences) > 1:
        print("전량 매도")
        for ticker in balences[1:]:
            unit = upbit.get_balance(ticker['balance'])
            print(upbit.sell_market_order(ticker, unit))
    # unit = upbit.get_balance(ticker)  # 코인 잔고
    # # orderbook = pyupbit.get_orderbook(ticker)
    # # buy_price = orderbook[0]['orderbook_units'][0]['bid_price']  # 제일 싸게 파는 가격

    # print(upbit.sell_market_order(ticker, unit))
