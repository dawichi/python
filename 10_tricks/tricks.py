# Python tricks
from collections import Counter
import sys

'''
╭────────────────────────────────────╮
│   1. Save memory with Generators   │
╰────────────────────────────────────╯
Instead of create and keep the whole sequence in memory, the generator creates the next item in demand
'''
# List Comprehension
my_list = [x for x in range(1000)]
print(
    sum(my_list),						# 499500
    sys.getsizeof(my_list), "bytes"		# 9024 bytes
)
# Generator Comprehension
generator = (x for x in range(1000))
print(
    sum(generator),						# 499500
    sys.getsizeof(generator), "bytes"  # 88 bytes
)


'''
╭────────────────────────╮
│   2. Multiple inputs   │
╰────────────────────────╯
Get multiple values with a single input
'''
x, y, z = input("Enter three values: ").split()
print(x, y, z)   # Ex: 'one two three'


'''
╭────────────────────────────╮
│   3. Concatenate strings   │
╰────────────────────────────╯
with .join() now it's easier than ever
'''
arr = ['H', 'E', 'L', 'L', 'O']
print("".join(arr))


'''
╭─────────────────────────────────╮
│   4. Count items with counter   │
╰─────────────────────────────────╯ 
'''
list = [1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 5, 6, 6]
print(Counter(list))


'''
╭────────────────────────────────────────────╮
│   5. get(), setDefault() with Dictionary   │
╰────────────────────────────────────────────╯
Asign a default value to a dictionary
'''
dictionary = {1: 'one', 2: 'two', 4: 'four'}
print(dictionary.get(3))  # None
print(dictionary.setdefault(3, 'Default Value'))
print(dictionary.get(3))  # 'Default value'


'''
╭──────────────────────────────────────────╮
│   6. Sort complexs Iterables in One Go   │
╰──────────────────────────────────────────╯
sorted() sorts any iterable
'''
data = [
    {'name': 'John', 'age': 21},
    {'name': 'Lisa', 'age': 19},
    {'name': 'Mary', 'age': 22}
]
sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)


'''
╭────────────────────────────────────╮
│   7. Conditional List - All & Any  │
╰────────────────────────────────────╯
Instead of build many [if] conditions, use conditional lists
'''
physics = 49
chemistry = 51
mathematics = 57

list_condition = [
    physics > 50,
    chemistry > 50,
    mathematics > 50
]
print("Pass" if all(list_condition) else "Fail")  # Fail
print("Pass" if any(list_condition) else "Fail")  # Pass


'''
╭─────────────╮
│   9. Swap   │
╰─────────────╯
'''
a = 1
b = 2
a, b = b, a 	# swap values


'''
╭─────────────────────────────────╮
│   10. Return more than 1 value  │
╰─────────────────────────────────╯
'''


def SumAndSub(a, b):
    add = a + b
    sub = a - b
    return add, sub


addition, substraction = SumAndSub(20, 10)


'''
╭──────────────────────────────╮
│   11. Remove repeated items  │
╰──────────────────────────────╯
with set() you store unique values
'''
arr = [1, 2, 2, 3, 3, 3]
print(list(set(arr)))  # [1,2,3]


'''
╭─────────────────────────────────╮
│   12. Group 2 iterable objects  │
╰─────────────────────────────────╯
'''
names = list(zip((1, 2), ['Anna', 'Alice']))
print(names)  # [(1, 'Anna'), (2, 'Alice')]


'''
╭──────────────────────╮
│   13. Reverse lists  │
╰──────────────────────╯
'''
arr = [1, 2, 3, 4, 5]
print(arr[::-1])  # [5,4,3,2,1]


'''
╭────────────────────────────╮
│   14. Print data with sep  │
╰────────────────────────────╯
'''
user = 'user'
host = 'mail.com'
print(user, host, sep='@')  # user@mail.com

print('29', '09', '1999', sep='-')  # 29-09-1999


'''
╭─────────────────────────────────────╮
│   15. Swap dictionary key & values  │
╰─────────────────────────────────────╯
'''
my_dict = {1: 11, 2: 22, 3: 33}
my_dict = {i: j for j, i in my_dict.items()}
print(my_dict)  # {11: 1, 22: 2, 33: 3}


'''
╭─────────────────────────────────────────────╮
│   16. Get index of all letters in a string  │
╰─────────────────────────────────────────────╯
'''
s = 'Python'
e = enumerate(s)
print(list(e))  # [(0, 'P'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]
