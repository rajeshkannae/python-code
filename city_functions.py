def city_country (City, Country, population=''):
	if population:
		location = f"{City}, {Country} - population {population}"
	else:
		location = f"{City}, {Country}"
	return location.title()