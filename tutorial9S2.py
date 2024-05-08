#!/usr/bin/env python
"""
Tutorial 9 Functions
@Author: Alan
@Date: 2024 Semester 1
"""

import graphs 
import digraphs

# Here I am just going to visualise the tree
# This was just a quick google so I dont need to draw it by hand.

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


#------------------------------------------------------------


# Example for Q1 Power

V = { 'A', 'B', 'C','D', 'E', 'F', 'G' }
E = { ('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'G'), ('E','C') }
E = E | { (v, u) for (u, v) in E }
r = 'A'


G = nx.Graph()
G.add_edges_from(list(E))
nx.draw(G, with_labels=True, node_size=1500, alpha=0.3, arrows=True)
plt.title("UN-Directed")
plt.show()

test = graphs.spanningTree(V, E, r)

Edges = { (v, u) for u, v in test.items() if v is not None }
Edges = Edges | { (u, v) for u, v in test.items() if v is not None }
Vertices = set(test.keys())

G = nx.Graph()
G.add_edges_from(list(Edges))
nx.draw(G, with_labels=True, node_size=1500, alpha=0.3, arrows=True)
plt.title("UN-Directed")
plt.show()

# Example for Q2 Clothes

V = {"socks", "shoes", "pants", "belt", "gloves","jacket", "hat","shirts"}
E = {("socks","shoes"), ("pants","shoes"), ("belt","pants"), ("jacket","shirt"), ("glove","jacket"), ("hat","jacket")}

E2 = { (v, u) for (u, v) in E }

G = nx.DiGraph()
G.add_edges_from(list(E2))
nx.draw(G, with_labels=True, node_size=1500, alpha=0.3, arrows=True)
plt.title("Directed")
plt.show()

digraphs.topOrdering(V, E2)



#------------------------------------------------------------

# Case Study


adj_list = {
    "A": {"B", "D"},
    "B": {"A", "C", "D"},
    "C": {"B", "D", "E"},
    "D": {"A", "B", "C"},
    "E": {"C"},
}



v_set = set(adj_list.keys())

for vertex in v_set:
    for neighbour in adj_list[vertex]:
        print(vertex, neighbour)

v_set = set(adj_list.keys())

e_set = {(vertex, neighbour) for vertex in v_set for neighbour in adj_list[vertex]}


G = nx.Graph()
G.add_edges_from(list(e_set))
nx.draw(G, with_labels=True, node_size=1500, alpha=0.3, arrows=True)
plt.title("UN-Directed")
plt.show()


def firstHop(v_set, e_set, start, end):
    if start == end: return None
    return graphs.shortestPath(v_set, e_set, start, end)[1]


firstHop(v_set,e_set, 'A', 'A')


def routingTable(v_set, e_set, start):
    return { end: firstHop(v_set,e_set,start,end) for end in v_set }

routingTable(v_set, e_set, 'D')


def solve_rtp(adj_list, start):
    v_set = set(adj_list.keys())
    e_set = {(vertex, neighbour) for vertex in v_set for neighbour in adj_list[vertex]}
    return routingTable(v_set, e_set, start)

solve_rtp(adj_list, 'A')
solve_rtp(adj_list, 'D')

