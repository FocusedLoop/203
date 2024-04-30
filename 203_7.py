import graphs

# 7.6
def isPath(V, E, p):
    allButLast = p[:-1]
    allButFirst = p[1:]
    consecativePairs = zip(allButLast, allButFirst)
    return all((u,v) in E for u,v in consecativePairs)

#7.7
def abitary(S):
    return next(iter(S))

def connected(V,E):
    v = arbitary(V)
    D = distanceClasses(V, E, v)
    return V==set.union(*D)

#7.8
V = { 'A', 'B', 'C', 'D', 'E', 'F' }
E = { ('A', 'F'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('B','F'), ('C', 'F')}
E = E | { (v,u) for (u,v) in E }
u = 'A'

def distance1(V,E,u):
    d=dict()
    for v in V:
        d[v] = graphs.distance(V, E, u, v)
    return d

def distance2(V, E, u):
    return { v:graphs.distance(V, E, u, v) for v in V }

print(distance1(V, E, u))
print(distance2(V, E, u))