N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
intersection = A.intersection(B)
union = A.union(B)
result = union.difference(intersection)
print(len(result))