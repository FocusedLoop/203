import graphs
import digraphs

V = { 'A', 'B', 'C','D', 'E', 'F', 'G' }
E = { ('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'G') }
E = E | { (v, u) for (u, v) in E }
r = 'A'
v = 'B'

def get_children(V, E, r, v):
    neighbours = graphs.N(V, E, v)
    # children = neighbours, excluding parent
    spanning_tree = graphs.spanningTree(V, E, r)
    # Dictionary of vertex : parent
    return neighbours - { spanning_tree[v] }

print(get_children(V, E, r, v))

V = { 'A', 'B', 'C', 'D', 'E', 'F' }
E = { ('A', 'B'), ('A', 'E'), ('B', 'D'), ('C', 'A'),
('C', 'B'), ('C', 'E'), ('E', 'B'), ('F', 'A') }

print(digraphs.topOrdering(V, E))

E = { ('A', 'E'), ('A', 'F'), ('A', 'G'), ( 'B', 'F'),
('B', 'G'), ('C', 'E'), ('C', 'F') }
E = E | { (b, a) for (a, b) in E } # symmetrise
# Provide our own bipartition
U = { 'A', 'B', 'C' }
T = { 'E', 'F', 'G' }
print(digraphs.maxMatching(U, T, E))

V = { u for (u,v) in E }
# If not given bipartition
def find_max_matching(V, E):
    U, T = graphs.bipartition(V, E)
    return digraphs.maxMatching(U, T, E)

print(find_max_matching(V, E))