#河流
rivers = {'nile': 'egypt', 'amazon': 'peru', 'yangtze': 'china', 
		'mississipi': 'american'
		}
		
		
for river, country in rivers.items():
	print("The " + river.title() + " runs through " + country.title() + ".\n")
	
for river in rivers.keys():
	print(river.title() + "\n")
	
for country in rivers.values():
	print(country.title() + "\n")
