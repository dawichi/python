class Person:

	def __init__(self, name):
		self.name = name

	def advance(self):
		print('Person: Moving forward walking')


class Cyclist(Person):

	def __init__(self, name):
		super().__init__(name)
	
	def advance(self):
		print('Cyclist: Moving forward on a bike')


def run():
	person = Person('David')
	person.advance()
	
	cyclist = Cyclist('Ana')
	cyclist.advance()


if __name__ == '__main__':
	run()
