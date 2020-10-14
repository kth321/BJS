coins = []
N, K = map(int, input().split())
for _ in range(N):
    coins.append(int(input()))
ans = 0
coins.reverse()
for coin in coins:
    if K // coin > 0:
        tmp, K = divmod(K, coin)
        ans += tmp
print(ans)