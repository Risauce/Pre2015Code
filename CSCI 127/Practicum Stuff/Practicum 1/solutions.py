#import turtle

#drawingTurtle = turtle.Turtle()
#drawingTurtle.width(3)
#drawingTurtle.hideturtle()


#numberSegments = int(input("Enter number of segments"))
#segmentLength = int(input("Enter length of a segment"))

def bobcat_line(t, numSeg, lenSeg):
    t.goto(0,0)
    color = "blue"
    for i in range(numSeg):
        if color == "blue":
            color = "yellow"
            t.color(color)
            t.forward(lenSeg)
        elif color == "yellow":
            color = "blue"
            t.color(color)
            t.forward(lenSeg)


#bobcat_line(drawingTurtle, numberSegments, segmentLength)


scores = [0, 31, 27, 31, 49, 21, 17, 25]

def winGames(listScores):
    wins = 0
    losses = 0
    catsInList = 0
    
    for i in listScores:
        while catsInList < (len(listScores) - 1):
            if listScores[catsInList+1] > listScores[catsInList]:
                catsInList += 2
                losses+=1
                
            elif listScores[catsInList+1] < listScores[catsInList]:
                catsInList += 2
                wins += 1
                

    return wins

def lossGames(listScores):
    wins = 0
    losses = 0
    catsInList = 0
    
    for i in listScores:
        while catsInList < (len(listScores) - 1):
            if listScores[catsInList+1] > listScores[catsInList]:
                catsInList += 2
                losses+=1
                
            elif listScores[catsInList+1] < listScores[catsInList]:
                catsInList += 2
                wins += 1
                

    return losses



wins = winGames(scores)
losses = lossGames(scores)

print("MSU has", wins, "win(s)", "and", losses, "loss(es)")












