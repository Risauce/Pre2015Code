#Question 1:

stranger_things = {}
stranger_things["The Vanishing of Will Byers"] = "The Duffer Brothers"
stranger_things["The Weirdo on Maple Street"] = "The Duffer Brothers"
stranger_things["Holly, Jolly"] = "Shawn Levy"
stranger_things["The Body"] = "Shawn Levy"
stranger_things["The Flea and the Acrobat"] = "The Duffer Brothers"
stranger_things["The Monster"] = "The Duffer Brothers"
stranger_things["The Bathtub"] = "The Duffer Brothers"
stranger_things["The Upside Down"] = "The Duffer Brothers"

def episodes_directed(dic, director):
    count = 0
    for episode in dic:
        if dic[episode] == director:
            count += 1
    print(director + " directed " + str(count) + " episodes.")

    

#episodes_directed(stranger_things, "The Duffer Brothers")
#episodes_directed(stranger_things, "Shawn Levy")
#episodes_directed(stranger_things, "Kerri Cobb")

#Question 2:

class Series:
    def __init__(self, title, director, numSeasons, numEpisodes):
        self.title = title
        self.director = director
        self.seasons = numSeasons
        self.episodes = numEpisodes

    def addSeason(self):
        self.seasons += 1

    def addEpisodes(self,num):
        self.episodes += num

    def __str__(self):
        theStr = (self.title + " has aired " + str(self.episodes) + " episodes over " + str(self.seasons) + " seasons.")
        return theStr

stranger_things = Series("Stranger Things", "The Duffer Brothers", 1, 8)
#print(stranger_things)
stranger_things.addSeason() # here comes the next season
stranger_things.addEpisodes(9) # there are now 9 more episodes
#print(stranger_things)


#Question 3:

#a __init__()

#b class Runner(Athlete):

#c john = Runner(5, 2, 1)
# john is the instance of Runner, while 5 may be an instance variable defining something about him

#d a reader method just returns an instance variable, while a writer method may change an instance variable

#e def __pow__











