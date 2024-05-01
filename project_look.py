import graphs
import digraphs
import csv
from collections import defaultdict

# Make sure that you implement all of the following functions
# Run the test suit like:
# python test_project.py
# or
# python3 test_project.py
# 
# you can install pytest with
# pip install pytest 
# Then you can run
# pytest test_project.py

def gamesOK(games):
    connections = {}    #create a dictionary called connections

    #populate the connections dictionary
    for game in games:                      
        player1, player2 = game             #game consists of two players
        if player1 not in connections:
            connections[player1] = set()
        if player2 not in connections:
            connections[player2] = set()
        connections[player1].add(player2)
        connections[player2].add(player1)
        
    print(connections)

    #checking the required property for each pair of distinct players
    players = list(connections.keys())
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            playerA = players[i]
            playerB = players[j]

            #checking if A plays against B
            if playerB in connections[playerA]:
                continue

            #checking if A plays against some other player that plays against B
            found_common_player = False
            for playerC in connections[playerA]:
                if playerB in connections[playerC]:
                    found_common_player = True
                    break

            if not found_common_player:
                return False

    return True     #returns true once all conditions are met


def potentialReferees(refereecsvfilename, player1, player2):
    referees = set()
    with open(refereecsvfilename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  #skip the header row in csv file
        for row in reader:
            #strip white space
            row = [i.strip() for i in row]
            conflicts = [conflict for conflict in row[1:] if conflict]  #filter out empty strings
            if player1 not in conflicts and player2 not in conflicts and row[0] != player1 and row[0] != player2:
                referees.add(row[0])  #add referee to the set
    
    return referees


def gameReferees(gamePotentialReferees):
    assignments = {}
    return assignReferees(assignments, gamePotentialReferees)


#additonal function created for gameReferees function
def assignReferees(assignments, gamePotentialReferees):
    if len(assignments) == len(gamePotentialReferees): #checks if length of assignments is equal to gamePotentialReferees,
        return assignments                             #if it does that means all games have a referee assigned,
    else:                                              #otherwise assign referees
        for game, potentialRefs in gamePotentialReferees.items():
            if game not in assignments:
                for ref in potentialRefs:
                    if ref not in assignments.values():
                        assignments[game] = ref
                        result = assignReferees(assignments, gamePotentialReferees)
                        if result is not None:
                            return result
                        del assignments[game]
        return None


def gameSchedule(assignedReferees):
    schedule = []
    games_to_schedule = list(assignedReferees.items())

    while games_to_schedule:
        slot = []
        people_in_slot = set()

        for game, ref in games_to_schedule[:]:
            player1, player2 = game
            if player1 not in people_in_slot and player2 not in people_in_slot and ref not in people_in_slot:
                slot.append((player1, player2, ref))
                people_in_slot.update(game)
                people_in_slot.add(ref)
                games_to_schedule.remove((game, ref))

        schedule.append(set(slot))

    return schedule


def ranking(games):
    #build the graph of players and their wins
    graph = defaultdict(set)
    for winner, loser in games:
        graph[loser].add(winner)

    #performing sort to determine ranking
    ranking = []
    visited = set()
    stack = set(graph.keys())

    #small function for depth-first search - chatGPT was used to help with sorting correctly :)
    def dfs(player):
        visited.add(player)
        for opponent in graph[player]:
            if opponent not in visited:
                dfs(opponent)
        ranking.append(player)

    while stack:
        player = stack.pop()
        if player not in visited:
            dfs(player)

    #checking to see if the ranking is valid
    for i in range(len(ranking)):
        for j in range(i + 1, len(ranking)):
            if ranking[j] in graph[ranking[i]]:
                return None

    return ranking

games = { ( " Alice " , " Bob " ) , ( " Charlie " , " Bob " ) }

print(gamesOK(games))