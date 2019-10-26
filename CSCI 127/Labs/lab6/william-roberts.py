# --------------------------------------
# CSCI 127, Lab 6
# October 10, 2017
# Riley Roberts
# --------------------------------------

# Change 1: The process_season parameters include output_file 

def process_season(output_file, season, games_played, points_earned):
    output_file.write("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned) + '\n')
    output_file.write("Possible Win-Tie-Loss Records\n")
    output_file.write("-----------------------------\n")
    if games_played == 1: #POINTS_EARNED = 3*WINS + Ties + 0
        if points_earned == 3:
            output_file.write("1-0-0\n")
        if points_earned == 1:
            output_file.write("0-1-0\n")
        if points_earned == 0:
            output_file.write("0-0-1\n")
    else:
        for w in range(games_played, 0, -1):
            for t in range(games_played - w + 1):
                points = w*3
                points += t
                l = games_played - w - t
                if points == points_earned:
                    output_file.write(str(w) + '-' + str(t) + '-' + str(l) + '\n')
   
        
    print()


# --------------------------------------

# Change 2: The process_seasons parameters are input_file (e.g. "soccer-in.txt") and output_file (e.g. "soccer-out.txt")

def process_seasons(input_file, output_file):
    inFile = open(input_file, "r")
    outFile = open(output_file, "w")
    season = 0
    for line in inFile:
        season += 1
        numbersList = line.split()
        gamesPlayed = numbersList[0]
        points = numbersList[1]

        process_season(outFile, int(season), int(gamesPlayed), int(points))
    

# --------------------------------------

# Change 3: The function process_seasons is called with "soccer-in.txt" and "soccer-out.txt" 


process_seasons("soccer-in.txt", "soccer-out.txt")
