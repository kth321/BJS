T = int(input())
stack = []
result = ""
last = 1
flag = False
for _ in range(T):
    n = int(input())
    if len(stack) >= 1:
        if n < stack[-1]:
            flag = True            
    while last <= n:
        stack.append(last)
        result += '+'
        last += 1
    stack.pop()
    result += '-'
if flag is False:
    for s in result:
        print(s)
else:
    print('NO')