
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])


print("\n")

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


print("\n")
#添加键-值对
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)



'''
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['color']
print(alien_0)
del alien_0['points']
print(alien_0)
'''

'''
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
print(alien_0[0])
'''


#移动的外星人
'''
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
	
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
'''
