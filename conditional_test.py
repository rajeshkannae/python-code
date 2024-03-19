car = 'subaru'
print("Is car == 'subrau'? I predict True.")
print(car == 'subaru')

cars = ['subaru', 'bmw', 'nissan','toyota','AUDI']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	if car.lower() == 'audi':
		print(car.title())

aliens = {'color':'green','speed':'slow'}
point_value = aliens.get('points','No point value assigned')
print(point_value)


