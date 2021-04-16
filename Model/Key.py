import pyupbit


def getKey():
    with open('Model/key.txt', 'r') as f:
        access, secret = f.readlines()
    upbit = pyupbit.Upbit(access.strip(), secret.strip())
    return upbit
