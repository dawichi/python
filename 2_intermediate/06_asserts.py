''' Assert statement

You check a condition, if is no true, returns an error message
─ code
    └─ assert
	    └─ true: code
	    └─ false: error

Ex:   assert condition, error message
'''

# 1. This onoe will return true, because "" its a palindrome for python
'----------------------------------'
def palindrome(string):
	return string == string[::-1]

print(palindrome(""))
'----------------------------------'


# 2. So to control the empty string case, we can use assert so the program will return AssertionError, being able to control it with try/except
'----------------------------------'
def palindrome(string):
	assert len(string) > 0, "It's not allowed to enter empty values"
	return string == string[::-1]

print(palindrome(""))
'----------------------------------'


