import json

with open("user_favourite.json") as f:
	favourite = json.load(f)

print(f"I know your favourite number! It's {favourite}")