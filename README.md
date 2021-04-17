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