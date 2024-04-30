def forall(S,p):
    for x in S:
        if not p(x):
            return False
    return True

def forall2(S,p):
    return all(p(x) for x in S)

def p(x):
    return x%2 == 0

def exists (S,p):
    for x in S:
        if p(x):
            return True
    return False

def exists2(S,p):
    return any(p(x) for x in S)

def p(x,y):
    return y % x == 0

print(any(	all(p(x,y) for y in {6,8,10}) for x in {2,3,4}))