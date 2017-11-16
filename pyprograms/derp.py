import random
import turtle
import math

import tkinter.font

root = tkinter.Tk()

fonts=tkinter.font.families(root)
#print(len(fonts))

wn = turtle.Screen()
wn.colormode(255)

def draw_multicolor_line_word(t, sz):
	t.pensize(int(random.uniform(1,15)))
	t.color(int(random.uniform(0,256)),int(random.uniform(0,256)),int(random.uniform(0,256)))
	t.forward(sz)
	t.left(random.uniform(-360,360))
	t.write('DERP', font=(fonts[int(random.uniform(0,len(fonts)))], int(random.uniform(5,31)), "normal"))
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

#wn.bgcolor("lightgreen") # Set up the window and its attributes
tess = turtle.Turtle()
tess.pensize(10) # Create tess and set some attributes
tess.speed(0)
size = 25
# Size of the smallest square
for i in range(10000):

	size = random.uniform(1,150)

	draw_multicolor_line_word(tess, size)
	# Increase the size for next time
	#tess.forward(10)
	# Move tess along a little
	#tess.right(18)
	#and give her some turn
wn.mainloop()

words = ['derp', 'DERP', 'Hello world!', 'Much line', 'Very wow', 'Such random','ASDF', 'ONG!!!11!!'
,'Boop']
