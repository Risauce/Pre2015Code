#-------------------------------------
# Riley Roberts, Nikolas Torgerson
# JBD, Assignment 6, Weather Assignment
# This program takes a large csv file that holds data about weather and displays it to be easily deciphered.
#-------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import pandas

weather = pandas.read_csv("weather.csv") #Read the csv file

#This function finds the hottest mean temperature, and uses it's position to print out a string containing max, mean, and min temps of that day
def hot_mean():
    print("Dates with hottest mean temperature")
    print("-----------------------------------")
    hottestTemp = weather["Mean TemperatureF"].max()
    print("         date  max_temp  mean_temp  min_temp")
    for i in range(len(weather)):#Loop through the file and find the hottestTemp's position
        if weather.ix[i, "Mean TemperatureF"] == hottestTemp:
            print(str(i)+" "+str(weather.ix[i, 0])+"\t    "+str(weather.ix[i, 1])+"\t\t"+str(weather.ix[i, 2])+"\t  "+str(weather.ix[i, 3]))

#This function finds the coldest mean temperature, and uses it's position to print out a string containing max, mean, and min temps of that day
def cold_mean():
    print("Dates with coldest mean temperature")
    print("-----------------------------------")
    coldestTemp = weather["Mean TemperatureF"].min()
    print("         date  max_temp  mean_temp  min_temp")
    for i in range(len(weather)): #Loop through the file and find the coldestTemp's position
        if weather.ix[i, "Mean TemperatureF"] == coldestTemp:
            print(str(i)+" "+str(weather.ix[i, 0])+"\t    "+str(weather.ix[i, 1])+"\t\t"+str(weather.ix[i, 2])+"\t  "+str(weather.ix[i, 3]))

#This function loops through the event section of the csv file and counts how many rainy days there are
def daysRain():
    rainyDays = 0
    for event in weather[" Events"]:
        if "Rain" in str(event):
            rainyDays += 1
    print("\nThe number of days with rain: " + str(rainyDays))

#This funtion takes the Max and Min temps from the csv file and graphs them on the same plot!
def plot():
    weather.columns = ["Date", "Max_Temp", "Mean_Temp", "Min_Temp","5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
    weather.plot(x="Date", y="Max_Temp", kind="line", color="red", figsize=(12,6))
    weather.Min_Temp.plot(legend=True, color="blue")

    plt.title("Temperature Extremes")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.show()

#Start -------------------------
def main():
    hot_mean()
    cold_mean()
    daysRain()
    plot()
#-------------------------------
main()
