import random

# Binary search!
def binary_search(list, start, end, target, steps):
	steps += 1
	if target > end:
		return False, steps
	mid = (start + end) // 2
	if list[mid] == target:
		return True, steps
	elif list[mid] < target:
		return binary_search(list, mid+1, end, target, steps)
	elif list[mid] > target:
		return binary_search(list, start, mid-1, target, steps)


if __name__ == '__main__':
	print('Generating a list between 0 and...')
	list_size = int(input('Enter the end of the list: '))
	target = int(input('Which number will you look for: '))
	list = [i for i in range(list_size)]
	
	result, steps = binary_search(list=list, start=0, end=len(list), target=target, steps=0)

	print()
	print(f'Binary search:')
	print(f'{"YES :D, is" if result else "NO ;( , is not"} in the list')
	print(f'steps: {steps}')






