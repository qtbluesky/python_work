class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		print("The restaurant's name is " + self.restaurant_name.title()
				+ ".")
		print("The type is " + self.cuisine_type + ".")
		
	def open_restaurant(self):
		print("The restaurant is working.")
	
	def set_number_served(self, number):
		self.number_served = number
		
	def increment_number_served(self, increment):
		self.number_served += increment
		

restaurant = Restaurant('beijing ducky', 'chinese food')

restaurant.describe_restaurant()
restaurant.open_restaurant()
print("The number of customers served: " + str(restaurant.number_served))
restaurant.number_served = 1000
print("The number of customers served: " + str(restaurant.number_served))

restaurant.set_number_served(2000)
print("The number of customers served: " + str(restaurant.number_served))
		
restaurant.increment_number_served(200)
print("The number of customers served: " + str(restaurant.number_served))
	
	

