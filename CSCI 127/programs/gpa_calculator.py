# Riley Roberts
# Advanced Coding, The Joy and Beauty of Computing
# Assignment 1, gpa_calculator
# Last Edited: 9/8/17
#--------------------------------------------------
# This program takes in user input about classes (grades and credits) and uses the entered
# data to output a GPA for the user. 
#--------------------------------------------------

import math, string

def numberOfClasses(): #This function asks the user for the number of classes he/she took.
    classes = False
    while(classes == False):
        try:
            courses = int(input("Enter the number of classes you are taking: "))
            classes = True
        except:
            print("That is an invalid number of classes, try again. ")

    gradeAndCredits(courses) #Then calls gradeAndCredits with the number of classes
        

def gradeAndCredits(numberClass): #This function asks for the user input about the grade and credit for each class
    listOfGrades = [] #Instanciate list variables to store values in
    listOfCredits = []
    for i in range(1, numberClass+1):
        gradeForClass = (str(input("\nEnter grade for course " + str(i) + ": " )).lower())
        listOfGrades.append(gradeForClass)
        
        creditForClass = int(input("Enter credits for course " + str(i) + ": "))
        listOfCredits.append(creditForClass)

    translate(listOfGrades, listOfCredits) #Call the Translate Function


def translate(listOfGrades, listOfCredits): #This function holds a dictionary of all the translations between letter grades and GP scores. 
    listGP = []                             #It then takes the list holding the grade values to calculate all the corresponding GP scores.
    dicGrades = {}                          #Then, it uses GP scores and the total number of credits to calculate the final GPA of the user.
    dicGrades["a"] = 4.0
    dicGrades["a-"] = 3.7
    dicGrades["b+"] = 3.3
    dicGrades["b"] = 3.0
    dicGrades["b-"] = 2.7
    dicGrades["c+"] = 2.3
    dicGrades["c"] = 2.0
    dicGrades["c-"] = 1.7
    dicGrades["d+"] = 1.3
    dicGrades["d"] = 1.0
    dicGrades["f"] = 0.0


    for i in listOfGrades:
        listGP.append(dicGrades[str(i)]) # For each letter grade in the list, add the corresponding GP into a new list

    totalCredits = 0
    for i in listOfCredits: # For each credit value in the list of all credits, add it to a total number.
        totalCredits += i

    gradeCredit = 0
    for i in range(len(listGP)):
        gradeCredit += listGP[i] * listOfCredits[int(i)] #Go through both lists, multiplying the class GP and credit together

    finalGPA = round((gradeCredit / totalCredits), 2) #Finally, divide the product of GP and credit by the total number of class credits.
        
    print("\nYour GPA is " + str(finalGPA))
    

def main():
    numberOfClasses()
   
main()
