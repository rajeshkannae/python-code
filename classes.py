class Dog:

	def __init__(self, name, age):
		self.name = name
		self.age= age

	def sit(self):
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()


class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"My restaurant {self.restaurant_name} has cuisine type {self.cuisine_type}.")

	def open_restaurant(self):
		print(f"My restaurant {self.restaurant_name} is open!")

my_restaurant = Restaurant("Vishrudh", "Chicken")

print(f"My restaurant name is {my_restaurant.restaurant_name}")
print(f"My restaurant cuisine is {my_restaurant.cuisine_type}")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


my_restaurant1 = Restaurant("Velrani", "Veg")
my_restaurant2 = Restaurant("Rajesh", "Non veg")

my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()


class Car:

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 50
my_new_car.read_odometer()

my_new_car.update_odometer(25)

from car import Car, ElectricCar
#import car
#car.Car

my_nissan = Car('Nissan','Altima','2012')
print(my_nissan.get_descriptive_name())

my_tesla = ElectricCar('tesla','model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()


class IceCreamStand(Restaurant):

	def __init__(self, flavors):
		self.flavors = flavors

	def printflavor(self):
		print(f"Flavors available : {self.flavors}")

flavors = ['chocolate', 'pineapple','vennilla']

icecream_stand = IceCreamStand(flavors)
icecream_stand.printflavor()


class User():

	def __init__(self, first_name, last_name):
		self.first_name=first_name
		self.last_name=last_name

	def describe_user(self):
		print(f"User First Name : {self.first_name}")
		print(f"User Last Name : {self.last_name}")

	def greet_user(self):
		print(f"Hello {self.first_name} {self.last_name}")

my_user = User("Vishrudh","Rajesh")
my_user.greet_user()
my_user.describe_user()



class Privileges:
	def __init__(self, privileges=["can add post","can delete post","can ban user"]):
		self.privileges = privileges

	def show_privileges(self):
		print(f"Administrator's privileges are : {self.privileges}")

class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()

my_admin = Admin('Vishrudh','Rajesh')
my_admin.privileges.show_privileges()

