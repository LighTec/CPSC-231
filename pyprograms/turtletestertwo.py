import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")
# Set up the window and its attributes

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5) # Create tess and set some attributes
alex = turtle.Turtle() # Create alex
alex.shape("circle")
tess.shape("square")

tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120) # Make tess draw equilateral triangle
tess.right(180)
tess.forward(80) # Turn tess around


	# Move her away from the origin
for c in ["yellow", "red", "purple", "blue"]:
	alex.color(c)
	alex.forward(50)
	alex.left(90)

wn.mainloop()
