T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    num = N // H + 1
    if floor == 0:
        floor = H
        num -= 1
    if len(str(num)) == 1:
        num = '0'+str(num)
    print(str(floor) + num if type(num) is str else str(floor) + str(num))