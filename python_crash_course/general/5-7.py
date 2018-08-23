#喜欢的水果
favorite_fruits = ['apple', 'cherry', 'banana']
fruits = favorite_fruits[:]
fruits.append('pineapple')
fruits.append('orange')

for fruit in fruits:
	if fruit in favorite_fruits:
		print("I really like " + fruit + "!\n")
	else:
		print("I dont like " + fruit + ".\n")
