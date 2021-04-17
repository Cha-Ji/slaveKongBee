import pyupbit


def getTargetPrice(ticker):
    # given: upbit key
    #  and: yesterday[close, high, low]
    # when: 9'o clock
    # then: return target price
    df = pyupbit.get_ohlcv(ticker)
    yesterday = df.iloc[-2]  # yesterday data

    todayOpen = yesterday['close']  # 당일 시가
    yesterdayHigh = yesterday['high']  # 전일 고가
    yesterdayLow = yesterday['low']  # 전일 저가
    target = todayOpen + (yesterdayHigh - yesterdayLow) * 0.5

    return target


def getYesterdayMa5(ticker):
    # given: upbit key
    #  and: past 5 days data
    # when: 9'o clock
    # then: return moving average price
    df = pyupbit.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(window=5).mean()
    return ma[-2]
