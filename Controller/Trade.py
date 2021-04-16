import pyupbit


def buy_crypto_currency(upbit, ticker):
    krw = upbit.get_balance(ticker)[2]
    orderbook = pyupbit.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw/float(sell_price)
    # upbit.buy_market_order(ticker, unit)


def sell_crypto_currency(upbit, ticker):
    unit = upbit.get_balance(ticker)[0]
    # upbit.sell_market_order(ticker, unit)  # FIXME: 메소드이름
