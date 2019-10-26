import pandas as pd
import matplotlib.pyplot as plt
#manually entered data
years = [2000, 2001, 2002, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
wins = [17, 21, 38, 37, 34, 34, 42, 48, 29, 26, 36, 23, 47, 51, 67, 73, 67]

#Make a long list of tuples with several different strings
warriorsDataSet = list(zip(years, wins))
print(warriorsDataSet)

#Make a data set from manually entered data
data = pd.DataFrame(data = warriorsDataSet, columns=["Year", "Wins"])
print()
print(data)

#Send the data to a csv file
data.to_csv("warriors2.csv", index = False, header = False)

#Read from CSV file
warriors = pd.read_csv('warriors2.csv', names=['Year', 'Wins'])
print(warriors)

#Sort it in Wins if need be
sortedWarriors = warriors.sort_values(['Wins'], ascending = False)
print()
print(sortedWarriors)


#PLOT IT
sortedWarriors.plot(x="Year", y="Wins", kind="bar", color="red")
plt.xlabel("Year")
plt.ylabel("Warrior's Wins")
plt.title('Line Graph of Warrior Wins')

plt.show
