import pyupbit

# 키 발급
with open('key.txt', 'r') as f:
    access, secret = f.readlines()
upbit = pyupbit.Upbit(access.strip(), secret.strip())

# 보유 현금 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회


print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
