filename = 'guest_book.txt'

while True:
	guest_name = raw_input("pls input your name: ")
	
	with open(filename, 'a') as file_object:
		file_object.write(guest_name + "\n")
