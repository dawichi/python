''' Backpack problem

'''
def backpack(size, weights, values, n): 
	if n == 0 or size == 0:
		return 0
	if weights[n - 1] > size:
		return backpack(size, weights, values, n-1)
	return max(
		values[n-1] + backpack(size-weights[n-1], weights, values, n-1),
		backpack(size, weights, values, n-1)
	)

if __name__ == '__main__':
	size = 50
	weights = [10, 20, 30]
	values = [60, 100, 120]
	n = len(values)

	result = backpack(size, weights, values, n)
	print(result)