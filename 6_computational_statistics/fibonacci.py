# If u try to calculate a number bigger than 30-35, will start to take so much time
# because the function must calculate every small number multiple times in a exponential growth
def fibonacci_recursive(n):
	if n == 0 or n == 1:
		return 1
	return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Best solution: memorize the result in a dictionary and now is instant! Even if u calc f(500)
# The key is to exchange [time] with [space]:
#   --> you save time when calculating, by saving the results in memotu (space)
def fibonacci_dynamic(n, memo = {}):
	if n == 0 or n == 1:
		return 1

	try:
		return memo[n]
	except KeyError:
		result = fibonacci_dynamic(n - 1, memo) + fibonacci_dynamic(n - 2, memo)
		memo[n] = result
		return result


if __name__ == '__main__':
	n = int(input('Type a number: '))
	print(fibonacci_dynamic(n))