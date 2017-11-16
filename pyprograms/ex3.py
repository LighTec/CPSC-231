import sys

# Tested and working. Unsure about proper name to give to the
# grade() method.

def test_suite(int_arr):
	test(turn_clockwise("N") == "E") # All of these should return "good"
	test(turn_clockwise("W") == "N")
	test(turn_clockwise("S") == "W")
	test(turn_clockwise("E") == "S")
	test(turn_clockwise(76) == None)
	test(turn_clockwise("used clothing") == None)
	for i in xs:
		print(mark(i))

def turn_clockwise(direc): # turns the given cardinal direction 90 degrees to the right
	if direc == "N":
		return "E"
	elif direc == "E":
		return "S"
	elif direc == "S":
		return "W"
	elif direc == "W":
		return "N"
	else:
		#print("Incorrect data entered.") # if anything but cardinal directions given
		return None

def mark(num):
	if num >= 75:
		return "First"
	elif num >= 70:
		return "Upper Second"
	elif num >= 60:
		return "Second"
	elif num >= 50:
		return "Third"
	elif num >= 45:
		return "F1 Supp"
	elif num >= 40:
		return "F2"
	else:
		return "F3"

def test(tested): # Used for testing functions.
	line = sys._getframe(1).f_lineno # get the line number from which this is called
	if tested:
		print("Test at line {0} good.".format(line))
	else:
		print("Test at line {0} FAIL.".format(line))

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0]

test_suite(xs)
