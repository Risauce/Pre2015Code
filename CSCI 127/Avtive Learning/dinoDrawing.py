import turtle

drawer = turtle.Turtle()
theFile = open("mystery.txt", "r")

def dino(theFile, t):
    t.hideturtle()
    for i in theFile:
        value = i.split()
        if str(value[0]) == "DOWN":
            t.down()

        elif str(value[0]) == "UP":
            t.up()

        else:
            t.goto(int(value[0]), int(value[1]))
    theFile.close()


        
dino(theFile, drawer)
            
