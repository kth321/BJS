import sys
coins = [500, 100, 50, 10, 5, 1]
cnt = 0
money = 1000 - int(sys.stdin.readline())
for coin in coins:
    if money // coin > 0:
        x, money = divmod(money, coin)
        cnt += x
print(cnt)