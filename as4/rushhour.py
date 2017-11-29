import random
import turtle
import math
import tkinter.font

root = tkinter.Tk()
# FOnts setup
fonts=tkinter.font.families(root)

# As you can tell, this is wildly out of scope.
# At the time of writing, it's 12:27 AM, almost 2
# days after the due date. The text version of my rush
# hour prototype is buggy, and likes to delete cars at
# the edge of the array. Still haven't figured out
# how to properly install pygame. I just decided to 
# procrastinate my hours away. I'd just rather turn
# anything rather than nothing in. So, this program
# uses the turtle graphics library in order to take a
# random position in relation to the turle, draw a
# line with random width and color, turn a random
# amount, then take a random font from the tkinter
# library and take one of the words below randomly
# and write it with a random size. I understand that
# I'm getting a 0/10 (even if given glitz, its
# -5 points for late submission anyways) Anyhow, built
# this to learn turtle graphics for assignment 1 and 2
# Late September.


#########################################################
# TL;DR: Bad time management, couldn't get assignment
# 4 done. Just wanted to hand anything in. Thought this
# would break the monotomy of marking. Expecting a 0/10
# for this assignment.
#########################################################

# Word library
rush = ['derp', 'DERP', 'Hello world!', 'Much line', 'Very wow', 'Such random','ASDF','boop'
,'rush hour', 'rushhour', 'much car', 'very rush', 'so puzzle', 'wow', 'derp', 'foo'
, 'python3', 'rushour', 'never', 'gonna', 'give', 'you', 'up'
, 'never', 'gonna', 'let', 'you', 'down', 'never', 'gonna', 'turn', 'around', 'and', 'desert', 'you'
, ':(', 'traffic sim 2019', 'beep beep', 'DERP', 'dErP', 'DeRp', 'derp', 'derP', 'dErp', 'deRp']

# Create the screen
wn = turtle.Screen()
# Change the turtle color scheme to RGB 0-255 values
wn.colormode(255)

def draw_multicolor_line_word(t, sz):
	# random line width
	t.pensize(int(random.uniform(1,15)))
	# random line color
	t.color(int(random.uniform(0,256)),int(random.uniform(0,256)),int(random.uniform(0,256)))
	# go forward
	t.forward(sz)
	# turn around randomly
	t.left(random.uniform(-360,360))
	# write a random string from the array, with random font and size. Same color as line
	t.write(rush[int(random.uniform(0,len(rush)))], font=(fonts[int(random.uniform(0,len(fonts)))], int(random.uniform(5,31)), "normal"))
	
		### Boundary detection, to keep the turtle drawing where we can see it
	if t.xcor() > 1300:
		t.goto((-1) * int(random.uniform(250,750)), t.ycor())
		#print('x over 1000')

	if t.xcor() < -1300:
		t.goto(int(random.uniform(250,750)), t.ycor())
		#print('x under -1000')

	if t.ycor() > 900:
		t.goto(t.xcor(), (-1) * int(random.uniform(250,750)))
		#print('y over 1000')

	if t.ycor() < -900:
		t.goto(t.xcor(), int(random.uniform(250,750)))
		#print('y under -1000')

tess = turtle.Turtle()
tess.speed(0)

# Go for 500 times.
for i in range(500):

	# make the next line's length randomized
	size = random.uniform(1,150)

	# call the line draw utility
	draw_multicolor_line_word(tess, size)

# exit to main GUI loop once done
wn.mainloop()
