import random

def merge_sort(list):
	if len(list) > 1:
		mid = len(list) // 2
		left = list[:mid]
		right = list[mid:]
		print(left, '-'*5, right)

		# recursive call in each mid
		merge_sort(left)
		merge_sort(right)

		# Iterators to go throw lists
		i = 0
		j = 0
		# Iterator for main list
		k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				list[k] = left[i]
				i += 1
			else:
				list[k] = right[j]
				j += 1
			k += 1
		
		while i < len(left):
			list[k] = left[i]
			i += 1
			k += 1
		
		while j < len(right):
			list[k] = right[j]
			j += 1
			k += 1
		
		print(f'left: {left} ----- right: {right}')
		print(list)
		print()

	return list

		

if __name__ == '__main__':
	list_size = int(input('Enter the size of the list: '))
	list = [random.randint(0,100) for i in range(list_size)]
	print(list, '\n')

	sort_list = merge_sort(list)
	print(sort_list)