# -----------------------------------------------------
# CSCI 127, Lab 8
# October 24, 2017
# Riley Roberts
# -----------------------------------------------------
class Contact:

    def __init__(self, firstName, lastName, number):
        self.firstName = firstName
        self.lastName = lastName
        self.title = 0
        self.number = number

    def set_first_name(self, entered):
        self.firstName = entered

    def set_title(self, entered):
        self.title = entered

    def get_cell_number(self):
        return self.number

    def get_area_code(self):
        thing = self.number.split("-")
        code = thing[0]
        return code

    def __str__(self):
        if self.title == 0:
            result = (str(self.firstName) + " " + str(self.lastName)  + str(self.number).rjust(40 - len(self.firstName + self.lastName)))

        else:
            result = (str(self.title) + " " + str(self.firstName) + " " + str(self.lastName)  + str(self.number).rjust(39 - len(self.firstName + self.lastName + self.title)))
        return result

# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        print(person)
    print("-----------\n")

# -----------------------------------------------------

def main():
    champ = Contact("???", "Bobcat", "406-994-0000")
    president = Contact("Waded", "Cruzado", "406-994-CATS")
    professor = Contact("John", "Paxton", "406-994-4780")

    contacts = [champ, president, professor]

    print_directory(contacts)

    champ.set_first_name("Champ")
    president.set_title("President")
    professor.set_title("Professor")

    print_directory(contacts)

    print("The area code for cell number", champ.get_cell_number(), "is", \
           champ.get_area_code())

# -----------------------------------------------------

main()
