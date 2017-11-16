import turtle
def draw_multicolor_poly(t, sz):
	for i in ["red", "purple", "black", "blue", "grey", "orange"]:
		t.color(i)
		t.forward(sz) #draw a multicolor abomination
		t.left(60)

def draw_square(size, turtle):
	turtle.penup() #move to new corner
	turtle.left(180)
	turtle.forward(10)
	turtle.left(90)
	turtle.forward(10)
	turtle.left(180)
	turtle.pendown()
	for i in range(4): #actually draw the circle
		turtle.forward(size)
		turtle.right(90)
	turtle.right(90) # 

wn = turtle.Screen()
#wn.bgcolor("lightgreen") # Set up the window and its attributes
tess = turtle.Turtle()
tess.hideturtle() # I personally think a hidden turtle looks better
tess.pensize(3) # Create tess and set some attributes
tess.speed(0)
size = 20 # base size of square
# Size of the smallest square
for i in range(4): # 4 times
	draw_square(size, tess) # draw it
	size = size + 20 # then increase square size

wn.mainloop()
