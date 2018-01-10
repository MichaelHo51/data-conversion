from pprint import pprint
import json

# read superheroes.json into a variable
with open("superheroes.json") as f:
	rawdata = json.load(f) # now my whole json is the rawdata variable

# create variable for members
members = rawdata["members"]

#print members for sanity check
pprint(members)

#prep for csv export
import csv

#Write a new csv file
with open("supers.csv","w") as g:
	writer = csv.writer(g)

#Create a header for my csv file
	header = ["name", "age", "secretIdentity", "powers", "squadName", "homeTown", "formed", "secretBase","active"]
#write the header into new supers.csv	
	writer.writerow(header)

#Create heroes variable which loops over members variable
	for heroes in members:

#create row variable which stores all info of heroes
		row = [
			heroes["name"],
			heroes["age"],
			heroes["secretIdentity"],
			str(heroes["powers"]),
			rawdata["squadName"],
			rawdata["homeTown"],
			rawdata["formed"],
			rawdata["secretBase"],
			rawdata["active"]
			]
#write the hero info into new supers.csv
		writer.writerow(row)
pprint(row)
pprint(header)