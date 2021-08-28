import time

def factorial(n):
	response = 1
	while n > 1:
		response *= n
		n -= 1
	return response


# recursive solution
def factorial_r(n):
	if n == 1:
		return 1
	return n * factorial(n - 1)

if __name__ == '__main__':
	n = 200000
	start = time.time()
	factorial(n)
	end = time.time()
	print(end - start)

	start = time.time()
	factorial_r(n)
	end = time.time()
	print(end - start)



