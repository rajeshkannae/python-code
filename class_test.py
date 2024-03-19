class TV:
	def __init__(self, make, inches):
		self.make = make
		self.inches = inches

	def print_tv(self):
		tv_description = f"{self.make}  TV is  {self.inches} inches"
		return tv_description


my_tv = TV("LG","50")
print(my_tv.print_tv())


class LG(TV):
	def __init__(self, make, inches):
		super().__init__(make, inches)


lg_tv = LG("LG","50")
print(lg_tv.print_tv())

from random import randint

class Die:
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		return randint(1,self.sides)

i=1
die_6 = Die()

while i<=10:
	print(die_6.roll_die())
	i+=1

print(f"Die 6 completed")

i=1
die_10 = Die(10)

while i<=10:
	print(die_10.roll_die())
	i+=1
