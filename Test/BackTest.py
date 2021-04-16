import pyupbit
import numpy as np
from pandas import DataFrame

tickers = pyupbit.get_tickers(fiat="KRW")

maxNode = 0
minNode = 100
result = []

for ticker in tickers:
    ticker = ticker[4:]
    df = pyupbit.get_ohlcv("KRW-" + ticker)

    df['ma5'] = df['close'].rolling(window=5).mean().shift(1)
    df['range'] = (df['high'] - df['low']) * 0.5
    df['target'] = df['open'] + df['range'].shift(1)

    # 상승장 돌파
    df['bull'] = df['open'] > df['ma5']

    fee = 0.0032  # 빗썸기준 (업비트는 더 저렴)
    df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
                         df['close'] / df['target'] - fee, 1)

    df['hpr'] = df['ror'].cumprod()
    df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

    result.append([ticker, df['dd'].max(), df['hpr'][-2]])


def printResult():

    for node in sorted(result, key=lambda x: x[2]):
        if node[2] > 1:
            print("[", node[0], "형님 ]: {0:0.2f}".format(node[2]), "배가 되었다구 ~")
        else:
            print("[", node[0], ".. ]")

        # print("  MDD: {0:0.2f}".format(
        #     df['dd'].max()), "% (최대 누적 손실 낙폭)")  # 최대 누적 손실

    # df.to_excel("Test/" + ticker + ".xlsx")


printResult()
