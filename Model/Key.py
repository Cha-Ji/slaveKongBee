import pyupbit


def getKey():
    # given: upbit API
    # when: call this def
    # then: return API
    with open('Model/key.txt', 'r') as f:
        access, secret = f.readlines()
    upbit = pyupbit.Upbit(access.strip(), secret.strip())
    return upbit
