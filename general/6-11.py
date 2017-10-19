cities = {
	'ChengDu': {
		'country': 'China',
		'population': 1000,
		'food': 'Hotpot',
		},
	'Los Angles': {
		'country': 'America',
		'population': 2000,
		'food': 'Hamburger',
		},
	'Tokyo': {
		'country': 'Japen',
		'population': 500,
		'food': 'Sushi',
		},
	}

for city, infos in cities.items():
	print("The information of " + city + ":")
	print("belong to " + infos['country'])
	print("population is " + str(infos['population']))
	print("special food is " + infos['food'])
	print("\n")
