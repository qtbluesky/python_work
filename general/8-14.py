def add_car(company, model, **infos):
	car_info = {}
	car_info['company'] = company
	car_info['model'] = model
	
	for key, value in infos.items():
		car_info[key] = value
		
	return car_info
	
car = add_car('benz', 'a45', color='grey', others='AMG')
print(car)
	
