''' Anonymous functions

A anonymous function or a 'lambda' function as it is known in python)
Can only have 1 line of code.
In another langs as JS, anonymous functions can have multiple lines, but not in python
Structure:

	lambda params: expression

'''

palindrome = lambda string: string == string[::-1]
palindrome('ana')


# VS normal functions

def palindrome(string):
	return string == string[::-1]
palindrome('ana')




