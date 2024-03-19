import json

favourite_number = input("Your favourite number : ")

with open("user_favourite.json",'w') as f:
	json.dump(favourite_number,f)

