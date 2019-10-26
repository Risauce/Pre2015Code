import turtle
import random


window = turtle.Screen()  #Make the Window
window.screensize(300, 300)
height = window.screensize()[0]
width = window.screensize()[1]

drawer = turtle.Turtle() #Make the turtle
drawer.speed(0) #Speed=instant

#def check (turtle):
    #if (-width+50 < drawer.xcor() < width-50 and -height+50 < drawer.ycor() < height-50):

#if (((-width) + 35) < drawer.xcor() and drawer.xcor() < ((width) - 35) and ((-height) + 35) < drawer.ycor() and drawer.ycor() < ((height) - 35)):

def east():                #Turn turtle right
    drawer.right(90)
    

def north():                    #Turtle goes forward
    global width, height
    if (-width+50 < drawer.xcor() < width-50 and -height+50 < drawer.ycor() < height-50):
        drawer.forward(50)
    else:
        print("nope")
        drawer.backward(50)

def west():                  #Turn turtle left
    drawer.left(90)
  

def south():                  #Turtle Go backwards
    global width, height
    if (((-width) + 35) < drawer.xcor() and drawer.xcor() < ((width) - 35) and ((-height) + 35) < drawer.ycor() and drawer.ycor() < ((height) - 35)):
        drawer.backward(50)
    else:
        print("nope")
        drawer.forward(50)

def turn45Right():                #Turn right 45 degrees
    drawer.right(45)
    

def turn45Left():             #Turn left 45 degrees,
    drawer.left(45)

def changeColor():        #Change to random color
    R = random.random()
    G = random.random()
    B = random.random()
    drawer.color(R, G, B)
    


def somethingCrazy():
    randomNumber1 = random.randint(1,49)
    randomNumber2 = random.randint(1,49)
    randomNumber3 = random.randint(1, 11)
    randomNumber4 = random.randint(10, 100)
    randomNumber5 = random.randint(1,5)
    
    while(True):
        drawer.forward(randomNumber1)
        for i in range(randomNumber3):
            drawer.left(randomNumber2)
            drawer.forward(randomNumber2)
            drawer.right(randomNumber1)
            drawer.forward(randomNumber2)
        drawer.goto(0,0)
        drawer.pensize(randomNumber5)
        drawer.right(randomNumber4)
        drawer.backward(randomNumber4)
        for i in range(randomNumber3):
            somethingCrazy()
        

window.onkey(east, "Right")   #On the key press, call the function of corresponding arrow
window.onkey(north, "Up")
window.onkey(west, "Left")
window.onkey(south, "Down")
window.onkey(turn45Right, "r")
window.onkey(turn45Right, "R")
window.onkey(turn45Right, "Next")
window.onkey(turn45Left, "e")
window.onkey(somethingCrazy, "BackSpace")
window.onkey(changeColor, "space")
window.listen()

window.exitonclick()           #Exit the program on clicking the screen

