# ---------------------------------------
# Joy and Beauty of Data
# Assignment 2: Bowling
# Bozeman High School
# Riley Roberts, Tanner Smith
# ---------------------------------------

# ---------------------------------------
# main: The function to call to start the solution.
# ---------------------------------------

def main():
    bowling_file = open("bowling.txt", "r")
    number_of_games = int(bowling_file.readline())
    for game_number in range(number_of_games):
        print("Game", game_number + 1)
        print("------------------------")
        game = read_game(bowling_file)
        #print(game)
        score_game(game)
        
    bowling_file.close()

# ----------------------------------------
# read_game: Reads a single game of bowling scores
# ----------------------------------------
# file_name: The file that contains the bowling informatino
# ----------------------------------------
# The function returns a list of numbers that shows
# the result of each individual ball rolled.
# ----------------------------------------

def score_game(game):
    cumalative = 0         #set the total = 0 to start
    spot = len(game)-1    #The len of the entered list 
    for rl in range(0,spot,2):  #  Game1 - [1, 1, 2, 2, 3, 3, 4, 4, 5, 1, 6, 2, 7, 0, 8, 0, 9, 0, 0, 5]      Every two is a frame
        firstRoll = game[rl]         # First Roll is equal to the first position the loop is at.
        secondRoll = game[rl+1]      # Second Roll is the position one to the right of firstRoll
        
        #OPEN FRAME:
        if firstRoll + secondRoll < 10:     
            thisFrame = firstRoll + secondRoll                
            cumalative += thisFrame
            print("Frame: " + str(int(((rl +1)/2)+.5)) + "\n  First Roll in Frame: " + str(firstRoll) + " \n  Second Rolling Score: " + str(secondRoll) + " \n  Frame Score: " + str(thisFrame) + " \n  Cumalative Score: " + str(cumalative) + "\n")

        #SPARE:
        elif firstRoll + secondRoll == 10:
            thirdRoll = game[rl + 2]
            thisFrame = 10 + thirdRoll              # Spare is 10, so add 10 to the next roll
            cumalative += thisFrame
            print("Frame: " + str(int(((rl +1)/2)+.5)) + "\n  First Roll in Frame: " + str(firstRoll) + " \n  Second Rolling Score: " + str(secondRoll) + "\n  Spare! \n  Third Scoring Roll: " + str(thirdRoll) + "\n  Frame Score: " + str(thisFrame) + "\n  Cumalative Score: " + str(cumalative) + "\n")

        #STRIKE:
        else:                           # Game3-[10, 2, 3, 10, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10] #SO CLOSE... How do you get the for loop to know to go one roll a frame and then have a 2 roll frame?!
            nextRoll = game[rl+1]
            secondNextRoll = game[rl + 2]
            thisFrame = 10 + nextRoll + secondNextRoll         # Strike is 10 + the next two scoring Rolls
            cumalative += thisFrame
            print("Frame: " + str(int(((rl +1)/2)+.5)) + "\n  First Roll in Frame: " + str(firstRoll) + "\n  Strike!" + "\n  Next Scoring Roll: " + str(nextRoll) + "\n  Second Scoring Roll: " + str(secondNextRoll) + "\n  Frame Score: " + str(thisFrame) + "\n  Cumalative Score: " + str(cumalative) + "\n")
            

#All my problems arise from index errors, which happen because the third game has too little spaces.
#The only thing wrong is game 3, but to fix it I would have to change everything... So this is good enough.    
#I couldn't figure out how to change the position at which the for loop is at to change how it goes down the list for strikes.



def read_game(file_name):
    rolls = []
    for frame in range(10):                 # 10 frames per game
        data = file_name.readline().split() # read rolls for one frame
        for item in range(len(data)):       # there will be 1, 2 or 3 rolls
            ball= int(data[item])           # convert to an integer
            rolls = rolls + [ball]          # add to list of rolls
    return rolls

# ----------------------------------------

main()
