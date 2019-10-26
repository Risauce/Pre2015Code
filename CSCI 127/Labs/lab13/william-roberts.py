import numpy as np
import matplotlib.pyplot as plt
import random

# --------------------------------------

def evaluate(theCard): #This assigns ace and ten to special value cards, leaving face value cards alone.
    if (2 <= theCard % 13 <= 10):
        return theCard % 13
    elif(theCard % 13 == 1):
        return 11
    else:
        return 10

def score():
    card1 = random.randint(1,52)
    card2 = random.randint(1,52)
    while card1 == card2:
        card2 = np.random.randint(52)

    value = evaluate(card1) + evaluate(card2)
    if value == 22:
        value = 12
    return value

def generateHands(howMany):
    theArray = np.ndarray([howMany], dtype=int)
    
    for hand in range(howMany):
        theArray[hand] = score()
        
    return theArray

def handCounts(hands):
    counts = np.zeros([22], dtype=int)
    for hand in hands:
        counts[hand] += 1
    

hands = generateHands(10000)
handCounts(hands)

# --------------------------------------
x = np.arange(4, 22, 1)
plt.figure('CSCI 127, Lab 13')
plt.hist(hands, 18, normed=True, facecolor='g')  # create the histogram
plt.xticks(x)
plt.xlabel('Hand Value')
plt.ylabel('Probability')
plt.title('Histogram of BlackJack Hands')
plt.grid(True)
plt.show()


