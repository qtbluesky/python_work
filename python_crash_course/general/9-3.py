class User():
	def __init__(self, first_name, last_name, gender, age):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = first_name + " " + last_name
		self.gender = gender
		self.age = age
		
	def describe_user(self):
		print("Full Name: " + self.full_name.title() + 
				"\nFirst Name: " + self.first_name.title() + 
				"\nLast Name: " + self.last_name.title() +
				"\nGender: " + self.gender + 
				"\nAge: " + str(self.age)
				)
				
	def greet_user(self):
		print("Greeting! " + self.full_name.title())
		
user1 = User('qing', 'tian', 'male', 25)
user1.describe_user()
user1.greet_user()

