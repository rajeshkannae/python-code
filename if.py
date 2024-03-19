cars=['audi','bmw','nissan','toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")

banned_users = ['andrew','carolina','david']
user='marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a reqponse if you wish.")

car='subaru'
print(car == 'subaru')

print(car == 'audi')

age=12
if age<4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25.")
else:
	print("Your admission cost is $40.")

alien_color='red'
if alien_color == 'green':
	print("You have earned 5 points")

if alien_color == 'green':
	print("You have earned 5 points")
else:
	print("You have earned 10 points")

if alien_color == 'green':
	print("You have earned 5 points")
elif alien_color == 'yellow':
	print("You have earned 10 points")
elif alien_color == 'red':
	print("You have earned 15 points")

age=32
if age<2:
	print("You are an baby")
elif age>=2 and age<4:
	print("You are an toddler")
elif age>=4 and age<13:
	print("You are an kid")
elif age>=13 and age<20:
	print("You are an teenager")
elif age>=20 and age<65:
	print("You are an adult")
elif age>=65:
	print("You are an elder")

requested_toppings=[]
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

users=['rajesh','vishrudh','yazini','admin']
for user in users:
	if user == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print(f"Hello {user.title()}, thank you for logging in again")

user=[]
if user:
	print("users are there")
else:
	print("We need to find some users!")

current_users=["rajesh","yazini","vishrudh","babu","puppy"]
new_users = ["andrew","jim","tom","babu","puppy"]

for newuser in new_users:
	if newuser in current_users:
		print("Username already exists. Enter new user name")
	else:
		print("Username is available")

numbers = list(range(1,10))
for number in numbers:
	if number == 1:
		print("1st")
	elif number == 2:
		print("2nd")
	elif number == 3:
		print("3rd")
	else:
		print(f"{number}th")


