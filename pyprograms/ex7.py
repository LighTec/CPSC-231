# Chapter 18, exercise 7

import sys


def flatten(lst):
	newlst = []
	for element in lst:
		if(type(element) == type([])):
			temp = []
			temp = flatten(element)
			for piece in temp:
				newlst.append(piece)
		else:
			newlst.append(element)
	return newlst

def test_suite():
	test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
	test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
	test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
	test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==["this","a","thing","a","is","a","easy"])
	test(flatten([]) == []) 
	test(flatten([1,[2,[3,[4,5],6],7],8]) == [1,2,3,4,5,6,7,8])

def test(tested): # Used for testing functions.
	line = sys._getframe(1).f_lineno # get the line number from which this is called
	if tested:
		print("Test at line {0} good.".format(line))
	else:
		print("Test at line {0} FAIL.".format(line))

test_suite()
