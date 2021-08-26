def divisors(num):
	divisors = []
	for i in range(1, num + 1):
		if num % i == 0:
			divisors.append(i)
	return divisors

def run():
	try:
		num = input("Entry a integer: ")
		assert num.isnumeric(), "You must enter a number"
		print(divisors(int(num)))
		print("End of program")
	except ValueError:
		print("You must enter a number")

if __name__ == '__main__':
	run()