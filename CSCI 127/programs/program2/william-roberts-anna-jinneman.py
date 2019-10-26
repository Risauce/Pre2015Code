#----------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 2: Three Card Poker 
# Riley Roberts, Anna Jinneman
# Last Modified: September 30, 2017 
# ---------------------------------------
# This program takes an input file that consists of cards from a standard 52 card deck.
# It creates 3 card hands and then evaluates those hands to see how they score in a game of Poker
# It also does not output anything into the IDLE environment, only into a text file called pokerOut.txt
# ---------------------------------------
import random, math, string, os


os.remove("poker.out") #Remove any file from subsequent uses of this program (ensures that the outputs don't compound)
def print_hand(theList, outFile): #This function takes in a list and output file and prints the card values in that file
    output = open(outFile, "a")

    output.write("Poker Hand \n -------")
    for i in range(len(theList)):
        card = ("\nCard " + str(i+1) + ": " + str(theList[i][0]).capitalize() + ' of ' + str(theList[i][1]).capitalize())
        output.write(card)

#-----------------------------------------------------------
def three_of_a_kind(card1Rank, card2Rank, card3Rank):
    if card1Rank == card2Rank and card1Rank == card3Rank:
        return True

def flush(card1Suit, card2Suit, card3Suit):
    if card1Suit == card2Suit and card1Suit == card3Suit:
        return True

def two_of_a_kind(card1Rank, card2Rank, card3Rank):
    if card1Rank == card2Rank or card1Rank == card3Rank or card2Rank == card3Rank:
        return True
#----------------------------------------------------------


def evaluate(theList, outFile): # This function takes in a list of cards and calculates the hand's value.
    output = open(outFile, "a")
#The separate card parts are certain positions in the list:
#------------------------------
    card1Rank = theList[0][0] 
    card2Rank = theList[1][0]
    card3Rank = theList[2][0]

    card1Suit = theList[0][1]
    card2Suit = theList[1][1]
    card3Suit = theList[2][1]
#------------------------------
#The algorithm that puts out hand values:
    if three_of_a_kind(card1Rank, card2Rank, card3Rank) == True:
        output.write("\n\nPoker Hand Evaluation: THREE OF A KIND\n\n")
        
    elif flush(card1Suit, card2Suit, card3Suit) == True:
        output.write("\n\nPoker Hand Evaluation: FLUSH\n\n")
        
    elif two_of_a_kind(card1Rank, card2Rank, card3Rank) == True:
        output.write("\n\nPoker Hand Evaluation: TWO OF A KIND\n\n")
    else:
        output.write("\n\nPoker Hand Evaluation: NOTHING\n\n")

    output.close()
    

# --------------------------------------
# Do not change anything below this line
# --------------------------------------


def main(input_file, output_file, cards_in_hand):    
    poker_input = open(input_file, "r")

    for hand in poker_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([hand[0], hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list, output_file)
        evaluate(hand_as_list, output_file)

    poker_input.close()
        

# --------------------------------------

main("poker.in", "poker.out", 3)
