# --------------------------------------
# CSCI 127, Lab 3
# September 19, 2017
# Riley Roberts
# --------------------------------------
import string

def count_vowels(sentence):
    count = 0
    count += sentence.count("i")
    count += sentence.count("e")
    count += sentence.count("o")
    count += sentence.count("u")
    #count += sentence.count("y") #Y ISNT A VOWEL??!
    count += sentence.count("a")
    return count

def count_vowels_iterative(sentence):
    count = 0
    vowels = "aeoui"
    for i in sentence:
        if i in vowels:
            count += 1
    return count
        

def count_vowels_recursive(sentence):
    count = 0
    vowels = "aeoui"
    
    if len(sentence) == 1:
        if sentence[0] in vowels:
            return 1
        return 0

    else:
        if sentence[0] in vowels:
            count = 1 + count_vowels_recursive(sentence[1:])
            return count
        else:
            count = count_vowels_recursive(sentence[1:])
            return count
        

        

        

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence to evaluate: ")
        sentence = sentence.lower()     # convert to lowercase
        print()
        print("Number of vowels using count     =", count_vowels(sentence))
        print("Number of vowels using iteration =", count_vowels_iterative(sentence))
        print("Number of vowels using recursion =", count_vowels_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
