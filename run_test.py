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

# Question 3
def generate_game_graph(assignedReferees):
    games = list(assignedReferees.keys())
    vertices = {i for i in range(len(games))}
    edges = set()

    for i in range(len(games)):
        for j in range(i + 1, len(games)):
            game1 = games[i]
            game2 = games[j]
            referee1 = assignedReferees[game1]
            referee2 = assignedReferees[game2]

            # Check if games share a player or referee
            if (referee1 == referee2 or 
                game1[0] in game2 or game1[1] in game2 or
                game2[0] in game1 or game2[1] in game1):
                edges.add((i, j))
                edges.add((j, i))

    return vertices, edges, games

assignedReferees = { 
    ('Alice', 'Bob'): 'Rene', 
    ('Elaine', 'Charlie'): 'Dave',
    ('Rene', 'Elaine'): 'Alice',
    ('Dave', 'Bob'): 'Charlie',
    ('Alice', 'Rene'): 'Dave',
    ('Dave', 'Elaine'): 'Rene'
}

# Generate the graph
vertices, edges, games = generate_game_graph(assignedReferees)

# Find the chromatic number and the coloring
chromatic_number, vertex_coloring = minColouring(vertices, edges)

# Create the schedule based on vertex coloring
schedule = {}
for game_index, color in vertex_coloring.items():
    if color not in schedule:
        schedule[color] = []
    schedule[color].append(games[game_index])

# Output the schedule
print("Chromatic Number (Minimum Time Slots Needed):", chromatic_number)
print("Schedule (Games that can be scheduled at the same time):")
for time_slot, games in schedule.items():
    print(f"Time Slot {time_slot}: {games}")
    
#Question 3.2
def create_graph_from_assignments(assignments):
    """Creates a graph (V, E) from the given referee assignments."""
    V = set(assignments.keys())
    E = set()
    
    pairs = list(assignments.keys())
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            if assignments[pairs[i]] == assignments[pairs[j]]:
                E.add((pairs[i], pairs[j]))
                E.add((pairs[j], pairs[i]))
            if set(pairs[i]) & set(pairs[j]):
                E.add((pairs[i], pairs[j]))
                E.add((pairs[j], pairs[i]))
    
    return V, E

# Given referee assignments
assignedReferees = { 
    ('Alice', 'Bob'): 'Rene', 
    ('Elaine', 'Charlie'): 'Dave',
    ('Rene', 'Elaine'): 'Alice',
    ('Dave', 'Bob'): 'Charlie',
    ('Alice', 'Rene'): 'Dave',
    ('Dave', 'Elaine'): 'Rene'
}

# Create the graph from the given assignments
V, E = create_graph_from_assignments(assignedReferees)

# Print V and E to see the vertices and edges
print("Vertices (V):", V)
print("Edges (E):", E)

# Apply the minColouring function
k, C = minColouring(V, E)

# Print the results
print("Chromatic number:", k)
print("Coloring of the graph:", C)

# Create time slots based on the coloring
time_slots = colourClassesFromColouring(C)
print("Time slots:", time_slots)

#Question 4
def order_game_groups_with_top_ordering(assignedReferees, gameGroups):
    referees = {referee for referee in assignedReferees.values()}
    referee_graph = {referee: {assignedReferees[player_pair] for player_pair in assignedReferees if assignedReferees[player_pair] != referee} for referee in referees}
    top_ordered_referees = topOrdering(referees, referee_graph)
    referee_index = {ref: i for i, ref in enumerate(top_ordered_referees)}
    return sorted(gameGroups, key=lambda group: min(referee_index[assignedReferees[player_pair]] for player_pair in group))

ordered_game_groups = order_game_groups_with_top_ordering(assignedReferees, gameGroups)
#Question 4.2
def order_games(assignedReferees, gameGroups):
    V = set()
    E = set()

    # Constructing vertices and directed edges
    for ref_pair, ref in assignedReferees.items():
        V.add(ref)
        V.add(ref_pair[0])
        V.add(ref_pair[1])
        E.add((ref, ref_pair))
        E.add((ref_pair, ref))

    for group in gameGroups:
        for ref_pair in group:
            V.add(ref_pair)
            E.add((ref_pair, group))
            E.add((group, ref_pair))

    # Determine the order of referees
    ordering = topOrdering(V, E)

    # Order game groups based on the computed order of referees
    ordered_groups = []
    for ref in ordering:
        if ref in gameGroups:
            ordered_groups.append(ref)

    return ordered_groups

# Example data
assignedReferees = {
    ('Edward', 'Julia'): 'Faye Valentine',
    ('Faye Valentine', 'Edward'): 'Evalyn',
    ('Jet Black', 'Ein'): 'Spike Spiegel',
    ('Julia', 'Spike Spiegel'): 'Waymond',
    ('Spike Spiegel', 'Vicious'): 'Faye Valentine',
    ('Vicious', 'Jet Black'): 'Julia'
}

gameGroups = [
    {('Spike Spiegel', 'Vicious')},
    {('Vicious', 'Jet Black')},
    {('Jet Black', 'Ein'), ('Edward', 'Julia')},
    {('Faye Valentine', 'Edward'), ('Julia', 'Spike Spiegel')}
]

# Output ordered game groups
print(order_games(assignedReferees, gameGroups))
#Question 5
# Define the vertices and edges
V = { 's', 'v1', 'v2', 't' }
E = { ('s', 'v1'), ('s', 'v2'), ('v1', 'v2'), ('v1', 't'), ('v2', 't') }
w = { ('s', 'v1'): 10, ('s', 'v2'): 5, ('v1', 'v2'): 15, ('v1', 't'): 10, ('v2', 't'): 10 }

# Define source and sink
s = 's'
d = 't'

# Initialize the flow to zero for all edges
f = { e: 0 for e in E }

# Find an augmenting path
path = augmentingPath(V, E, w, f, s, d)
print("Augmenting Path:", path)

# Augment the flow along the augmenting path
if path:
    f = augmentFlow(path, f, w)
    print("Flow after augmentation:", f)

# Compute the maximum flow
max_flow = maxFlow(V, E, w, s, d)
print("Maximum Flow:", max_flow)

# Total flow into the sink (which will be the maximum flow value)
total_flow = sum(max_flow[(u, 't')] for u in V if (u, 't') in max_flow)
print("Total Flow into sink:", total_flow)