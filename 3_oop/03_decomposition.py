class Auto:
	def __init__(self, brand, model, color):
		self.brand = brand
		self.model = model
		self.color = color
		self._state = 'parking'
		self._motor = None

	def acelerate(self, type='slow'):
		if type == 'fast':
			self._motor.put_gas(10)
		else:
			self._motor.put_gas(3)

class Motor:
	def __init__(self, type='gasoline'):
		self.type = type
		self._temperature = 0

	def put_gas(self, liters):
		pass