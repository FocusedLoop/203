#!/usr/bin/env python
"""
Tutorial 7 Functions
@Author: Alan
@Date: 2024 Semester 1
"""

import graphs 

# I stole this from lecture


def NS(V, E, S):
   """Returns the set of vertices in V that are adjacent to a vertex in S given edges E.

   If (V,E) is the entire graph, returns the neighbourhood of S."""
   return { v for v in V for u in S if (u,v) in E }


def distanceClasses(V, E, u, D = None):
   """Given a graph (V,E) and a starting vertex u, outputs a list of distances classes.  That is, returns a partition of the vertices into sets of fixed distances from u, where u is in the distance class for distance 0.  Behaviour is undefined if the graph is disconnected."""
   if D is None:                             # j = 0 case
      D = [ {u} ]                            # D[0] = D_0 = {u}
      return distanceClasses(V, E, None, D)  # recurse to get remaining distance classes
   
   Vnew = V - D[-1]                          # V_{j} = V_{j-1} / D_{j-1}
   Dnew = D + [ NS(Vnew, E, D[-1]) ]         # D_{j} = N_{V_j}(D_{j-1})
   if len(Dnew[-1]) == 0: return D           # Didn't find any more vertices.  All done or G is disconnected.
   return distanceClasses(Vnew, E, None, Dnew)

# Alans little corner of things :) 


#================================================================================================

a = ("a", "b", "c")
b = ("1", "2", "3")

x = zip(a, b)
print(list(x))


my_list = ['apple', 'banana', 'cherry']
for index, value in enumerate(my_list):
    print(index, value)

#================================================================================================

# 4c encoded
V = {'A', 'B', 'C', 'D', 'E', 'F'}
E = {('A','D'), ('A','E'), ('A','F'), ('B','C'), ('B','E'),('C','D'),  ('E','F')}
E = E | { (v,u) for (u,v) in E }  # Add in the reverse edges

# E = {('A','D'), ('A','E'), ('A','F'), ('B','C'), ('B','E'),('C','D'),  ('E','F'), ('D','A'), ('E','A'), ('F','A'), ('C','B'), ('E','B'),('D','C'),  ('F','E')}
#connected(V,E)

p = ['A', 'D', 'C']
p = ['A', 'D', 'F']

u = 'A'

NS(V, E, {'C'})
distanceClasses(V,E,u)


distanceClasses(V, E, u)

#######################################################################################
# check list()

# 6. Write a Python function that, given V , E and a list of vertices, determines whether the list forms
# a path. Do so without using a loop.

p = ['A', 'D', 'C']
print(list(zip(p[:-1],p[1:])))

def isPath(V: set,E: set,p: list) -> bool:
   """
   This function takes a set of vertices V, a set of edges E, and a list of vertices p, and returns a boolean that represents whether the list of vertices forms a path.

   :param set V: A set of vertices
   :param set E: A set of edges
   :param list p: A list of vertices
   :return: A boolean that represents whether the list of vertices forms a path
   """
   allMyEdges = zip(p[:-1],p[1:])
   return all( (u,v) in E for (u,v) in allMyEdges )
   # return None


p = ['A', 'D', 'C']
isPath(V,E,p)
p = ['A', 'D', 'F']
isPath(V,E,p)

   
# 7. The lecture slides suggest a way to determine if a graph is connected using distance classes. Implement this method in Python. You may assume that you have access to a function distanceClasses(V, E, u)
# that returns a list containing the distance classes from u in order.

#  access an arbitrary element from a collection without specifically indexing it, especially when you're not concerned with which element you get

def arbitary(S: set) -> any:
   return next(iter(S))


# *D: Unpacks the sets in D into separate arguments.

def connected(V: set,E: set) -> bool:
   """
   This function takes a set of vertices V and a set of edges E, and returns a boolean that represents whether the graph is connected.

   :param set V: A set of vertices
   :param set E: A set of edges
   :return: A boolean that represents whether the graph is connected
   """
   v = arbitary(V)
   D = distanceClasses(V,E,v) 
   return V == set.union(*D)

connected(V,E) #COPIED # Results in bool


#  Using functions from graphs.py write a Python function that takes a graph (V, E) and a vertex
# u ∈ V and returns a dictionary where keys are vertices in V and values are the distances from u
# to the key. Do so two ways: with loops and without any loops.



def distance1(V: set,E: set,u: str) -> dict:
   """
   This function takes a set of vertices V, a set of edges E, and a vertex u, and returns a dictionary where keys are vertices in V and values are the distances from u to the key.

   :param set V: A set of vertices
   :param set E: A set of edges
   :param str u: A vertex in V
   :return: A dictionary where keys are vertices in V and values are the distances from u to the key
   """
   d = dict()

   for v in V:
      d[v] = graphs.distance(V,E,u,v)

   return d

distance1(V,E,'A') # Results in {'E': 1, etc}

def distance2(V: set,E: set,u: str) -> dict:
   """
   This function takes a set of vertices V, a set of edges E, and a vertex u, and returns a dictionary where keys are vertices in V and values are the distances from u to the key.

   :param set V: A set of vertices
   :param set E: A set of edges
   :param str u: A vertex in V
   :return: A dictionary where keys are vertices in V and values are the distances from u to the key
   """
   return {v:graphs.distance(V,E,u,v) for v in V}

distance2(V,E,'A') # Results in {'E': 1, etc}


def distance3(V: set,E: set,u: str) -> dict:
   """
   This function takes a set of vertices V, a set of edges E, and a vertex u, and returns a dictionary where keys are vertices in V and values are the distances from u to the key.

   :param set V: A set of vertices
   :param set E: A set of edges
   :param str u: A vertex in V
   :return: A dictionary where keys are vertices in V and values are the distances from u to the key
   """
   d = dict()   
   D = distanceClasses(V,E,u)
   for dist, distClass in enumerate(D):
      for v in distClass:
         d[v] = dist

   return d

distance3(V,E,'A')


def distance4(V: set,E: set,u: str) -> dict:
   """
   This function takes a set of vertices V, a set of edges E, and a vertex u, and returns a dictionary where keys are vertices in V and values are the distances from u to the key.

   :param set V: A set of vertices
   :param set E: A set of edges
   :param str u: A vertex in V
   :return: A dictionary where keys are vertices in V and values are the distances from u to the key
   """
   D = distanceClasses(V,E,u)
   return {v:dist for dist, distClass in enumerate(D) for v in distClass}

distance4(V,E,'A') # Results in {'E': 1, etc}
