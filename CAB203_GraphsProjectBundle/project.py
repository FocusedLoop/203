import graphs
import digraphs
import csv

#remove
import os
scriptDirectory = os.path.dirname(__file__)


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
    # Evey player needs to play against or they need 2 games
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
    first = list(games)[0]
    # Check if they have 2 players in common
    for player in sorted(players):
        print(player)
        print(first)
        opponents[player] = (graphs.N(players, games, player))
        #print(opponents[player])
        #print(graphs.N(players,games, list(opponents[player])[0]))
        #print(graphs.N(players,games, list(opponents[player])[1]))
        #if not graphs.connected(graphs.NS(players,games, opponents[player]), games):
            #print(graphs.N(players, games, player))
            #print(graphs.NS(players,games, opponents[player]))
            #print(list(opponents[player])[0])
            #return False
        #if graphs.N(players,games, list(opponents[player])[0]) != graphs.N(players,games, list(opponents[player])[1]):
            #return False
    
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
    #Lecture 6
    #first_elements = {player_1 for (player_1, player_2) in games}
    #second_elements = {player_2 for (player_1, player_2) in games}
    #players = first_elements | second_elements
    #print(games)
    #games = games | { (b, a) for (a,b) in games } # makes the graph undirected
    #with open(refereecsvfilename, 'r') as csvfile:
    #    reader = csv.reader(csvfile)
    #    next(reader)
    #    rows = list(reader)
    
    #print(players)
    #row_0 = {(digraphs.arbitrary(rows[0]), v) for v in rows[0][1:]}
    #row_1 = {(digraphs.arbitrary(rows[0]), v) for v in rows[0][1:]}
    #row_2 = {(digraphs.arbitrary(rows[0]), v) for v in rows[0][1:]}
    #print(row_0)
    #row_0 = row_0 | { (b, a) for (a,b) in row_0 }
    #print('\n')
    #k, C = graphs.minColouring(rows[0], games)
    #k, C = graphs.minColouring(rows[0], row_0)
    #print(C)
    #print(digraphs.arbitrary(games))
    #print(graphs.bipartition(set(rows[0]), games))
    #print(graphs.colourClassesFromColouring(C))
    #print(graphs.pathFromTree(set(rows[0]), games, 'Joe'))
    
    #NEW CODE
    rows = {}
    with open(refereecsvfilename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows[row['Referee']] = (row['Conflict1'], row['Conflict2'], row['Conflict3'], row['Conflict4'])
    
    # Get the refs and the games seperate
    #print(rows)
    V = games.union(list(rows.keys()))
    E = set([])
    
    print(E)
    #E = E | { (b, a) for (a,b) in E } # makes the graph undirected
    #A, B = graphs.bipartition(V, E)
    #print(A)
    #print(B)
    #print(digraphs.maxMatching(A, B, E))
    #V = games.union(list(rows.keys()))
    # Get all the conflicts
    # Players refs can ref
    new_dict = {key: tuple(v for v in set().union(*rows.values()) if v not in rows[key]) for key in rows}
    # Remove refs from players can ref
    new_dict = {k: tuple(v for v in val if v != k) for k, val in new_dict.items()}
    # Remove None players
    new_dict = {key: tuple(value for value in values if value is not None) for key, values in new_dict.items()}
    #E = set([((x, y), key) for key, values in new_dict.items() for i, x in enumerate(values) for y in values[i+1:]])
    E = {((player_1, player_2), key) }
    print(valid_pairs)
    #E = E | { (b, a) for (a,b) in E } # makes the graph undirected
    
    #print('\n')
    #print(E)
    #A, B = graphs.bipartition(V, E)
    #print(A)
    #print(B)
    #print(digraphs.maxMatching(A, B, games))
    #E = - conflict
    
def gameGroups(assignedReferees):
   pass

def gameSchedule(assignedReferees, gameGroups):
   pass

def scores(p, s, c, games):
   pass

#games = { ( " Alice " , " Bob " ) , ( " Charlie " , " Bob " ) }
#games = { ( " A ", " B " ), (" B ", " C "), (" C ", " D "), (" D ", " A ") }
#games = { ( " A ", " B " ), ( " C ", " D " ) }
#games = { (0, 1), (1, 2), (2, 3), (3, 4), (4, 0) }
#games = { ( " A ", " C " ), ( " A ", " D " ), ( " B ", " C " ), ( " B ", " D ") }

#print(gamesOK(games))
refereecsvfilename = os.path.join(scriptDirectory, 'referees1.csv')
games = { ('Bob', 'Alice'), ('Joe', 'Charlie'), ('Elaine', 'Rene') }
print(referees(games, refereecsvfilename))