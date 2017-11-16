import sys

# Chapter 16, exercise 2 and 3.

# By Kell Larson

# Tested and working.

def test_suite():
	r = Rectangle(Point(10,5), 100, 50)
	test(str(r) == "((10, 5), 100, 50)")
	r.grow(25, -10)
	test(str(r) == "((10, 5), 125, 40)")
	r.move(-10, 10)
	test(str(r) == "((0, 15), 125, 40)")
	r = Rectangle(Point(0, 0), 10, 5)
	test(r.perimeter() == 30)
	r = Rectangle(Point(100, 50), 10, 5)
	test(r.width == 10 and r.height == 5)
	r.flip()
	test(r.width == 5 and r.height == 10)

def test(tested): # Used for testing functions.
	line = sys._getframe(1).f_lineno # get the line number from which this is called
	if tested:
		print("Test at line {0} good.".format(line))
	else:
		print("Test at line {0} FAIL.".format(line))

class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def distance_from_origin(self):
		return ((self.x ** 2) + (self.y ** 2)) ** 0.5
	
	def __str__(self):
		return "({0}, {1})".format(self.x, self.y)

	def halfway(self, target):
		mx = (self.x + target.x)/2
		my = (self.y + target.y)/2
		return Point(mx, my)

	def reflect_x(self):
		self.y = self.y * -1
		return self


class Rectangle:
	def __init__(self, corner=Point(0,0), width=0, height=0):
		self.corner = corner
		self.width = width
		self.height = height
	
	def __str__(self):
		return "({0}, {1}, {2})".format(str(self.corner), self.width, self.height)

	def grow(self, delta_width, delta_height):
		self.width += delta_width
		self.height += delta_height

	def move(self, dx, dy):
		self.corner.x += dx
		self.corner.y += dy

	def perimeter(self):
		ww = self.width * 2
		hh = self.height * 2
		return (ww + hh)
	def flip(self):
		temp = self.width
		self.width = self.height
		self.height = temp

test_suite()
