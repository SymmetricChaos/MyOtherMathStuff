def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    if x == 0:
        return 0
    

def prod(L):
    out = 1
    for i in L:
        out *= i
    return out


def pairs(m=0):
    ctr = m
    while True:
        for i in range(m,ctr+1):
            yield (i,ctr)
        ctr += 1
        
        
def inds_where(L,val):
    """All indices of list L that equal val"""
    return [i for i in range(len(L)) if L[i] == val]


def first_where(L,val):
    """First index of list L that equals val"""
    for pos,l in enumerate(L):
        if l == val:
            return pos
    return None
     

def sort_by_nth(L,n,func=None):
    """Sort a list of lists by the nth element of each sublist"""
    if func == None:
        f = lambda x: x[n]
        return sorted(L,key=f)
    else:
        f = lambda x: func(x[n])
        return sorted(L,key=f)