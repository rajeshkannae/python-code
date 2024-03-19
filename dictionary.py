alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

print(alien_0)

alien_0['x_position']=0
alien_0['y_position']=25

print(alien_0)

alien_0={}
alien_0['color']='green'
alien_0['points']=5

print(alien_0)

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
	x_increment=1
elif alien_0['speed'] == 'medium':
	x_increment=2
else:
	x_increment=3

alien_0['x_position']=alien_0['x_position']+x_increment

print(f"New position: {alien_0['x_position']}")

alien_0={'color':'green','points':5}
del alien_0['points']
print(alien_0)

point_value=alien_0.get('points','No point value assigned')
print(point_value)

person = {'first_name':'velrani','last_name':'rajaguru','age':32,'city':'Madurai'}
print(f"First name : {person['first_name']}")
print(f"Last name : {person['last_name']}")
print(f"Age : {person['age']}")
print(f"City : {person['city']}")

user_0={
	'username':'rajesh8880',
	'first':'rajesh',
	'last':'esakki'
}

for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
	print(f"{name.title()}")

for value in favorite_languages.values():
	print(f"{value.title()}")

for name, language in sorted(favorite_languages.items()):
	print(f"{name.title()}'s favorite language is {language.title()}.")

for value in set(favorite_languages.values()):
	print(f"{value.title()}")


rivers = {'Ganges':'India','nile':'Egypt','Thames':'England'}
for river,country in rivers.items():
	print(f"The {river} runs through {country}")

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
	print(alien)

aliens=[]

for alien_number in range(30):
	new_alien = {'color':'green','points':alien_number,'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print("...")

print(f"Total aliens : {len(aliens)}")

pizza = {
	'crust':'thick',
	'toppings':['mushrooms','extra cheese']
}
print(f"You ordered a {pizza['crust']}-crust pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")

favorite_languages = {
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell']
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are ")
	for language in languages:
		print(f"\t{language.title()}")
