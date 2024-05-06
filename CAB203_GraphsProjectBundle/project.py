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
    
    #graphs.connected(players, games)
    
    #graphs.isIndependentSet()
    
    #NEW CODE
    # List all the players
    first_elements = {player_1 for (player_1, player_2) in games}
    second_elements = {player_2 for (player_1, player_2) in games}
    players = first_elements | second_elements
    
    # Add edges to ensure graph is undirected
    games = games | { (b, a) for (a,b) in games } # symmetrise
    
    # Find all possible neighbours of the players
    # V = players
    # E = games
    # u = player
    opponents = {}
    for player in sorted(players):
        opponents[player] = (graphs.N(players, games, player))
    print(opponents)
    
    # All games have the same number of games
    opponent_size = graphs.degree(opponents, games, (list(opponents.keys()))[0])# arbitrary?
    for opponent in opponents:
        if graphs.degree(opponents, games, opponent) != opponent_size:
            return False
        opponent_size = graphs.degree(opponents, games, opponent)
    return True

def referees(games, refereecsvfilename):
    # Create a dictionary and assign the playable players to the referee (opposite of first question)
    # Spanning Tree
    # Find path
    
    # Use bipartition to divide the set of available referees into two groups such that referees
    # within the same group do not have conflicts of interest with each other
    # isIndependentSet to determine if 2 a referee is connected to a player
    
    #  Spanning Tree, Bipartion, isIndependentSet
   pass

def gameGroups(assignedReferees):
   pass

def gameSchedule(assignedReferees, gameGroups):
   pass

def scores(p, s, c, games):
   pass

games = { ( " Alice " , " Bob " ) , ( " Charlie " , " Bob " ) }
#games = { ( " A ", " B " ), (" A ", " C "), (" B ", " D "), (" C ", " D "), (" B ", " C ") }
games = { ( " A ", " B " ), ( " C ", " D " ) }
#games = { ( " A ", " C " ), ( " A ", " D " ), ( " B ", " C " ), ( " B ", " D ") }

print(gamesOK(games))