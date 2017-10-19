banner = "pls input your age to get the price: "

while True:
	age = input(banner)
	age = int(age)
	
	if age < 3:
		print("price is free.")
	elif 3 <= age and age <= 12:
		print("price is $10.")
	elif age > 12:
		print("price is $15.")
	else:
		print("input wrong, pls try again.")
