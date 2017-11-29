#        R
#        R
#       R
#       R
#      R
#      R
#     R
#     R
#
# By Kell Larson

import sys

# Returns the input of a given filename, by parsing the values into a 2d array.
def getInput(fileName):
	txt = []
	for line in open(fileName, "r"):
		temp = line.replace("\n", "")
		txt.append(temp)
	return txt

print(getInput(sys.argv[1]))

class Car:
	def __init__(self, isTargetCar, isOriginal, ID):
		# Determines whether or not if this is the target car,
		# also known as the car that needs to reach (2,5) on the grid
		# to win or complete the game.
		target = isTargetCar

		# Determines whether if this is the original object, or a
		# disposable Car object that is used to occupy the grid to
		# demonstrate multiple square sized vehicles. These blocks are
		# created to be checked against in case something wants to move
		# to it's position. When the car they belong to is moved, all non
		# origin Car objects related to the car being moved are deleted and
		# recreated. If the Car object is not the origin, it is a "shadow copy".
		origin = isOriginal

		# the unique identification number belonging to the car and its shadow
		# copies, to help track car positioning.
		num = ID

	def __str__(self):
		print("hello")

	def isOriginal(self):
		if(origin):
			# do something
		else:
			# do something else

class Board:
	def __init__(self, inputList):
		board = [[]]

		for row in board:
			break

	def addCar(self):
		print("hello")

	def loadGame(self):
		takes the input array from getInput(), calls addCar() a bunch of times. Also adds
		all of the cars to the carArr array.

	def gameOver(self):
		if(the board point (2,5) has the car with target == True on it
			return True
		else:
			return False

	def __str__(self):
		return str(board)

	def moveCar(self):
