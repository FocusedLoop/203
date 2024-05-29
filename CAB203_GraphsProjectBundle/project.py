import graphs
import digraphs
import csv

def gamesOK(games):
    # Evey player needs to play against or they need 2 games
    # List all the players
    first_elements = {player_1 for (player_1, player_2) in games}
    second_elements = {player_2 for (player_1, player_2) in games}
    players = first_elements | second_elements
    
    # Add edges to ensure graph is undirected
    # Reference: Tutorial 7 python code
    games = games | { (b, a) for (a,b) in games }
    
    # Set V to all players and E to the games
    V = players
    E = games
    
    # Check if all players play at most one game
    opponent_sizes = [graphs.degree(V, E, opponent) for opponent in V]
    if len(set(opponent_sizes)) != 1:
        return False

    # Go through each players opponent (neighbour) in the verticies
    for player in V:
        for player_opponent in V:
            # Check if the player isnt the opponent
            if player != player_opponent:
                # Check if the player plays against the opponent
                if (player, player_opponent) in E or (player_opponent, player) in E:
                    continue
                # Check if the player and opponent share atleast 2 neighbours
                neighbors_player = graphs.N(V, E, player)
                neighbors_player_opponent = graphs.N(V, E, player_opponent)
                common_neighbors = neighbors_player & neighbors_player_opponent
                if len(common_neighbors) < 2:
                    return False
    return True

def referees(games, refereecsvfilename):
    # Read the csv file and create a dictionary of referee conflicts, referee (key) and conflicts(value)
    # Reference: lecture 6 Python CSV DictReader
    rows = {}
    with open(refereecsvfilename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows[row['Referee']] = (row['Conflict1'], row['Conflict2'], row['Conflict3'], row['Conflict4'])
    
    # Set V as the verticies of all games and referees
    V = games.union(list(rows.keys()))
    
    # Set E as the edges
    E = set()
    
    # Get all the players
    first_elements = {player_1 for (player_1, player_2) in games}
    second_elements = {player_2 for (player_1, player_2) in games}
    players = first_elements | second_elements
    
    # Create a list of all games and referees
    games_list = list(games)
    referees = list(rows.keys())
    
    # For each game check each of the conflicts
    for game in range(len(games_list)):
        for conflicts in rows.values():
            for conflict in range(len(conflicts)):
                # Check if that conflict is not in the game
                if list(conflicts)[conflict] not in games_list[game]:
                    # For each referee create an undirected edge for each referee from game to referee
                    for referee in range(len(referees)):
                        E.add((games_list[game], referees[referee]))
                        E.add((referees[referee], games_list[game]))
                        
    # Put V and E into the bipartion function and return to seperate sets, games and referees
    A, B = graphs.bipartition(V, E)
    
    # Match the referees and game returned by the bipartition using the edges
    matched_games = digraphs.maxMatching(A, B, E)
    
    # Create a dictionary from the results of matched_games
    # Set the referee to the value and game to the key
    matched_games_dict = {}
    for matched_game in matched_games:
        if isinstance(matched_game[0], tuple):
            player_game, referee = matched_game
        else:
            referee, player_game = matched_game
            matched_games_dict[player_game] = referee

    return matched_games_dict
    
def gameGroups(assignedReferees):
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
    
    # Create timeslots using the chromatic colour
    time_slots = graphs.colourClassesFromColouring(C)
    
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
        # Go through each game group in the set of game groups
        for games in gameGroups:
            # Check all the elements in the game group
            for game in games:
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

    return game_order

def scores(p, s, c, games):
    # augmentedFlow and maxFlow would be used here
   pass