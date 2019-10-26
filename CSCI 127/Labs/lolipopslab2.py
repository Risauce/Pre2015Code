# --------------------------------------
# CSCI 127, Lab 2
# September 12, 2017
# William "Riley" Roberts
# --------------------------------------

import turtle, random

border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.up()
border.goto(-300, 300)
border.down()
for side in range(4):
    border.forward(600)
    border.right(90)

lollipop = turtle.Turtle()
lollipop.color("red")
lollipop.hideturtle()
lollipop.speed(0)

stick = turtle.Turtle()
stick.color("black")
stick.width(5)
stick.hideturtle()
stick.speed(0)
stick.right(90)

""" 
Do not delete or change any of the Python statements above this line.

The next 4 statements illustrate a lollipop of radius 30 whose bottom 
is at (0,0) and a stick of length 60 whose top appears at (0, 0)
""" 
def drawLollipop():
    radius = random.randint(10, 30)
    x = random.randint(-300 + radius, 300 - radius) #Find somewhere inside the border
    y = random.randint(-300 + 2*radius, 300 - 2*radius)
    R = random.random()
    G = random.random()
    B = random.random()
                       
    lollipop.up()
    lollipop.goto(x,y)
    lollipop.down()

    stick.up()
    stick.goto(x, y)
    stick.down()
    stick.fd(radius*2)

    lollipop.color(R, G, B) #Change Colors
    lollipop.fillcolor(R, G ,B)
    
    lollipop.begin_fill()
    lollipop.circle(radius)
    lollipop.end_fill()
    


def main():
    for i in range(99):
        drawLollipop()
        



main()













