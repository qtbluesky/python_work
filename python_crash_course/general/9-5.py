class User():
	def __init__(self, first_name, last_name, gender, age):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = first_name + " " + last_name
		self.gender = gender
		self.age = age
		self.login_attempts = 0
		
	def describe_user(self):
		print("Full Name: " + self.full_name.title() + 
				"\nFirst Name: " + self.first_name.title() + 
				"\nLast Name: " + self.last_name.title() +
				"\nGender: " + self.gender + 
				"\nAge: " + str(self.age)
				)
				
	def greet_user(self):
		print("Greeting! " + self.full_name.title())
		
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0
		
user1 = User('qing', 'tian', 'male', 25)
user1.describe_user()
user1.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)


