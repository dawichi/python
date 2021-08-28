# OOP in Python

To define a class in Python
````python
class Hotel:
	pass
````

Then we can create an instance of that class calling the constructor
````python
hotel = Hotel()
````


## Instance's atributes

All classes create objects, and all objects have atributes.

We use `__init__` to define the initial state of our instance. Gets as first obligatory parameter `self` which is a reference for the instance

````python
class Hotel:
	def __init__(self, max_clients, parking_places):
		self.max_clients = max_clients
		self.parking_places = parking_places
		self.clients = 0

hotel = Hotel(max_clients = 50, parking_places = 20)

print(hotel.parking_places) # 20
````

## Instance's methods

While instance's atributes describe the object, methods show what we can to do with that instance.

````python
class Hotel:
	def __init__(self, max_clients, parking_places):
		self.max_clients = max_clients
		self.parking_places = parking_places
		self.clients = 0

	def add_client(self, number_clients):
		self.clients += number_clients
	
	def checkout(self, number_clients):
		self.clients -= number_clients

	def current_clients(self):
		return self.clients

hotel = Hotel(max_clients = 50, parking_places = 20)

hotel.add_client(3)
hotel.checkout(1)
hotel.current_clients() # 2
````
