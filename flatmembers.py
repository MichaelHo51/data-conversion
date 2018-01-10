from pprint import pprint
import json

# read superheroes.json into a variable
with open("superheroes.json") as f:
	rawdata = json.load(f)

# select the members
# loop over the members
members = rawdata["members"]
pprint(members)
# output headers
import csv
with open("supers.csv","w") as g:
	writer = csv.writer(g)
	header = ["name", "age", "secretIdentity", "powers", "squadName", "homeTown", "formed", "secretBase","active"]
	writer.writerow(header)
# for each member, output the row
	for heroes in members:
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
		writer.writerow(row)
pprint(row)
pprint(header)