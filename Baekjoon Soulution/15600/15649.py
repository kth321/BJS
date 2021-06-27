def seQence(n, m):
	outputs = []
	result = []
	def dfs(elements):
		if len(result) == m:
			outputs.append(result[:])
			return
		for e in elements:
			next = elements[:]
			next.remove(e)
			result.append(e)
			dfs(next)
			result.remove(e)
			
	dfs(list(range(1, n+1)))
	return outputs

n, m = map(int, input().split())
results = seQence(n, m)
for result in results:
	for element in result:
		print(element, end=' ')
	print()