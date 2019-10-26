# -----------------------------
# The Joy and Beauty of Data
# Assignment 3: Pokedex
# Your Name: Riley Roberts
# Date: 10,4,2017
# -----------------------------
# This program uses an input file of comma separated values and uses its contents to create a full-blown pokedex of 30 of the 1st gen pokemon. It can do lots of
# things to organize the pokedex, and also allow for searching through it for specific pokemon. 

import string

def printMenu():
    print("1. Print Pokedex")
    print("2. Lookup Pokemon by Name")
    print("3. Lookup Pokemon by Number")        #List all of the options in the menu so the user can choose
    print("4. Print Number of Pokemon")
    print("5. Print Total Hit points of ALL Pokemon")
    print("6. Organize the Pokedex and print it by HP")
    print("7. Lookup Pokemon by type")
    print("8. End the Program")

def tryThis(counter, name, typ, hp, dic, i): # This function is used a lot, mainly to deal with the error that comes from trying to instanciate dic[i][3]
    #Usually doing so would crash the program, so we put it in a try and except block to get around it.
    try: #Try this, if it doesn't work try the except. Used to see if there is a second type.
        print("Number: " + str(counter) + " Name: " + name + " Type: " + typ + " and " + str(dic[i][3]) + " HP: " + hp + "\n --------")
    except:
        print("Number: " + str(counter) + " Name: " + name + " Type: " + typ + " HP: " + hp + "\n --------")

def printPokedex(dic):        #This function takes in a dict, and prints the number of each pokemon, along with type, name, and hp.
    counter = 0
    for i in dic:
        counter += 1
        name = str(dic[i][0]) #Pos of name
        typ = str(dic[i][2])  #Pos of type
        hp = str(dic[i][1])   #Pos of hp
        
        tryThis(counter, name, typ, hp, dic, i)

def lookupByName(dic, name): #This function searches for a specific value based on the entered pokemon name.
    counter = 0
    wordExist = False     #Boolean to see if the name exists in the dict at all
    
    for i in dic:
        counter += 1
        name2 = str(dic[i][0])
        typ = str(dic[i][2])
        hp = str(dic[i][1])

        if str(name) == name2: #If the name entered equals the name in any value;
            wordExist = True  #Set it to true
            tryThis(counter, name, typ, hp, dic, i)
    if wordExist == False: #If the name is never found, print this:
        print("That Pokemon name doesn't exist, try again:")
        

def lookupByNumber(dic, number):  #This function searches through a dict for the entered number, then prints its values
    counter = 0
    for i in dic: #For each key in the dict
        counter += 1
        name2 = str(dic[i][0])
        typ = str(dic[i][2])
        hp = str(dic[i][1])
        
        if counter == number:  #The counter is the key number, so if it equals the number entered, then print that value
            tryThis(counter, name2, typ, hp, dic, i)


def howManyPokemon(dic):  #Really we could just set this to print("30") but this instead puts all the keys into a list, then prints the len of that list
    number = list(dic.keys())
    print("The number of pokemon in the Pokedex is " + str(len(number)) + "\n")

def howManyHitPoints(dic): #This function prints the total number of HP in the dict
    total = 0
    for i in dic:
        hp = dic[i][1]
        total += hp
        
    print("The total amount of HP is: " + str(total) + "\n")

def organizeHP(dic):
    listOfDic = []
    greatestValue = 0
    for i in dic:
        
        HP1 = dic[i][1]
        try:
            HP2 = dic[i+1][1]
        except:
            None
            
        if HP2 > HP1:
            if HP2 > greatestValue:
                greatestValue = int(HP2)
                listOfDic.insert(0,dic[i+1])
    print(listOfDic)

def lookupByType(dic, poketype):   #This function will look through the pokedex and print all pokemon and their values of the given type.
    counter = 0
    for i in dic: #For each key in the dict
        counter += 1
        name2 = str(dic[i][0])
        typ = str(dic[i][2])
        hp = str(dic[i][1])
        
        if poketype == typ:  #If the type entered is found as the first instance of type in the dic, print
            tryThis(counter, name2, typ, hp, dic, i)

        try:
            if poketype == str(dic[i][3]): #If the type entered is found as the second instane of type then print
                tryThis(counter, name2, typ, hp, dic, i)
        except:
                None


               
# -----------------------------

def createPokedex(filename):          #Get the File and initiate a dict for it called pokedex
    pokedex = {}
    file = open(filename, "r")
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        index = int(pokelist.pop(0))
        pokedex[index] = [pokelist.pop(0)]          # name
        pokedex[index] += [int(pokelist.pop(0))]    # hit points
        pokedex[index] += [pokelist.pop(0)]         # type
        if len(pokelist) == 1:
            pokedex[index] += [pokelist.pop(0)]     # optional second type
    print (pokedex)

    return pokedex

# -----------------------------
    

def getChoice(low, high, message):  #This function takes in a low, high, then message and makes sure the entered number is legal. 
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# -----------------------------

def main(): #The main function, it takes in the users input to initalize the given function. I only modified this to allow for my extra functions.
    pokedex = createPokedex("pokedex.txt")
    choice = 0
    while choice != 8:
        printMenu()
        choice = getChoice(1, 8, "Enter a menu option: ")
        if choice == 1:    
            printPokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ")
            name = name.capitalize()
            lookupByName(pokedex, name)
        elif choice == 3:
            number = getChoice(1, 30, "Enter a Pokemon number: ")
            lookupByNumber(pokedex, number)
        elif choice == 4:
            howManyPokemon(pokedex)
        elif choice == 5:
            howManyHitPoints(pokedex)
        elif choice == 6:
            organizeHP(pokedex)
        elif choice == 7:
            poketype = input("Enter a Pokemon type: ")
            lookupByType(pokedex, poketype)
    print("Thank you.  Goodbye!")

# -----------------------------

main()
