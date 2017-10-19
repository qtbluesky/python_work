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

class Admin(User):
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("The privileges of an admin:")
        for privilege in self.privileges:
            print(privilege)


admin_sa = Admin('qing', 'tian', 'male', 25)
admin_sa.describe_user()
admin_sa.show_privileges()