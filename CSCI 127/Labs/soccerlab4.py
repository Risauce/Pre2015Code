import random
# --------------------------------------
# CSCI 127, Lab 4
# September 26, 2017
# Riley Roberts
# --------------------------------------
def process_season(season, games_played, points_earned):
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")
    if games_played == 1: #POINTS_EARNED = 3*WINS + Ties + 0
        if points_earned == 3:
            print("1-0-0")
        if points_earned == 1:
            print("0-1-0")
        if points_earned == 0:
            print("0-0-1")
    else:
        for w in range(games_played, 0, -1):
            for t in range(games_played - w + 1):
                points = w*3
                points += t
                l = games_played - w - t
                if points == points_earned:
                    print(str(w) + '-' + str(t) + '-' + str(l))
   
        
    print()
# --------------------------------------

def process_seasons(seasons):
    for i in range(len(seasons)):
        numGames = seasons[i][0]
        points = seasons[i][1]
        process_season(i+1, numGames, points)
        

# --------------------------------------

# format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
soccer_seasons = [[1, 3], [1, 1], [1, 0], [29, 50]]

process_seasons(soccer_seasons)
