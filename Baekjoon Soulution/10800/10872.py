N = int(input())
factorial = 1
for i in range(N, 0, -1):
    factorial *= i
print(factorial)