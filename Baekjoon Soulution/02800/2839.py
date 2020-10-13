N = int(input())
available_5kg = N//5
result = -1
for i in range(available_5kg, -1, -1):
    bag_5kg = i
    remain = N - (5 * i)
    if remain == 0:
        result = bag_5kg
        break
    if remain // 3 != 0:
        bag_3kg = remain // 3
        remain %= 3
        if remain != 0:
            continue
        else:
            result = bag_5kg + bag_3kg
            break
print(result)
            
