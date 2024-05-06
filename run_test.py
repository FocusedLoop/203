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
    for opponent in opponents:
        if graphs.degree(opponents, games, opponent) > 1:
            return False
    return True
    
    #graphs.degree(players, )

games = { ( " Alice " , " Bob " ) , ( " Charlie " , " Bob " ) }
#games = { ( " A ", " B " ), (" A ", " C "), (" B ", " D "), (" C ", " D "), (" B ", " C ") }
#games = { ( " A ", " B " ), ( " C ", " D " ) }
#games = { ( " A ", " B " ), ( " C ", " D " ), ( " E ", " F " ), ( " A ", " D " ) }
#games = { ( " A ", " C " ), ( " A ", " D " ), ( " B ", " C " ), ( " B ", " D ") }

print(gamesOK(games))

def gamesOK(games):
    graph = {}
    for game in games:
        player1, player2 = game
        if player1 not in graph:
            graph[player1] = set()
        if player2 not in graph:
            graph[player2] = set()
        graph[player1].add(player2)
        graph[player2].add(player1)
        
    print(graph)

    game_counts = {player: len(opponents) for player, opponents in graph.items()}
    min_games = min(game_counts.values())
    max_games = max(game_counts.values())
    return max_games - min_games <= 1

# Example usage:
#games = {("Alice", "Bob"), ("Charlie", "Bob")}
#print(gamesOK(games))  # Output: True

def gamesOK(games):
    graph = {}
    for game in games:
        player1, player2 = game
        if player1 not in graph:
            graph[player1] = set()
        if player2 not in graph:
            graph[player2] = set()
        graph[player1].add(player2)
        graph[player2].add(player1)
    
    print(graph)

    for player1 in graph:
        for player2 in graph:
            if player1 != player2:
                common_opponents = graph[player1].intersection(graph[player2])
                if player2 not in graph[player1] and len(common_opponents) < 2:
                    return False

    game_counts = {player: len(opponents) for player, opponents in graph.items()}
    return len(set(game_counts.values())) == 1

# Example usage:
#games = {("Alice", "Bob"), ("Charlie", "Bob"), ("Alice", "Charlie")}
#print(gamesOK(games))  # Output: True

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
    
    # Symmetrise
    print(games)
    games = games | { (b, a) for (a,b) in games }
    print(games)
    
    opponents = {}
    for game in games:
        opponents[game] = graphs.NS(players, games, game)
    #print(opponents)

    for group in games:
        if graphs.degree(opponents, games, group) < 2:
            return False
    return True