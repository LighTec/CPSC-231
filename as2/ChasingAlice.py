import math
import turtle
import random

# Created By Kell Larson

def public_static_void_main(): #Memories of main methods past
	wrld, master, alex, alice = worldSetup()
	count = 0;

	FONT = ("Arial", 12, "normal")
	
	# Writes the step #, and the distance between alex and alice.
	# Needs to be here for the inital step.
	master.write("Step #: 0. Distance between Alex & Alice: {0:.2f}".format(abs(alex.distance(alice.xcor(), alice.ycor()))), font=FONT)

	# Keeps looping until win condition has been reached (alex within 30 pixels of alice)
	while(True):
		# Moves the turtles
		movePlayer(alex, alice)
		moveAI(alice, alex)
		count += 1
		master.clear()
		if(hasWon(alex,alice)):
			master.write("You have won in {0} turns!".format(count), font=FONT)
			# releases program from infinite loop
			break
		else:
			master.write("Step #: {0}. Distance between Alex & Alice: {1:.2f}".format(count, abs(alex.distance(alice.xcor(), alice.ycor()))), font=FONT)

	wrld.mainloop()

# Moves Alex. Will recurse until proper input is given
def movePlayer(alex, alice):
	move = input("")
	move = move.lower()
	
	#Moves / turns Alex, depending on input
	if (move == "w"):
		alex.forward(30)
	elif(move == "a"):
		alex.left(45)
	elif(move == "s"):
		alex.forward(-30)
	elif (move == "d"):
		alex.right(45)
	else:
		#Recurses if improper input
		print("string is not recognized as a movement. Retype as one of the WASD keys.")
		movePlayer(alex, alice)
	
	checkIfInBounds(alex, alice)

# Moves the computer controlled turtle, Alice. 2/3 chance of going forward,
# 1/6 chance turning 90 degrees right, 1/6 chance of turning 90 degrees left.
def moveAI(alice, alex):
	# chooses to turn of move forward
	choice = int(random.uniform(0,3))
	if(choice == 0):
		# chooses turn direction
		direc = int(random.uniform(0,2))
		if(direc == 0):
			alice.left(90)
		else:
			alice.right(90)
	else:
		alice.forward(20)
	checkIfInBounds(alice, alex)

# Makes sure the turtles are within the playground.
# If they aren't place them back within an acceptable range and domain.
def checkIfInBounds(toCheck, other):
	if(abs(toCheck.xcor()) > 250 or abs(toCheck.ycor()) > 250):
		moveTurtQuiet(toCheck, int(random.uniform(-240,240)),int(random.uniform(-240,240)))
		moveTurtQuiet(other, int(random.uniform(-240, 240)),int(random.uniform(-240,240)))

# Sets up the world, with proper screen size and turtle locations.
def worldSetup():
	wrld = turtle.Screen()
	wrld.title("Assignment 2: Chasing Alice!  By Kell Larson")
	turtle.setup(500,500)

	# creates the turtles
	alice = turtleFactory("Red")
	alex = turtleFactory("Blue")

	# moves alex somewhere on the screen, randomly.
	moveTurtQuiet(alice, int(random.uniform(-240,240)),int(random.uniform(-240,240)))
	#Alice is already at the center of the screen.

	master = turtleFactory("black")
	master.ht()
	#goto the top left corner of screen
	moveTurtQuiet(master, -245,220)

	return wrld, master, alex, alice

# Generates a generalized turtle, less code repetition
def turtleFactory(color):
	turt = turtle.Turtle()
	turt.color(color)
	turt.shape("turtle")
	turt.speed(0)
	return turt

# Returns true if alex and alice are within distance for the game
# to be considered as "won", if distance between them is less than 30
def hasWon(alex, alice):
	if(abs(alex.distance(alice.xcor(), alice.ycor())) < 30):
		return True
	else:
		return False

# Moves the turtle to an X,Y position without drawing a line.
def moveTurtQuiet(turt, x, y):
	turt.penup()
	turt.goto(x,y)
	turt.pendown()

public_static_void_main() # One day I can go back to Java
