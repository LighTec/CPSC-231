import sys

# Tested and working.

def test_suite():
	test(theMethodToTest("stuff") == "a thing") # All of these should return "good"

def test(tested): # Used for testing functions.
	line = sys._getframe(1).f_lineno # get the line number from which this is called
	if tested:
		print("Test at line {0} good.".format(line))
	else:
		print("Test at line {0} FAIL.".format(line))

test_suite()
