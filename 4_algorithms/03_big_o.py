''' Algorithmic complexity

O(x)
----------------------
1         constant
n         lineal
log n     logarithmic
n log n   log lineal
n**2      polynomial
2**n      exponential
'''


# Sum law
def f(x):
	for i in range(x):
		print(i)
	
	for i in range(x):
		print(i)

# O(n) + O(n) = O(n + n) = O(2n) = O(n)



# Multiple recursive
def fibonacci(n):
	if n == 0 or n == 1:
		return 1
	
	return fibonacci(n - 1) + fibonacci(n - 2) 