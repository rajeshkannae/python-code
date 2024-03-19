favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}

fav = favorite_languages.get('sarah','No person in the dictionary')
print(fav)

fav = favorite_languages.get('rajesh','No person in the dictionary')
print(fav)


for person, language in favorite_languages.items():
	print(f"{person.title()} favourite language is {language}")

for name in favorite_languages.keys():
	print(name.title())
