msu = {}
msu[(3, 1, 2017)] = "win"   # Idaho State
msu[(3, 3, 2017)] = "win"   # Weber State
msu[(3, 8, 2017)] = "win"   # Weber State
msu[(3, 10, 2017)] = "win"  # Eastern Washington
msu[(3, 11, 2017)] = "win"  # Idaho State
msu[(3, 18, 2017)] = "loss" # Washington


def determine_wins(dic):
    count = 0
    for key in dic:
        if dic[key] == "win":
            count += 1

    return count


#print(determine_wins(msu))

#Class: A user-created object that allows for custom methods and objects to be manipulated to help solve a problem.
#Object/Intance: An instance of a class that holds the instance variables defined by that class.
#Method: A user defined funciton that an object of a class may call. 
#Constructor: __init__ The special method that instanciates the variables of a class object.
#Reader/Writer: A reader method returns an instance variable of a class. A writer changes an instance variable.
#Encapsulation: How OOP works, it keeps code that may be extremely complex very readable and easy to the user. 
#Inheritence: The mechanism by which an object acquires the some/all properties of another object. class platypus(mammal)
#Polymorphism: Polymorphism means to process objects differently based on their data type. One method, mupltiple implementations.


class Person():
    def __init__(self, name, lastName, height):
        self.name = name
        self.last = lastName
        self.height = height

    def getName(self):
        return self.name

    def getHeight(self):
        return self.height

    def changeHeight(self, entered):
        self.height = entered

##abe = Person("abe", "harrison", 60)
##print(abe.getName())
##
##abe.changeHeight(72)
##print(abe.getHeight())
        
#--------------------------

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Rectangle():
    def __init__(self, Point, height, width):
        self.x = Point.getX
        self.y = Point.getY
        self.height = height
        self.width = width

    def draw(self):
        pass


r = Rectangle(Point(4,5), 6, 5)



#------------------------
class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)

class Game():
    def __init__(self, team1, score1, team2, score2, Date):
        self.team1 = team1
        self.score1 = score1
        self.team2 = team2
        self.score2 = score2
        self.date = Date

    def __str__(self):
        if self.score1 > self.score2:
            theStr = (self.team1 + " beat " + self.team2 + " on " + str(self.date) + ": " + str(self.score1) + " to " + str(self.score2))
        else:
            theStr = (self.team2 + " beat " + self.team1 + " on " + str(self.date) + ": " + str(self.score2) + " to " + str(self.score1))

        return theStr


championship = Game("Montana State", 62, "Idaho State", 56, Date(3, 11, 2017))
print(championship)

ncaa = Game("Montana State", 63, "Washington", 91, Date(3, 18, 2018))
print(ncaa)


