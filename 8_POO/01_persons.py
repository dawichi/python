class Person:
	def __init__(self, name, age) -> None:
		self.name = name
		self.age = age

	def say_hello(self):
		print(f'Hi, I\'m {self.name}, {self.age} years old')

if __name__ == '__main__':
	person = Person('David', 34)
	person.say_hello()