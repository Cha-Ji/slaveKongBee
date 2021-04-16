import pyupbit

# get_tikers(fiat="KRW")


def getTikers():
    tickers = pyupbit.get_tickers(fiat="KRW")
    return tickers


# get current price
# element = ticker
def getCurrentPrice(coin):
    price = pyupbit.get_current_price("KRW-" + coin)
    return price


# prev price
# interval, count
def prevPrice(coin):
    df = pyupbit.get_ohlcv("KRW-" + coin)
    return df


# bid(매수호가), ask(매도호가)
orderbook = pyupbit.get_orderbook("KRW-XRP")
bids_asks = orderbook[0]['orderbook_units']
print(*bids_asks)

# 키 발급
with open('./model/key.txt', 'r') as f:
    access, secret = f.readlines()
upbit = pyupbit.Upbit(access.strip(), secret.strip())

# 보유 현금 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
