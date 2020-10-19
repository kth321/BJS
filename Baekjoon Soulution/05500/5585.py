coins = [500, 100, 50, 10, 5, 1]
cnt = 0
n = 1000 - int(input())
for coin in coins:
    if n // coin > 0:
        x, n = divmod(n, coin)
        cnt += x
print(cnt)