def greet_user():
	"""Display a simple greeting."""
	print('hello')

greet_user()

def greet_user(username):
	"""Display a simple greeting."""
	print(f"Hello, {username.title()}!")

greet_user('Rajesh')

def describe_pet(animal_type, pet_name):
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

def describe_pet(pet_name, animal_type='dog'):
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='Willie')

describe_pet('harry','hamster')

def make_shirt(size='L', text='I love Python'):
	print(f"\nSize of the T-Shirt is {size}")
	print(f"\nMessage in the T-Shirt is '{text.title()}'.")

make_shirt('M','Universe is the boss')
make_shirt(text='My arguments interchanged',size='M')

make_shirt()
make_shirt(size='M')

def get_formatted(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {middle_name} {last_name}"
	return full_name.title()

scientist = get_formatted('vishrudh','rajesh', 'kanna')
print(scientist)

def build_person(first_name, last_name, age=None):
	person = {'first':first_name,'last':last_name}
	if age:
		person['age']=age
	return person

musician = build_person('rajesh','kanna', age='42')
print(musician)

# def City_Country(city, country):
# 	print(f'"{city}, {country}"')

# while True:
# 	print(f"Please provide City and Country")
# 	city = input("City : ")
# 	if city == 'q':
# 		break
# 	country = input("Country : ")
# 	if country == 'q':
# 		break
# 	City_Country(city, country)


def make_album(artist, title, no_songs = None):
	album_detail = {'artist':artist, 'title':title}
	if no_songs:
		album_detail['no_songs'] = no_songs
	return album_detail

album_detail = make_album('rajesh','life')
print(album_detail)
album_detail = make_album('vishrudh','forever', 100)
print(album_detail)
album_detail = make_album('velrani','life')
print(album_detail)


def greet_users(names):
	for name in names:
		msg=f"Hello, {name.title()}!"
		print(msg)

usernames=['rajesh','vishrudh','yazhini']
greet_users(usernames)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design}")
	completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		completed = unprinted_designs.pop()
		completed_models.append(completed)

	#print(completed_models)

print_models(unprinted_designs[:],completed_models)

print(unprinted_designs)


short_message = ['hello world','hi vishrudh','hi yazhini']

def show_messages(short_message):
	for message in short_message:
		print(f"{message}")

#show_messages(short_message)

def send_messages(short_message):
	sent_message = []
	while short_message:
		sent_message.append(short_message.pop())

	print(sent_message)

# send_messages(short_message)
# print(short_message)

send_messages(short_message[:])
print(short_message)

def make_pizza(*toppings):
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extrac cheese')

def make_pizza(size, *toppings):
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')

def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('rajesh','kanna',location='cincinnati',field='physics')
print(user_profile)

def sandwich(**items):
	return items

sandwichitem = sandwich(bread='honey wheat')
print(sandwichitem)

sandwichitem = sandwich(bread='honey wheat',cheese='american')
print(sandwichitem)

def make_car(manufacturer, model, **carinfo):
	carinfo['manufacturer'] = manufacturer
	carinfo['model'] = model
	return carinfo

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

