import sys

# Tested and working.

def test_suite():
	test(replace("Mississippi", "i", "I") == "MIssIssIppI")
	s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
	test(replace(s, "om", "am") ==
	"I love spam! Spam is my favorite food. Spam, spam, yum!")
	test(replace(s, "o", "a") ==
	"I lave spam! Spam is my favarite faad. Spam, spam, yum!")

def test(tested): # Used for testing functions.
	line = sys._getframe(1).f_lineno # get the line number from which this is called
	if tested:
		print("Test at line {0} good.".format(line))
	else:
		print("Test at line {0} FAIL.".format(line))

def replace(s, old, new):
	sSplit = s.split(old)
	sJoin = new.join(sSplit)
	return sJoin

test_suite()	
