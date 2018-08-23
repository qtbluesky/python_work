def build_profile(first, last, **user_info):
	profile={}
	profile['first_name'] = first
	profile['last_name'] = last
	
	for key, value in user_info.items():
		profile[key] = value
	return profile


user_profile = build_profile('Tian', 'Qing', location='CTU', field='Linux')
print(user_profile)
	
