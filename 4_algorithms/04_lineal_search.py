# Search items going through a list in a lineal way
import random

def search(list, target):
	match = False

	for element in list: # O(n)
		if element == target:
			match = True
			break

	return match


def run():
	list_size = int(input('Enter the size of the list: '))
	target = int(input('Which number will you look for: '))

	list = [random.randint(0, 100) for i in range(list_size)]
	found = search(list=list, target=target)

	print(list)
	print(f'The element {target} {"is" if found else "is not"} in the list')


if __name__ == '__main__':
	run()