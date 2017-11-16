import turtle
def draw_multicolor_square(t, sz):
	for i in ["red", "purple", "black", "blue", "grey", "orange"]:
		t.color(i)
		t.forward(sz)
		t.left(60)

wn = turtle.Screen()
wn.bgcolor("lightgreen") # Set up the window and its attributes
tess = turtle.Turtle()
tess.pensize(3) # Create tess and set some attributes
tess.speed(0)
size = 5
# Size of the smallest square
for i in range(500):
	draw_multicolor_square(tess, size)
	size = size + 1
	# Increase the size for next time
	tess.forward(10)
	# Move tess along a little
	tess.right(18)
	#and give her some turn
wn.mainloop()
