# -----------------------------
# The Joy and Beauty of Data
# Assignment 5: Batters
# Names: Riley Roberts & Anna Jinneman
# Date: November 21st 2017
# -----------------------------
# This program will take in the .txt file "batting.txt" and then will use information from the
# file by opening and reading it. With the information, the program then creates a numpy array 
# and adds the values of the batter to the array. Using classes and subclasses, the program will
# then generate a string to print. After the original values are printed, the program will then
# loop through the .txt file again and replace the hits, bats and average of the original statement.
# -----------------------------

import numpy as np

class Person():
    def __init__(self, first, last):    #Instanciates first and last names of a person
        self.first_name = first
        self.last_name = last
        
    def get_first(self):
        return str(self.first_name)

    def get_last(self):
        return str(self.last_name)

class Batter(Person):
        
    def __init__(self, first, last, pos):   #Instanciates position as well as pulling information from class Person
        Person.__init__(self, first, last)
        self.position = pos
        self.atBats = 0
        self.hits = 0
        self.bAverage = 0.0

    def __str__(self):
        return (str(self.first_name) + " " + str(self.last_name) + '(' + str(self.position.strip("\n")) + ')').ljust(25) + str(format(self.bAverage, '.3f')) + ' (' + str(self.hits) + ' for ' + str(self.atBats) + ')'
    
    def __repr__(self): #Needed for showing the name of the object inststead of it's location
        return (str(self.first_name) + " " + str(self.last_name) + '(' + str(self.position.strip("\n")) + ')').ljust(25) + str(format(self.bAverage, '.3f')) + ' (' + str(self.hits) + ' for ' + str(self.atBats) + ')'

    def updateHits(self, num):
        self.hits += num

    def updateBats(self, num):
        self.atBats += num

    def updateAverage(self):
        self.bAverage = self.hits / self.atBats

class All_Batters():
    def __init__(self, batters):
        self.batters = batters

def printStuff(people):
    print("\nPlayer" + ("Batting Average").rjust(40 - len("Player")) + "\n----------------------------------------")
    print(str(people[0]).strip("(")   
         + "\n" + str(people[1])
         + "\n" + str(people[2])
         + "\n" + str(people[3])
         + "\n" + str(people[4]))

#-------------------------

def main():
    
    theFile = open("batting.txt", "r")
    counter = 0
    n = int(theFile.readline()) #Reads the first line of the .txt file
    people = np.ndarray(shape=(n), dtype=Person)    #Creates an array with (n) number of spots for people

    
    for player in range(n):
        line = theFile.readline().split(",")
        
        people[player] = ((Batter(line[0], line[1], line[2])))  #Adds player to the array and then to the Batter Class where it can be used

        batterArray = All_Batters(people)


    printStuff(people) #Print first n players

    #This for loop goes through each player and collects only their batting values. 
    for i in people:
        theFile = open("batting.txt", "r") #We had to reset the index on each run through.
        
        for a in range(n+1): #Skip the first 5
            skipLines = theFile.readline().split(",")
            continue;
        
        for x in theFile:
            line = x.strip().split(',')
            
            if line[0] == i.get_first(): #Each player updates its own values. 
                i.updateBats(int(line[3]))
                i.updateHits(int(line[4]))
                i.updateAverage()

        theFile.close()

                
    printStuff(people) #Print after first n

    
   
#-------------------------
main()


