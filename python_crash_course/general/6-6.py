#调查

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
	
survey_people = ['jen', 'tom', 'jim', 'edward']

for people in survey_people:
	if people in favorite_languages.keys():
		print("Thanks, " + people.title() + "\n")
	else:
		print("We invite you, " + people.title() + "\n")
