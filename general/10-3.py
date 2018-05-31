filename = 'guest.txt'
yourname = raw_input("input your name: ")

with open(filename, 'w') as file_object:
	file_object.write(yourname)
