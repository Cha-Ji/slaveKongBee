import datetime
import pyupbit
import Price
import datetime
import requests
from bs4 import BeautifulSoup


def get_tickers_by_market_cap_rank(num=5):
    DEFAULT = ['KRW-BTC', 'KRW-ETH', 'KRW-XRP', 'KRW-BCH', 'KRW-LTC']
    try:
        url = "https://coinmarketcap.com/ko/"
        resp = requests.get(url)
        html = resp.text
        soup = BeautifulSoup(html, "html5lib")
        tags = soup.select(
            "#currencies > tbody > tr > td.no-wrap.text-right.circulating-supply > span > span.hidden-xs")
        tickers_by_market_cap = [tag.text for tag in tags]
        upbit_tickers_by_market_cap = [
            'KRW-' + ticker for ticker in tickers_by_market_cap[:num]]
        return upbit_tickers_by_market_cap
    except:
        return DEFAULT


def getSignalTicker():
    # given: upbit all tickers
    # when: catch signal
    # then: print buy signal order by ASC

    # get tickers ma5, target, ticker name
    tickerList = []
    getTickers = pyupbit.get_tickers(fiat="KRW")
    for ticker in getTickers:
        try:
            ma5 = Price.getYesterdayMa5(ticker)
            target_price = Price.getTargetPrice(ticker)
        except:
            ma5 = 9999999999
            target_price = 9999999999
            print(ticker, "getter error")
        tickerList.append([ma5, target_price, ticker])

    # catch
    while True:
        result = []
        ma5, target_price = 999999, 999999
        current_price = 0

        for tickerInfo in tickerList:
            try:
                ma5, target_price, ticker = tickerInfo
                current_price = pyupbit.get_current_price(ticker)

                if (current_price > target_price) and current_price > ma5:
                    result.append(
                        [ticker, (current_price / float(max(target_price, ma5)))])

            except:
                print(ticker, "result error")

        if result:
            result.sort(key=lambda x: -x[1])
        print("[", datetime.datetime.now(), "]")
        print(len(result), "개 코인이 매수 신호가 잡혔습니다.")
        for i in result:
            print(i[0][4:], "코인이 타겟보다 현재가가 {0:0.2f} 배 높습니다.".format(i[1]))


def getYesterDayMa5Tests(ticker):
    try:
        df = pyupbit.get_ohlcv(ticker)
        close = df['close']
        ma = close.rolling(window=5).mean()

        print(ma)
    except:
        print(ticker)
