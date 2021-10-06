# Decorators
#
#  A decorator, is a function that envolves another function, modifying that one
#  It allows to add code which executes "before" the function and "after" the function
#
#  For example, if we have a function "list elements", we can make it private by adding a decorator "admin_required" which checks if the user is an admin
#

PASSWORD = '1234'

# Decorator def
def admin_required(func):
	def wrapper():
		password = input('Enter the admin password: ')
		if password == PASSWORD:
			return func()
		else:
			print('The password is not correct')
	return wrapper


# Decorator added to the list function
@admin_required
def list_private_data():
	print('DATA super important')






#
#   another example: make a decorator to upper() the text of another function
#
def upper(func):
	def wrapper(*args, **kwargs):
		result = func(*args, *kwargs)
		return result.upper()
	return wrapper

@upper
def say_name(name):
	return 'Hello, {}'.format(name)


if __name__ == '__main__':
	list_private_data()
	print(say_name('David'))



