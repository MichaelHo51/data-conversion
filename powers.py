from pprint import pprint
import json

# read superheroes.json
with open("superheroes.json") as f:
	data = json.load(f)

#create a blank list of powers
powers = []

#get list of members
members = data["members"]

#loop over members - for each member get powers
for hero in members:
	heropower = hero["powers"]
	for superpower in heropower:
		powers.append(superpower)

# add to list of powers
unique_powers = list(set(powers))
#print unique powers as flat csv

pprint(unique_powers)