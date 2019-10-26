# -------------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 4: Advising System
# Riley Roberts, Anna Jinneman
# Last Modified: October 19th, 2017
# -------------------------------------------------
# This program will use classes to help students manage and
# store dat on their major. It will also provide a helpful message
# if they need help with their major or math.
# -------------------------------------------------


class Generic_Major:    #Creates the general class for other classes to be related to.

    def __init__(self, firstName, lastName):    #Initializes values such as name and major.
       self.first = firstName.capitalize()
       self.last = lastName.capitalize()
       self.major = "Generic"
       self.major_troubles = False  #Sets initial major troubles to False.
       self.math_troubles = False   #Sets initial math troubles to False.

    def get_first_name(self):   #Returns first name.
        return str(self.first)

    def get_last_name(self):    #Returns last name.
        return str(self.last)

    def get_major(self):    #Returns major.
        return str(self.major)

    def get_major_troubles(self):   #Returns major troubles.
        return self.major_troubles
    
    def get_math_troubles(self):    #Returns math troubles.
        return self.math_troubles

    def major_advising(self):   #Will print advising message for majors if the boolean is set to True.
        if self.major_troubles == True:
            print("Because you are having troubles with your major: \n --> visit your professor during office hours \n --> visit your academic advisor")
    def math_advising(self):    #Will print advising message for math if the boolean is set to True.
        if self.math_troubles == True:
            print("Because you are having troubles with math: \n --> visit the Math Learning Center in Wilson 1-112")

    def set_major_troubles(self, thing):    #Will set if major trouble is True.
        self.major_troubles = thing

    def set_math_troubles(self, thing): #Will set if math trouble is True.
        self.math_troubles = thing
 
# -------------------------------------------------
class CLS_Major(Generic_Major): #Creates class specifically for CLS majors.

    def __init__(self, firstName, lastName):    #Initializes values such as name and major.
        self.first = firstName.capitalize()
        self.last = lastName.capitalize()
        self.major = "College of Letters and Sciences"
        self.major_troubles = False
        self.math_troubles = False

    def major_advising(self):   #Will print advising message for majors if the boolean is set to True.
        if self.major_troubles == True:
            print("Because you are having troubles with your major: \n --> visit your professor during office hours \n --> visit your academic advisor")
    def math_advising(self):    #Will print advising message for math if the boolean is set to True.
        if self.math_troubles == True:
            print("Because you are having troubles with math: \n --> visit the Math Learning Center in Wilson 1-112")

# -------------------------------------------------
class COE_Major(Generic_Major): #Creates class specifically for COE majors.

    def __init__(self, firstName, lastName):    #Initializes values such as name and major.
        self.first = firstName.capitalize()
        self.last = lastName.capitalize()
        self.major = "College of Engineering"
        self.major_troubles = False
        self.math_troubles = False

    def major_advising(self):   #Will print advising message for majors if the boolean is set to True.
        if self.major_troubles == True:
            print("Because you are having troubles with your major: \n --> visit the EMPower Student Center in Roberts 313 \n --> visit your professor during office hours \n --> visit your academic advisor")
    def math_advising(self):    #Will print advising message for math if the boolean is set to True.
        if self.math_troubles == True:
            print("Because you are having troubles with math: \n --> visit the Math Learning Center in Wilson 1-112")

# -------------------------------------------------
class Computer_Engineering_Major(COE_Major):    #Creates class specifically for Computer Engineering majors.

    def __init__(self, firstName, lastName):    #Initializes values such as name and major.
        self.first = firstName.capitalize()
        self.last = lastName.capitalize()
        self.major = "Computer Engineering"
        self.major_troubles = False
        self.math_troubles = False

# -------------------------------------------------
class Physics_Major(CLS_Major): #Creates class specifically for Physics majors.
    
    def __init__(self, firstName, lastName):    #Initializes values such as name and major.
        self.first = firstName.capitalize()
        self.last = lastName.capitalize()
        self.major = "Physics"
        self.major_troubles = False
        self.math_troubles = False

    def major_advising(self):   #Will print advising message for majors if the boolean is set to True.
        if self.major_troubles == True:
            print("Because you are having troubles with your major: \n --> visit the Physics Learning Center in Barnard 230 \n --> visit your professor during office hours \n --> visit your academic advisor")
    def math_advising(self):    #Will print advising message for math if the boolean is set to True.
        if self.math_troubles == True:
            print("Because you are having troubles with math: \n --> visit the Math Learning Center in Wilson 1-112")

# -------------------------------------------------
class Computer_Science_Major(COE_Major):    #Creates class specifically for Computer Science majors.

    def __init__(self, firstName, lastName):    #Initializes values such as name and major.
        self.first = firstName.capitalize()
        self.last = lastName.capitalize()
        self.major = "Computer Science"
        self.major_troubles = False
        self.math_troubles = False

    def major_advising(self):   #Will print advising message for majors if the boolean is set to True.
        if self.major_troubles == True:
            print("Because you are having troubles with your major: \n --> visit the CS Studend Success Center in Barnard Hall 259 \n --> visit a CS professional advisor in Barnard Hall 357 \n --> visit the EMPower Student Center in Roberts 313 \n --> visit your professor during office hours \n --> visit your academic advisor")
    def math_advising(self):    #Will print advising message for math if the boolean is set to True.
        if self.math_troubles == True:
            print("Because you are having troubles with math: \n --> visit the Math Learning Center in Wilson 1-112")



# -------------------------------------------------
# Do not change anything below this line
# -------------------------------------------------

def advise(student):
    print("Student:", student.get_first_name(), student.get_last_name())
    print("Major: " + student.get_major() + ", Major Troubles: " +
          str(student.get_major_troubles()) + ", Math Troubles: " +
          str(student.get_math_troubles()))
    print()
    if not student.get_math_troubles() and not student.get_major_troubles():
        print("No advising is necessary.  Keep up the good work!")
    else:
        student.major_advising()
        student.math_advising()
    print("------------------------------")

# -------------------------------------------------

def process(student):
    advise(student)
    student.set_major_troubles(True)
    student.set_math_troubles(True)
    advise(student)

# -------------------------------------------------

def main():

    # Every student has a major, even if it is "undeclared"
    msu_student = Generic_Major("jalen", "nelson")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

    # A CLS (College of Letters and Science) major is a subclass of a Generic major
    msu_student = CLS_Major("emma", "phillips")
    process(msu_student)

    # A COE (College of Engineering) major is a subclass of a Generic major
    msu_student = COE_Major("camden", "miller")
    process(msu_student)

    # A Computer Engineering major is a subclass of a COE major
    msu_student = Computer_Engineering_Major("gabriel", "smith")
    process(msu_student)

    # A Physics major is a subclass of a CLS major
    msu_student = Physics_Major("lena", "hamilton")
    process(msu_student)

    # A Computer Science major is a subclass of a COE major
    msu_student = Computer_Science_Major("halley", "jones")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

# -------------------------------------------------

main()


