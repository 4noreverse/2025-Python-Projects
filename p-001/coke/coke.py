import math
coke = 50
amount = 0
print(f'Amount Due: {coke}')
while coke > 0:
    coin = int(input('Insert Coin: '))
    if coin == 25 or coin == 10 or coin == 5:
        coke = coke - coin
    if coke > 0:
        print(f'Amount Due: {coke}')
    elif coke <= 0:
        change = abs(coke)
        print(f'Change Owed: {change}')
        break


