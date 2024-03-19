#message=input("Tell me something, and I will repeat it back to you :")
#print(message)

#name = input("Please enter your name: ")
#print(f"\nHello, {name}!")

# age = input("how old are you? ")
# age = int(age)
# print(age>=18)

#rental_car = input("What kind of rental car they would like?")
#print(f"\nLet me see if I can find you a {rental_car}")


# current_number = 1
# while current_number <= 5:
# 	print(current_number)
# 	current_number += 1


# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
# 	message = input(prompt)
# 	print(message)

# prompt = "\nPlease enter the name of city you have visited"

# while True:
# 	city = input(prompt)

# 	if city == 'quit':
# 		break
# 	else:
# 		print(f"I'd love to go to {city.title()}")

# current_number = 0
# while current_number < 10:
# 	current_number += 1
# 	if current_number % 2 == 0:
# 		continue

# 	print(current_number)

# pizza_topping = "\nPlease enter toppings. Enter 'quit' if you want to exit"
# while True:
# 	topping = input(pizza_topping)

# 	if topping == 'quit':
# 		break
# 	else:
# 		print(f"You like the {topping.title()} topping")
	

# prompt = "\nEnter your age. Enter 'quit' if you want to exit "

# while True:
# 	age = input(prompt)

# 	if age == 'quit':
# 		break
# 	else:
# 		if int(age) < 3:
# 			print(f"Ticket is free")
# 		elif int(age) >=3 and int(age) <12:
# 			print(f"Cost of the ticket is $10")
# 		elif int(age) >= 12:
# 			print(f"Cost of the ticket is $15")

sandwich_orders = ['veg','chicken','fish']
finished_sandwiches = []

for sandwich in sandwich_orders:
	print(f"I made your {sandwich} sandwich")
	finished_sandwiches.append(sandwich)

print(finished_sandwiches)

finished_sandwiches.append('pastrami')
finished_sandwiches.append('tuna')
finished_sandwiches.append('pastrami')
finished_sandwiches.append('pastrami')

print(finished_sandwiches)

while 'pastrami' in finished_sandwiches:
	finished_sandwiches.remove('pastrami')

print(finished_sandwiches)












