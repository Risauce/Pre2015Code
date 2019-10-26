import random, turtle
theFile = open("Crazy.txt", "w")

bob = turtle.Turtle()
window = turtle.Screen()



def object(t, lst):
    for ln in lst:
        try:
            t.goto(lst[ln], lst[ln+1])
            
            t.goto(ln,ln+1)
        #except:
            

def main(t, file):
    theList = []
    for i in range(200):
        theList.append(i + random.randint(-100, 100))
        #print(theList)
        file.write(str(theList))
    object(t, theList)


main(bob, theFile)

theFile.close()
    
