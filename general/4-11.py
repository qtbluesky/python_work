#你的披萨和我的披萨

pizzas = ['fruit pizza', 'chees pizza', 'royal pizza', 'cream pizza']
for pizza in pizzas:
	print("I like " + pizza + "!\n")
print("I really love pizza!\n")

friend_pizzas = pizzas[:]

pizzas.append('yummy pizza')
friend_pizzas.append('burger pizza')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
