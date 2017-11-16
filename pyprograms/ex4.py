import sys
# Created by Kell Larson

def get_triangle_number(n):
	return (n * (n + 1)) // 2

def print_triangular_numbers(n):
# Line 10 derived from this example: 
#https://stackoverflow.com/questions/10623727/python-spacing-and-aligning-strings
	print("%-*s  %s" % (15,n,get_triangle_number(n)))
	if n != 1:
		print_triangular_numbers(n-1) # recursion!

# Tested and working.

def num_digits(n):
	n = abs(n)
	if n == 0:
		return 1
	count = 0
	while n != 0:
		count = count + 1
		n = n // 10
	return count

def test_suite():
	#test(theMethodToTest("stuff") == "a thing") # All of these should return "good"
	print_triangular_numbers(5)
	test(num_digits(0) == 1)
	test(num_digits(1234) == 4)
	test(num_digits(-123) == 3)
	test(num_digits(0) == 1)
	test(num_digits(-12345) == 5)

def test(tested): # Used for testing functions.
	line = sys._getframe(1).f_lineno # get the line number from which this is called
	if tested:
		print("Test at line {0} good.".format(line))
	else:
		print("Test at line {0} FAIL.".format(line))

test_suite()





