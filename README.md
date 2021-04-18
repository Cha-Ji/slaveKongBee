# Upbit Auto Trade
## Install

```python
pip install openpyxl
pip install pyupbit
pip install PyQt5
pip install PyQtChart
```

## How To Run

- get access key, private key from upbit API
- ```
  $vi Model/key.txt
- ```
    asdf1234
    qwer1234
- ```
    :wq!
- set ticker in main.py (default = "KRW-BTC")

## Release

- ver 0.1
  - given: past data
  - when: catch 2 buy signal
  - then: buy BTC (all-in)
  - when: tommorw 9'o clock
  - then: sell all

## Contack

chajiwon100785@gmail.com

## Copyright 

[출처 소스코드]https://github.com/sharebook-kr/book-cryptocurrency
[*파이썬을 이용한 비트코인 자동매매 (개정판)*. 조대표 외 1명]https://wikidocs.net/book/1665