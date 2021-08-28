class Rectangle:
	def __init__(self, base, height):
		self.base = base
		self.height = height

	def area(self):
		return self.base * self.height


# The class [Square] extends [Rectangle]
class Square(Rectangle):
	def __init__(self, side):
		super().__init__(side, side)


def run():
	rectangle = Rectangle(base=3, height=4)
	print(rectangle.area()) # 12: 3*4

	square = Square(side=5) # 25: 5*5
	print(square.area())


if __name__ == '__main__':
	run()

