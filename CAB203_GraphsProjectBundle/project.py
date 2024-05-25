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
        #print(player)
        #print(first)
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
    
    #NEW CODE
    rows = {}
    with open(refereecsvfilename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows[row['Referee']] = (row['Conflict1'], row['Conflict2'], row['Conflict3'], row['Conflict4'])
    
    #rows = {key: tuple(filter(lambda x: x is not None, value)) for key, value in rows.items()}
    # Get the refs and the games seperate
    #print(rows)
    V = games.union(list(rows.keys()))
    E = set()
    #E = {((player_1, player_2), key) }
    # get all the players
    first_elements = {player_1 for (player_1, player_2) in games}
    second_elements = {player_2 for (player_1, player_2) in games}
    players = first_elements | second_elements
    #print(games)
    #print(players)
    #print(rows)
    #print(V)
    
    games_list = list(games)
    referees = list(rows.keys())
    #print(referees)
    for game in range(len(games_list)):
        for conflicts in rows.values():
            #print(conflicts)
            for conflict in range(len(conflicts)):
                #print(conflict)
                if list(conflicts)[conflict] not in games_list[game]:
                    for referee in range(len(referees)):
                        E.add((games_list[game], referees[referee]))
                        E.add((referees[referee], games_list[game]))
    #print(E)
    A, B = graphs.bipartition(V, E)
    #print(A)
    #print(B)
    matched_games = digraphs.maxMatching(A, B, E)
    print(matched_games)
    matched_games_dict = {}
    for match in matched_games:
        if isinstance(match[0], tuple):
            # When the first element is a game pair
            game_pair, referee = match
        else:
            # When the first element is a referee
            referee, game_pair = match

            matched_games_dict[game_pair] = referee

    
    #print(matched_games_dict)

    return matched_games_dict
    
    
    #print(E)
    #E = E | { (b, a) for (a,b) in E } # makes the graph undirected
    #A, B = graphs.bipartition(V, E)
    #print(A)
    #print(B)
    #print(digraphs.maxMatching(A, B, E))
    #V = games.union(list(rows.keys()))
    # Get all the conflicts
    # Players refs can ref
    #new_dict = {key: tuple(v for v in set().union(*rows.values()) if v not in rows[key]) for key in rows}
    # Remove refs from players can ref
    #new_dict = {k: tuple(v for v in val if v != k) for k, val in new_dict.items()}
    # Remove None players
    #new_dict = {key: tuple(value for value in values if value is not None) for key, values in new_dict.items()}
    #E = set([((x, y), key) for key, values in new_dict.items() for i, x in enumerate(values) for y in values[i+1:]])
    #E = {((player_1, player_2), key) }
    #print(valid_pairs)
    #E = E | { (b, a) for (a,b) in E } # makes the graph undirected
    
    #print('\n')
    #print(E)
    #A, B = graphs.bipartition(V, E)
    #print(A)
    #print(B)
    #print(digraphs.maxMatching(A, B, games))
    #E = - conflict
    
def gameGroups(assignedReferees):
    
    
    #games = list(V)
    #print(games)
    #for game in games:
    #    for player in range(games:
    #    for player in range(i + 1, len(pairs)):
    #        # Check if a player exists in the other game
    #        if assignedReferees[games[player]] == assignedReferees[games[player + 1]]:
    #            # Make the edges undicted
    #            E.add((games[player], games[player + 1]))
    #            E.add((games[player + 1], games[player]))
            # Check if the games are the same
    #        if set(games[game]) & set(games[game + 1]):
    #            E.add((games[player], games[player + 1]))
    #            E.add((games[player + 1], games[player]))
            #if assignedReferee.values() in games:
                #E.add((games[game], games[game+1]))
            
    
    #pairs = list(assignedReferees.keys())
    #refs = list(assignedReferees.values())
    #for i in range(len(pairs)):
    #    for j in range(i + 1, len(pairs)):
    #        if refs[i] in pairs[j] or refs[j] in pairs[i]:
    #            E.add((pairs[i], pairs[j]))
    #            E.add((pairs[j], pairs[i]))
    #        if assignedReferees[pairs[i]] == assignedReferees[pairs[j]]:
    #            E.add((pairs[i], pairs[j]))
    #            E.add((pairs[j], pairs[i]))
    #        if set(pairs[i]) & set(pairs[j]):
    #            E.add((pairs[i], pairs[j]))
    #            E.add((pairs[j], pairs[i]))
    
    # Setting V (verticies) to set of games and Create an empty set for E (edges)
    V = set(assignedReferees.keys())
    E = set()
    
    # Get list of games and referees
    games = list(assignedReferees.keys())
    refs = list(assignedReferees.values())
    
    # Create a set of games that cant play together and add it to E
    for element_2 in range(len(games)):
        for element_1 in range(element_2 + 1, len(games)):
            # Check if both referees are not players in the other game
            if refs[element_2] in games[element_1] or refs[element_1] in games[element_2]:
                # Add it to E and make the edges undirected
                E.add((games[element_2], games[element_1]))
                E.add((games[element_1], games[element_2]))
            # Check if player exists in the other game
            if assignedReferees[games[element_2]] == assignedReferees[games[element_1]]:
                E.add((games[element_2], games[element_1]))
                E.add((games[element_1], games[element_2]))
            # Check if the games are the same (maybe remove)
            if set(games[element_2]) & set(games[element_1]):
                E.add((games[element_2], games[element_1]))
                E.add((games[element_1], games[element_2]))
            # Check if referees are same?
    
    # Create a coloured graph with V and E and get the chromatic colour
    k, C = graphs.minColouring(V, E)
    
    #print("Chromatic number:", k)
    #print("Coloring of the graph:", C)
    
    # Create timeslots using the chromatic colour
    time_slots = graphs.colourClassesFromColouring(C)
    #print("Time slots:", time_slots)
    #print(V)
    #print(E)
    #print(time_slots)
    
    return time_slots

def gameSchedule(assignedReferees, gameGroups):
    
    # Freeze each set of games in game groups
    gameGroups_frozen = [frozenset(group) for group in gameGroups]
    
    # Set V (verticies) to the all referees and game groups
    V = gameGroups_frozen
    for ref in assignedReferees.values():
        V.append(ref)
    
    # Set E as the edges
    E = set()
    
    # Get a list of all referees
    refs = list(assignedReferees.keys())
    
    # Go through each referee in V
    for ref in assignedReferees.values():
        #refs.append(ref)
        # Go through each game group in the set of game groups
        for games in gameGroups:
            # Check all the elements in the game group
            for game in games:
                #print(games)
                #print(ref)
                # Check if referee is playing in the game group
                if any(ref in element for element in games):
                    # Create an edge from the game group to referee
                    E.add((frozenset(games), ref))
                # Check if the referee is the referee for that game
                if ref == assignedReferees.get(game):
                    # Create an edge from referee to the game group
                    E.add((ref, frozenset(games)))
    
    # Create a list of game groups ordered by referees who have games playing first
    game_order = digraphs.topOrdering(set(V), E)
    
    # Unfreeze all the set game groups in the game order list
    if game_order != None:
        game_order = [elem for elem in game_order if isinstance(elem, frozenset)]
        game_order = [set(fs) for fs in game_order]
    #print(E)
    #print("\n")
    return game_order

def scores(p, s, c, games):
   pass

#games = { ( " Alice " , " Bob " ) , ( " Charlie " , " Bob " ) }
#games = { ( " A ", " B " ), (" B ", " C "), (" C ", " D "), (" D ", " A ") }
#games = { ( " A ", " B " ), ( " C ", " D " ) }
#games = { (0, 1), (1, 2), (2, 3), (3, 4), (4, 0) }
#games = { ( " A ", " C " ), ( " A ", " D " ), ( " B ", " C " ), ( " B ", " D ") }

#print(gamesOK(games))
refereecsvfilename = os.path.join(scriptDirectory, 'referees1.csv')
#games = { ('Bob', 'Alice'), ('Joe', 'Charlie'), ('Elaine', 'Rene') }
games = { ('Bob', 'Alice'), ('Joe', 'Charlie'), ('Ellie', 'Rene') }
print(referees(games, refereecsvfilename))
#assignedReferees = { 
#         ('Alice', 'Bob'): 'Rene', 
#         ('Elaine', 'Charlie'): 'Dave',
#         ('Rene', 'Elaine'): 'Alice',
#         ('Dave', 'Bob'): 'Charlie'
#      }
#assignedReferees = { ('Alice', 'Bob'): 'Rene'}
#assignedReferees = { 
#         ('Alice', 'Bob'): 'Rene', 
#         ('Elaine', 'Charlie'): 'Dave',
#         ('Rene', 'Elaine'): 'Alice',
#         ('Dave', 'Bob'): 'Charlie',
#         ('Alice', 'Rene'): 'Dave',
#         ('Dave', 'Elaine'): 'Rene'
#      }
#print(gameGroups(assignedReferees))
# test 3
#assignedReferees = {
#    ('Edward', 'Julia'): 'Faye Valentine',
#    ('Faye Valentine', 'Edward'): 'Evalyn',
#    ('Jet Black', 'Ein'): 'Spike Spiegel',
#    ('Julia', 'Spike Spiegel'): 'Waymond',
#    ('Spike Spiegel', 'Vicious'): 'Faye Valentine',
#    ('Vicious', 'Jet Black'): 'Julia'
#}

#gameGroups = [
#    {('Spike Spiegel', 'Vicious')},
#    {('Vicious', 'Jet Black')},
#    {('Jet Black', 'Ein'), ('Edward', 'Julia')},
#    {('Faye Valentine', 'Edward'), ('Julia', 'Spike Spiegel')},
#]
#assignedReferees = {
    #('Alice', 'Bob'): 'Charlie',
    #('Charlie', 'Bob'): 'Rene'
    #}
#gameGroups = [
    #{ ('Alice', 'Bob') },
    #{ ('Charlie', 'Bob') },
    #]
#assignedReferees =  {
#    ('Spike Spiegel', 'Vicious'): 'Jet Black',
#    ('Edward', 'Julia'): 'Faye Valentine',
#    ('Ein', 'Faye Valentine'): 'Julia',
#    ('Faye Valentine', 'Edward'): 'Vicious',
#    ('Jet Black', 'Ein'): 'Spike Spiegel',
#    ('Julia', 'Spike Spiegel'): 'Ein',
#    ('Vicious', 'Jet Black'): 'Edward'
#    }

#gameGroups = [
#    {('Spike Spiegel', 'Vicious'), ('Ein', 'Faye Valentine')},
#    {('Jet Black', 'Ein'), ('Edward', 'Julia')},
#    {('Faye Valentine', 'Edward'), ('Julia', 'Spike Spiegel')},
#    {('Vicious', 'Jet Black')}
#    ]

#print(gameSchedule(assignedReferees, gameGroups))