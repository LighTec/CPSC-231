# Chapter 20, exercise 1, read from sys.stdin


# By Kell Larson

import sys

# Tested and working.

def getCounts(fileName):
	letterAmt = {}
	tempLetters = ""
	for line in open(fileName):
		tempLetters += line
	tempLetters = tempLetters.lower()
	for letter in tempLetters:
		if(letter == ' ' or letter == '\n'):
			continue
		letterAmt[letter] = letterAmt.get(letter, 0) + 1
	letterAmt = list(letterAmt.items())
	letterAmt = sorted(letterAmt)
	
	for letter in letterAmt:
		print(letter[0], ' ', letter[1])

def test_suite():
	getCounts("sys.stdin")

def test(tested): # Used for testing functions.
	line = sys._getframe(1).f_lineno # get the line number from which this is called
	if tested:
		print("Test at line {0} good.".format(line))
	else:
		print("Test at line {0} FAIL.".format(line))

test_suite()
