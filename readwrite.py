with open("michaelho.txt") as name:
	my_name = name.read()

with open("testwrite.txt", "w") as new:
	new.write("Hello, my name is " + my_name)
