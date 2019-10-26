import turtle
import random

window = turtle.Screen()

square = turtle.Turtle()
square.speed(0)
square.hideturtle()

def drawSquare(t, R, G , B):
    square.up()
    square.goto(-200, 200)
    square.down()
    square.fillcolor(R, G, B)
    square.begin_fill()
    for i in range(4):
        square.forward(50)
        square.right(90)
    square.end_fill()

drawSquare(square, 0, 0, 0)

square.up()
square.goto(-205, 205)
square.write("Change Color")

pencil = turtle.Turtle()
pencil.hideturtle()
pencil.shape("circle")
pencil.showturtle()
pencil.down()

def drawing_controls(x, y):
    if (-200 <= x <= -150) and (150 <= y <= 200):
        R = random.random()
        G = random.random()
        B = random.random()
        pencil.color(R, G, B)
        square.color(R, G ,B)
        drawSquare(square, R, G, B)

    else:
        pencil.goto(x, y)
        

window.onclick(drawing_controls)

pencil.onrelease(pencil.goto)
