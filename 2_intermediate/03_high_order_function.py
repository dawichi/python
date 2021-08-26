''' High order function

Is a function which gets as param another function
'''

def say(func):
	func()

def hi():
	print("hi")

def bye():
	print("bye")

say(hi)
say(bye)


''' 3 important high order functions:

	filter, map , reduce

'''
# Filter
# example: get only the odd numbers
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd = [i for i in list if i % 2 != 0]         # List comprehensions solution
odd = list(filter(lambda x: x%2 != 0, list))  # Filter function


# Map
# example: get the list with the items elevated to square
list = [1, 2, 3, 4, 5]
square = [i**2 for i in list]               # List comprehensions solution
square = list(map(lambda x: x**2, list))    # Map function


# Reduce
# example: get the result of multiply all numbers in a list
list = [2, 2, 2, 2, 2]

# Using for loop
multiplied = 1
for i in list:
	multiplied = multiplied * i   

# Using reduce
from functools import reduce
list = [2, 2, 2, 2, 2]
multiplied = reduce(lambda a, b: a * b, list)                   