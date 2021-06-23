from collections import defaultdict

def dfs(result, start_v=1):
	if start_v not in result:
		result.append(start_v)
		for vertex in table[start_v]:
			dfs(result, vertex)
	return result


table = defaultdict(list)
input()
for _ in range(int(input())):
	start_v, end_v = map(int, input().split())
	table[start_v].append(end_v)
	table[end_v].append(start_v)
result = dfs([])
print(len(result) - 1)