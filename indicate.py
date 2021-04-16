import pyupbit
import Model.Price


def getSignalTicker():
    result = []
    for ticker in pyupbit.get_tickers(fiat="KRW"):
        ma5 = Model.Price.getYesterdayMa5(ticker)
        target_price = Model.Price.getTargetPrice(ticker)
        current_price = pyupbit.get_current_price(ticker)

        if (current_price > target_price) and current_price > ma5:
            result.append(
                [ticker, (current_price / float(max(target_price, ma5)))])

    result.sort(key=lambda x: -x[1])

    print(len(result), "개 코인이 매수 신호가 잡혔습니다.")
    for i in result:
        print(i[0][4:], "코인이 타겟보다 현재가가 {0:0.2f} 배 높습니다.".format(i[1]))

    if result:
        print(result[0][0])
        return result[0][0]
    else:
        return "KRW-BTC"


def getYesterDayMa5Tests(ticker):
    df = pyupbit.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(window=5).mean()

    print(ma)


# upbit = Model.Key.getKey()
# print((upbit.get_balances()[1]['balance']))
