# -----------------------------
# The Joy and Beauty of Data
# Assignment 6: Data Visualization
# Names: Riley Roberts & Anna Jinneman
# Date: Dec 1 2017
# -----------------------------
# This program will take in the file "buildings.csv" and use information from
# that file. It will then create two different visualizations using the pandas
# module.
# -----------------------------

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

theFile = pd.read_csv("buildings.csv") #Read the file


buildingValues = theFile["Building Value"]
names = theFile["Name"]

#Create the first figure, a bar graph of the 10 most expensive campus buildings.
#For some reason we couldn't change the x axis to be building names instead of numbers. 
plt.figure("CSCI 127, Figure 1")
buildingValues.sort_values(ascending = False)[:10].plot(color='blue',kind='bar')
plt.xlabel("Building Number")
plt.ylabel("Value in Millions")
plt.title('Bar Graph of the 10 Most Expensive Buildings')


def checkHistoric(theFile):
    #this function loops through the Ys and Ns of the historic building data in the csv.
    #and keeps track of how many there are of each.
    numY=0
    numN = 0
    for i in range(len(theFile)):
        
        historic = theFile.ix[i, 'Historic Building']
        if historic == 'Y':
            numY+=1
        else:
            numN+=1
        
    return numY, numN


#Create the second figure, a pie chart comparing historic to nonhistoric buildings.
historicValues =  checkHistoric(theFile)
plt.figure("CSCI 127, Figure 2")
plt.pie(historicValues, labels = ("Historic", "Non-Historic"))
plt.title("Pie Chart of Historic VS Non-Historic Buildings")

plt.show()



