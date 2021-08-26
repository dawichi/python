def divisors(num):
	divisors = []
	for i in range(1, num + 1):
		if num % i == 0:
			divisors.append(i)
	return divisors

def run():
	num = int(input("Entry a integer: "))
	print(divisors(num))
	print("End of program")

if __name__ == '__main__':
	run()