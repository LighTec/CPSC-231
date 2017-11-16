import sys

#By Kell Larson

#Chapter 8, excercises 8 & 9.

# Tested and working.

def mirror(s):
	mirroredStr = ""
	totalStr = s;
	Sarr = []
	for ch in s:
		Sarr.append(ch)
	subtractor = len(Sarr) - 1
	for i in range(len(Sarr)):
		totalStr += Sarr[subtractor - i]
	return totalStr

def remove_letter(rmch, s):
	endStr = ""
	for ch in s:
		if ch != rmch:
			endStr += ch
	return endStr

def test(tested): # Used for testing functions.
	line = sys._getframe(1).f_lineno # get the line number from which this is called
	if tested:
		print("Test at line {0} good.".format(line))
	else:
		print("Test at line {0} FAIL.".format(line))

def test_suite():
	test(mirror("good") == "gooddoog")
	test(mirror("Python") == "PythonnohtyP")
	test(mirror("") == "")
	test(mirror("a") == "aa")
	test(remove_letter("a", "apple") == "pple")
	test(remove_letter("a", "banana") == "bnn")
	test(remove_letter("z", "banana") == "banana")
	test(remove_letter("i", "Mississippi") == "Msssspp")
	test(remove_letter("b", "") == "")
	test(remove_letter("b", "c") == "c")

test_suite()
