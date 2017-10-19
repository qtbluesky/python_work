'''
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
'''

'''	
print("Sarah's favorite language is " + 
	favorite_languages['sarah'].title() + 
	".")
'''
favorite_languages = {}
favorite_languages['jen'] = 'go'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, langueage in favorite_languages.items():
	print(name.title() + "'s favorite langueage is " + langueage.title()
	+ ".")


'''
#if 'python' in favorite_languages.values():
if 'erin' not in favorite_languages.keys():
	print("yes")
else:
	print("no")
'''	

