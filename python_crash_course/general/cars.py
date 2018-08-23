cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

'''
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)
'''

'''
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
print(sorted(cars,reverse=True))

print("\n")
print(cars)
'''

'''
#倒着打印列表
cars.reverse()
print(cars)
'''

#确定列表的长度
print(len(cars))




#if语句
print("\n")
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())


#条件测试-检查是否相等
test = 'ss'
print(test == 'ss')	#True
print(test == 'xx')	#False
