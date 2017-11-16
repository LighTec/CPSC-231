# Chapter 15, exercise 1 and 2

# By Kell Larson

import sys

# Takes two points, returns distance as a float
def distance(p1, p2):
	dx = p1.x - p2.x
	dy = p1.y - p2.y
	dsquared = dx*dx + dy*dy
	result = dsquared**0.5
	return result	

def test_suite():
	test(distance(Point(1,1), Point(1,5)) == 4)
	test(distance(Point(0,0), Point(2,2)) == (8 ** (1/2)))
	test(distance(Point(-1,-1), Point(9,9)) == (200 ** (1/2)))
	p = Point(7,9)
	p2 = Point(7,-9)
	test(str(p.reflect_x()) == str(p2))

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

test_suite()
