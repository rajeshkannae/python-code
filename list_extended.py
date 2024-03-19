magicians=['alice','david','carolina']
for magician in magicians:
	print(magician)
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was great magic show!")

pizza_list=['perpporoni','chicken','veg']
for pizza in pizza_list:
	print(f"I like {pizza} pizza")
print("I really love pizza!")


animals_list=['dog','cat','cow']
for animal in animals_list:
	print(f"A {animal} would make a great pet")
print("Any of these animals would make a great pet!")

#for value in range(1,5):
for value in range(5):
	print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers=list(range(2,11,2))
print(even_numbers)

squares=[]
for value in range(1,11):
	squares.append(value ** 2)

print(squares)

digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value ** 2 for value in range(1,11)]
print(squares)


for value in range(1,21):
	print(value)

million_list = [value for value in range(1,1000001)]
print(min(million_list))
print(max(million_list))
print(sum(million_list))

for value in range(1,20,2):
	print(value)

for value in range(3,30,3):
	print(value)


cubes = [value ** 3 for value in range(1,10)]
print(cubes)

players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[:2])
print(players[2:])
print(players[-3:])

for player in players[:3]:
	print(player.title())

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)

print("The first three items in the list are:")
print(my_foods[0:3])
print("Three items from the middle of the list are:")
print(my_foods[2:])
print("The last three items in the list are:")
print(my_foods[-3:])

friend_pizzas = pizza_list[:]
pizza_list.append('bacon')
friend_pizzas.append('ham')
print(f"My favorite pizzas are: {pizza_list}")
print(f"My friend favourite pizzas are: {friend_pizzas}")

