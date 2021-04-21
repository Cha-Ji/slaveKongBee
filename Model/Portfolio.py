import pyupbit


def selectPortfolio(tickers, window=5):
    COIN_NUMS = 10
    DUAL_NOISE_LIMIT = 0.6
    try:
        portfolio = []
        noise_list = []

        # given: all tickers df[open], df[close]. df[high], df[low]
        for ticker in tickers:
            df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
            noise = 1 - abs(df['open'] - df['close']) / \
                (df['high'] - df['low'])
            average_noise = noise.rolling(window=window).mean()
            noise_list.append((ticker, average_noise[-2]))

        sorted_noise_list = sorted(
            noise_list, key=lambda x: x[1])  # noise DESC

        # when: noise < DUAL_NOISE_LIMIT
        for x in sorted_noise_list[:COIN_NUMS]:
            if x[1] < DUAL_NOISE_LIMIT:
                portfolio.append(x[0])

        # then: return portfolio[:COIN_NUMS]
        return portfolio

    except:
        return None
