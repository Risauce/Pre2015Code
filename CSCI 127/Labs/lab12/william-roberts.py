import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------
# CSCI 127, Lab 12
# November 21, 2017
# Riley Roberts
# -----------------------------------------------------

def read_file(name):
    input_file = open(name, "r")
    number_buckets = int(input_file.readline())
    total_counties = int(input_file.readline())

    county_populations = np.zeros([total_counties], dtype="int")
    for county_number in range(total_counties):
        line = input_file.readline().split(",")
        county_populations[county_number] = int(line[1])
    county_populations.sort()
    input_file.close()

    return number_buckets, county_populations

# -----------------------------------------------------

def print_summary(averages):
    pass
    print("Population Grouping Summary")
    print("---------------------------")
    for grouping in range(len(averages)):
        print("Grouping", grouping + 1, "has a population average of",
              averages[grouping])

# -----------------------------------------------------
# Do not change anything above this line
# -----------------------------------------------------

def calculate_averages(number_buckets, county_populations):
    n = int(len(county_populations) / number_buckets)
    total = int(len(county_populations))
    averages = np.zeros([number_buckets], dtype = 'int')

    for i in range(number_buckets):
        if i == 0:
            average = int(np.average((county_populations[0:n])))
            
        elif i == 1:
            average = int(np.average((county_populations[n:2*n])))
            
        elif i == 2:
            average = int(np.average((county_populations[2*n:3*n])))
            
        elif i == 3:
            average = int(np.average((county_populations[3*n:4*n])))

        #(n - (n-1))for a more general case this could go on to infinity.. for buckets = +Real#s
            
        else:
            print('none')

        averages[i] = int(average)

    #print(averages)

    return(averages)

# -----------------------------------------------------

def graph_summary(averages):
    x = ['1', '2', '3', '4']
    plt.figure("CSCI 127, Lab 12")
    plt.title("Montana County Population Analysis")
    plt.plot(x, averages, "c--")
    plt.plot(x, averages, "bh")
    plt.xticks(x)
    plt.xlabel("County Groupings")
    plt.ylabel("County Population Average")
    plt.show()

# -----------------------------------------------------

number_buckets, county_populations = read_file("montana-counties.txt")
averages = calculate_averages(number_buckets, county_populations)
print_summary(averages)
graph_summary(averages)
