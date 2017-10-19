banner = "pls input your age to get the price: "
flag = True
while flag:
	age = input(banner)
	age = int(age)
	
	if age < 3:
		print("price is free.")
		break
	elif 3 <= age and age <= 12:
		print("price is $10.")
		break
	elif age > 12:
		print("price is $15.")
		break
	else:
		print("input wrong, pls try again.")

#	flag = False
