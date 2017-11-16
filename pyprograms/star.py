# Kell Larson, CPSC 231
import turtle
wn = turtle.Screen()
wn.title("Star")

tess = turtle.Turtle()
tess.pensize(5)
tess.speed(0)
tess.hideturtle()
tess.penup()

tess.left(90) # Tess centers the star, 
tess.forward(140)
tess.right(90)

tess.pendown()
tess.forward(300)

for i in range(5): #draw the rest of the star
	tess.left(-144)
	tess.forward(600)

wn.mainloop()
