alien_0 = {'color' :'green', 'points': 5}
alien_1 = {'color' :'yellow', 'points':10}
alien_2 = {'color' : 'red', 'points':15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
	print(alien)

pets = ['dog','cat','goldfish','cat','rabbit']

while 'cat' in pets :
	print('hi')
	pets.remove('cat')

print(pets)

def describe_pets(animal_type, pet_name):
	print(f"I have a {animal_type}")
	print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pets(pet_name='dingu', animal_type='dog')

