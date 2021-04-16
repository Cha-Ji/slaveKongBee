import pyupbit


def getTargetPrice(ticker):
    df = pyupbit.get_ohlcv("KRW-" + ticker)
    yesterday = df.iloc[-2]  # yesterday data

    todayOpen = yesterday['close']  # 당일 시가
    yesterdayHigh = yesterday['high']  # 전일 고가
    yesterdayLow = yesterday['low']  # 전일 저가
    target = todayOpen + (yesterdayHigh - yesterdayLow) * 0.5

    return target

# 5일 이동 평균


def getYesterdayMa5(ticker):
    df = pyupbit.get_ohlcv("KRW-" + ticker)
    close = df['close']
    ma = close.rolling(window=5).mean()
    return ma[-2]
