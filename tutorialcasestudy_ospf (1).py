from graphs import *

def adjacencyListToGraph(adjacencyList):
   N = adjacencyList    # This is really the neighbourhood function 
   V = set(N.keys())
   E = { (u, v)   for u in V   for v in N[u] }
   return V, E


def adjacencyListToGraph2(adjacencyList):
   N = adjacencyList    # This is really the neighbourhood function 
   V = set(N.keys())
   E = set.union(*( { (u,v)   for v in N[u] }   for u in V ))
   return V, E


def firstHop(V, E, start, end):
   if start == end: return None
   return shortestPath(V, E, start, end)[1]


def routingTable(V, E, u):
   return {v: firstHop(V, E, u, v)   for v in V }


def solveRTP(adjacencyList, u):
   V, E = adjacencyListToGraph(adjacencyList)
   return routingTable(V, E, u)


if __name__ == "__main__":
   neighbours = {
      "A": { "B", "D" },
      "B": { "A", "C", "D" },
      "C": { "B", "D", "E" },
      "D": { "A", "B", "C" },
      "E": { "C" }
   }
   print(solveRTP(neighbours, "A"))