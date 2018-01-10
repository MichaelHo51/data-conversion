vegetables = [
	{"name": "eggplant"},
	{"name": "carrot"},
	{"name": "turnip"},
	{"name": "squash"},
	{"name": "okra"},
	{"name": "corn"},
	{"name": "radish"},
	{"name": "green beans"},
	{"name": "kale"},
	{"name": "lettuce"},
	{"name": "cabbage"},
]

import csv

with open("veggies.csv", "w") as veggies:
	writer = csv.writer(veggies)
	writer.writerow(["name", "length"])
	for x in vegetables:

#Give name of vegetable and length of name for each vegetable
		vegetable_name = x["name"]
		vegetable_length = len(x["name"])
		writer.writerow([vegetable_name, vegetable_length])