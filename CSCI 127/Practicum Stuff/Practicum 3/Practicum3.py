import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

units = ["Chemical and Biological Engineering", "Civil Engineering", "Computer Engineering", "General Engineering", "Mechanical and Industrial Engineering", "School of Computing"]

enrollments = [563, 731, 410, 210, 1463, 552]

dataset = list(zip(units, enrollments))
dataFrame = pd.DataFrame(data=dataset, columns=["Unit", "Enrollment"])



#print(dataFrame.sort_values(by=["Enrollment"]))
print(dataFrame.sort_values(by=["Enrollment"]).tail(int(len(units)-2)).head(2))


#Question 2:-----------------------------------------

class Course:
    def __init__(self, rubric, number):
        self.rubric = rubric
        self.number = number

    def __str__(self):
        return self.rubric + " " + str(self.number)


class Course_Schedule():
    def __init__(self, numClasses):
        self.numClasses = numClasses
        self.array = np.empty([numClasses], dtype = Course)
        self.numAdded = 0

    def add(self, Course):
        
        self.array[self.numAdded] = (str(Course))
        self.numAdded += 1

    def __str__(self):
        theStr = "My Schedule\n" + "-------\n" + str(self.array[0]) +'\n' + str(self.array[1])+'\n' +   str(self.array[2])
        return(theStr)
        

def main():
    my_courses = Course_Schedule(3)
    course_1 = Course("CSCI", 127)
    my_courses.add(course_1)
    course_2 = Course("M", 171)
    my_courses.add(course_2)
    course_3 = Course("WRIT", 101)
    my_courses.add(course_3)
    print(my_courses)
    

#main()



#Question 3:-----------------------------------------------------

units = ["CS", "ChBE", "Civil", "M&IE", "General", "CpE"]
enrollments = [552, 563, 731, 1463, 210, 410]
explode = (.01, .01, .01, .01, .01, .01)
colors = ("blue", "yellow", "blue", "yellow", "blue", "yellow")

plt.figure("COE Enrollment Visualization")

plt.pie(enrollments, explode=explode, labels=units,
        colors=colors, counterclock=False)
#plt.show()
