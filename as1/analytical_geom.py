# Created by Kell Larson

import turtle
import math

xc, yc = eval(input()) # get values
r = eval(input())
x1, y1 = eval(input())
x2, y2 = eval(input())

def draw_line(xi, yi, xf, yf):

	""" Draws a line with given data, with circles at each end."""
	lineTurt = turtle.Turtle() #make a specific line turtle
	lineTurt.speed(0) # gotta go fasttttttttt

	lineCirc = 10 # radius of the circle that is drawn
	# at each end of the line

	circ_yi = yi - lineCirc # Make the circle at the end of the line,
	#not beside it

	lineTurt.penup() #put turtle at x1, y1 relative to orgin
	lineTurt.goto(xi,circ_yi) # goto initial coordinates + circle
	lineTurt.pendown()

	lineTurt.circle(lineCirc) # circle at beginning of line
	
	lineTurt.penup() # to avoid drawing a non-useful line
	lineTurt.goto(xi,yi) # go back to the line origin
	lineTurt.pendown() # allows it to draw the line

	# for testing purposes
	#print('final: (xy)')
	#print(goodxf)
	#print(goodyf)
	#print('initial: (xy)')
	#print(goodxi)
	#print(goodyi)

	lineTurt.goto(xf, yf) # draw the line
	
	lineTurt.penup() # don't draw this line though
	circ_yf = yf - lineCirc  # calculate circle offset
	lineTurt.goto(xf, circ_yf) # goto end circle offset
	lineTurt.pendown() # allow it to draw the circle

	lineTurt.circle(lineCirc) # circle at the end of the line

	lineTurt.ht() #this turtle is done, hide it forever

def calc_quadratic(posNeg):
	""" Takes the sample data, and calculates the intersects.
	All are integers, except for posNeg, which is boolean, describing
	whether to add or subtract in the quadratic formula. """
	
	Xsquared = (x2 - x1) ** 2
	Ysquared = (y2 - y1) ** 2 # calculate the line deltas squared
	
	#print('+++++++++++++++++++++++++++++++++++++++++')
	#print('X and Y squared: (x,y)')
	#print(Xsquared)
	#print(Ysquared)
	#print('----------------------------------')

	Xdelta = (x2 - x1) # just the line deltas
	Ydelta = (y2 - y1)

	#print('delta x, then y:') # Print statements
	#print(Xdelta)		   # to bugfix FTW
	#print(Ydelta)
	#print('-----------------------------------')

	Xcirc = (x1 - xc) # calculate circle postion relative
	Ycirc = (y1 - yc) # to the line origin

	#print('circle delta, x then y')
	#print(Xcirc)
	#print(Ycirc)
	#print('-------------------------------------')
	

	# calculating the actual quadratic, with ax^2 + bx + c = 0.
	a = Xsquared + Ysquared

	b = 2 * abs((Xcirc * Xdelta) + (Ycirc * Ydelta))

	c = (Xcirc ** 2) + (Ycirc ** 2) - (r ** 2)

	#print("a: ")
	#print(a)
	#print("b: ")
	#print(b)	# For testing only
	#print("c: ")
	#print(c)
	#print('-----------------------------------------')

	sqroot = math.sqrt((b ** 2) - ( 4 * a * c)) # find (b^2 - 4ac)^1/2
	divdr = 2 * a # 2a, just a multiplied by 2

	#print('2a:')
	#print(divdr)
	#print('square root soln:')
	#print(sqroot)
	#print('negative b:')
	#print(negB)
	#print('++++++++++++++++++++++++++++++++++++++++')

	if(posNeg): # used to choose if the square root portion
		    # should be added or subtracted from -b
		alpha = (b + sqroot) / divdr
	else:
		alpha = (b - sqroot) / divdr
	#print('Alpha calculated to be')
	#print(alpha)
	return alpha #return the result

def generateIntersect(alpha):

	"""Creates circles at any intersections between the line
	and the circle."""

	Xint = ((1 - alpha) * x1) + (alpha * x2) # x of the intersect
	Yint = ((1 - alpha) * y1) + (alpha * y2) # y of the intersect

	circRadius = 6
	
	turMan = turtle.Turtle() # need something to draw with
	turMan.speed(0) # gotta go fast
	turMan.penup() # don't draw while going to the intersect
	turMan.goto(Xint, Yint - circRadius) # goto the intersect, offset
			# for the circle's radius
	turMan.pendown() # allow it to draw the circle
	turMan.circle(circRadius) # draw the circle

	turMan.ht()
	#print('Intersect draw: (x,y):')
	#print(Xint)
	#print(Yint)

def drawCircle():
	circTurt = turtle.Turtle() # circle turtle
	circTurt.speed(0) # become sonic

	circTurt.penup() # don't draw while going to circle coordinates

	circTurt.goto(xc, yc) #goto the circle coords

	circTurt.right(90)
	circTurt.forward(r) # goto the edge of the circle, was at the middle
	#of it
	circTurt.left(90)
	circTurt.pendown() # allow turtle to draw circle
	circTurt.circle(r) #draw the circle with supplied radius
	circTurt.ht() # done with this turtle, its now an eyesore to have
	#around

wn = turtle.Screen() # create a screen to draw on

wn.setworldcoordinates(0,0,1000,800) # fix the coordinate system to the
# old way

#wn.bgcolor("lightgreen") # Set up the window and its attributes
#wn.screensize(800,600) # ensure the screen size is correct

drawCircle() # draws the circle to intercept

draw_line(x1,y1,x2,y2) # draws the intercept line

alpha1 = calc_quadratic(True) # calculate when adding the square root
alpha2 = calc_quadratic(False)# calculate when subtracting the square root

#print(alpha1)
#print(alpha2) # for testing
if(alpha1 >= 0) and (alpha1 <= 1): # only create intersect circles
	generateIntersect(alpha1)  # if the alpha value is in its
if(alpha2 >= 0) and (alpha2 <= 1): # valid domain
	generateIntersect(alpha2)
#if(alpha1 == alpha2):
#	generateIntersect((-1) * alpha1)

wn.mainloop() # Creates an event listener and executor (such as display
# refreshes)

