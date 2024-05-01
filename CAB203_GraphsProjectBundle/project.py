import graphs
import digraphs
import csv


def gamesOK(games):
    #Degree, Connected
    #Distance
    #bipartition, minColouring
    #isIndependentSet
    
    #pathFromTree
    
    #Notes from chatgpt
    #N will show all the neighbours of a player
    #NS will show all the neighbours of 2 players
    #
    
    #OLD CODE
    player_database = {}
    #tutorial_6_april11 line 1 to 13, change
    #first_elements = {player_1 for (player_1, player_2) in games}
    #second_elements = {player_2 for (player_1, player_2) in games}
    #players = first_elements | second_elements
    #U, T = graphs.bipartition(players, games)
    #test = digraphs.maxMatching(players, players, games)
    #test = graphs.bipartition(players, games)
    #graphs.assertIsUndirectedGraph(players, games)
    
    #print(players)
    #print(games)
    #print(test)
    
    # V = players
    # E = games
    #graphs.connected(players, games)
    
    #graphs.isIndependentSet()
    
    #NEW CODE
    # List all the players
    first_elements = {player_1 for (player_1, player_2) in games}
    second_elements = {player_2 for (player_1, player_2) in games}
    players = first_elements | second_elements
    
    games = games | { (b, a) for (a,b) in games } # symmetrise
    
    # Find all possible neighbours of the players
    opponents = {}
    for player in sorted(players):
        opponents[player] = (graphs.N(players, games, player))
    print(opponents)
    
    #Size of games
    
    #graphs.degree(players, )
       

def referees(games, refereecsvfilename):
   pass

def gameGroups(assignedReferees):
   pass

def gameSchedule(assignedReferees, gameGroups):
   pass

def scores(p, s, c, games):
   pass

games = { ( " Alice " , " Bob " ) , ( " Charlie " , " Bob " ) }

print(gamesOK(games))