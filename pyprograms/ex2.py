import math

def area_of_circle(r):
	rr = r**2
	return math.pi * rr

radius = input('please enter the radius of the circle: ')
area = area_of_circle(float(radius))
print('the area is')
print(area)
