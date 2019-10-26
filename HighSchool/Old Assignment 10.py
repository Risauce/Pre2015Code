#Riley Roberts
#CSCI Assignment 10
#12/18/2014
#This program takes a multiply recursive function and draws it over and over
#to make a cool 'spiky wheel' shape. 

import turtle, random


a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()                     #Making all the turtles
e = turtle.Turtle()
f = turtle.Turtle()

wn = turtle.Screen()                    #Screen
wn.tracer(0)                           #Turn on tracer if you don't want to wait 
a.shape("turtle")
b.shape("turtle")
c.shape("turtle")
d.shape("turtle")
e.shape("turtle")                       #Turtles are turtle shaped :D
f.shape("turtle") 

a.speed(0)
b.speed(0)
c.speed(0)
d.speed(0)
e.speed(0)                              #Speeds
f.speed(0)

a.penup()
b.penup()
c.penup()
d.up()                                 #All pens up
e.up()
f.up()

a.goto(-200, 250)
b.goto(-200, 0)                        #Their starting positions
c.goto(-200, -250)
d.goto(200, 250)
e.goto(200, 0)
f.goto(200, -250)

d.setheading(180)
e.setheading(180)                        #Turtles on right look inward
f.setheading(180)

def recursiveObject(length, t):
    t.pendown() 
    if length > 20:
        t.tilt(40) 
        t.forward(length/2)
        t.right(5)
        t.forward(length/2)
        recursiveObject(length-15,t)     #The super awesome recursive line with 'sharp' points
        R = random.random()
        B = random.random()
        G = random.random()              #Random colors
        t.color(R, B, G) 
        t.left(length/2)                #Can be 3
        recursiveObject(length-20,t)
        t.backward(length/2)
        recursiveObject(length-15, t)


def myDrawing(length, t, levels):
    for i in range(51):
        if levels <= 7:
            recursiveObject(length, t)    #This function calls the recursive shape
            levels = levels - 1           #When levels are lower, makes different shapes
        elif levels <= 5:                   
            recursiveObject(length-2, t)
            levels = levels - 1
        else:
            recursiveObject(length-4, t)

    t.ht() 
         

myDrawing(70, a, 8)
myDrawing(70, b, 8)
myDrawing(70, c, 8)                       #All turtles are called!
myDrawing(70, d, 8)
myDrawing(70, e, 8)
myDrawing(70, f, 8) 
