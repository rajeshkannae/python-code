class Car():

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		self.litre = 0

	def display_car(self):
		print(f"This car is {self.year} {self.make.title()} {self.model.title()}")

	def print_odom(self):
		print(f"This car odometer reading is {self.odometer_reading}")

	def update_odom(self, reading):
		self.odometer_reading += reading

	def fill_tank(self, litre):
		self.litre += litre
		print(f"Fuel in the tank is {self.litre} litres")

mycar = Car('nissan','altima',2011)
mycar.display_car()
mycar.print_odom()
mycar.update_odom(10000)
mycar.print_odom()
mycar.fill_tank(3)


class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)

	def fill_tank(self):
		print(f"Electric car don't have gas tank")


myelectric = ElectricCar("Tesla","ABC", 2020)
myelectric.fill_tank();

