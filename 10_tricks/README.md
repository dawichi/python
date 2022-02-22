# python-tricks

Some python useful shortcodes

---

### Lists

- Retrieve the last element

```python
list = [1,2,3,4,5]
# 3 methods: brute force / negative index / pop
last_element = list[len(list) - 1]
last_element = list[-1]
last_element = list.pop()
```

- List comprehension

```python
def get_vowels(string):
	return [vowel for vowel in string if vowel in 'aeiou']
```

- Element most common

```python
def most_frequent(list):
	return max(set(list), key=list.count)
```

- Convert lists to dictionary

```python
def lists_to_dict(keys_list, values_list):
	return dict(zip(keys_list, values_list))
```

- Remove duplicates

```python
list = [1,2,2,3,3,3]
# Option 1:
    result = []
    [result.append(x) for x in list if x not in result]
    print(result) # [1,2,3]
# Option 2:
	print(list(set(arr))) # [1,2,3]
```

- Count items with counter

```python
from collections import Counter
list = [1,1,1,1,2,2,2,3,4,4,4,5,5,5,6,6]
print(Counter(list))    # Counter({1: 4, 2: 3, 3: 1, 4: 3, 5: 3, 6: 2})
print(Counter('hello')) # Counter({'h': 1, 'e': 1, 'l': 2, 'o': 1})
```

- Reverse lists

```python
arr = [1,2,3,4,5]
print(arr[::-1]) # [5,4,3,2,1]
```

- Concatenate strings

```python
arr = ['H', 'E', 'L', 'L', 'O']
print(''.join(arr)) # 'HELLO'
```

- Conditional list

```python
physics = 49
chemistry = 51
mathematics = 57

# Instead of build so many [if / else], just with a conditional list:
list_condition = [
	physics > 50,
	chemistry > 50,
	mathematics > 50
]
print("Pass" if all(list_condition) else "Fail") # Fail
print("Pass" if any(list_condition) else "Fail") # Pass
```

### Dictionaries

- Asign a default value

```python
dictionary = {1: 'one', 2: 'two', 4: 'four'}
print(dictionary.get(3))	# None
print(dictionary.setdefault(3, 'Default Value'))
print(dictionary.get(3))	# 'Default value'
```

- Swap keys & values

```python
dictionary = {1: 11, 2: 22, 3:33}
swap_dict = {i: j for j, i in dictionary.items()}
print(swap_dict) # {11: 1, 22: 2, 33: 3}
```

### Utils

- Swap values

```python
a = 1
b = 0
a, b = b, a
```

- Sort complex iterables

```python
data = [
	{'name': 'John', 'age': 21},
	{'name': 'Lisa', 'age': 19},
	{'name': 'Mary', 'age': 22}
]
sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)
```

- Group 2 iterable objects

```python
names = list(zip((1,2), ['Anna', 'Alice']))
print(names) # [(1, 'Anna'), (2, 'Alice')]
```

- Check if a file exists

```python
from os import path
print("Does file exist: ", path.exists("data.csv"))
```

- Error handling

```python
a, b = 1, 0
try:
	print(a / b)
except ZeroDivisionError:
	print("Cannot divide by 0")
finally:
	print("End block")
```

- Comparison in oneline

```python
a = 8
print(2 < a < 8) # True
```

- Get index of all letters in a string

```python
print(list(enumerate('Python')))	# [(0, 'P'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]
```

- Print data with separators

```python
user = 'user'
host = 'mail.com'
print(user, host, sep='@') # user@mail.com
print('29', '09', '1999', sep='-') # 29-09-1999
```

- Return multiple values

```python
def SumAndSub(a, b):
	add = a + b
	sub = a - b
	return add, sub

addition, substraction = SumAndSub(20, 10)
```

- Multiple inputs

```python
x, y, z = input("Enter three values: ").split()
print(x, y, z)   # Ex: 'one two three'
```

- Print multiple strings

```python
n = 5
print ('hello' * 5)	# hellohellohellohellohello
```

- Check execution time of a function

```python
import time
start_time = time.time()
# code to check time performance
end_time = time.time()
print('Time: ', end_time - start_time)
```

- Save memory with generators

```python
import sys
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
	sys.getsizeof(generator), "bytes"	# 88 bytes
)
```
