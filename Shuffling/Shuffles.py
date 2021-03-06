from numpy.random import binomial, randint, poisson
from itertools import cycle

def cut_deck(D):
    """Cut and complete the deck"""
    br = binomial(len(D),.5)
    return D[br:] + D[:br]



def _riffle(D):
    # Cut the deck near the middle
    br = binomial(len(D),.5)
    L = D[:br]
    R = D[br:]
    
    # Riffle the two sections together
    out = []
    while len(L) > 0 and len(R) > 0:
        a = randint(2)
        if a == 0:
            out.append(L.pop(0))
        else:
            out.append(R.pop(0))

    return out + L + R

def riffle(D,n=1):
    """Perform n riffle shuffles"""
    for i in range(n):
        D = _riffle(D)
    return D



def _overhand(D):
    # Cut the deck near the middle
    br = binomial(len(D),.5)
    L = D[:br]
    R = D[br:]
    # Repeatedly drop about five of the cards
    while len(R) > 0:
        br = poisson(5)
        if br > len(R):
            L,R = R+L, []
        L,R = R[:br]+L, R[br:]
    return L

def overhand(D,n):
    """Perform n overhand shuffles"""
    for i in range(n):
        D = _overhand(D)
    return D



def _faro(D,inshuffle=True):
    # Cut the deck exactly at the middle
    br = len(D)//2
    L = D[:br]
    R = D[br:]
    
    # Riffle the two sections together perfectly
    out = []
    if inshuffle:
        while len(L) > 0 and len(R) > 0:
            out.append(R.pop(0))
            out.append(L.pop(0))
    else:
        while len(L) > 0 and len(R) > 0:
            out.append(L.pop(0))
            out.append(R.pop(0))

    return out + L + R

def faro(D,n=1,inshuffle=True):
    """Perform n Faro shuffles"""
    for i in range(n):
        D = _faro(D,inshuffle)
    return D



def fisher_yates(D):
    """Produces an unbiased true shuffle"""
    D = D.copy()
    ctr = len(D)
    for i in range(len(D)):
        k = randint(ctr)
        ctr -= 1
        D.append(D.pop(k))
    return D



def _mongean(D):
    L = D.copy()
    R = []
    
    C = cycle([0,1])
    while len(L) > 0:
        if next(C) == 0:
            R = R + [L.pop(0)]
        else:
            R = [L.pop(0)] + R
    
    return R

def mongean(D,n=1):
    """Perform n Mongean shuffles"""
    for i in range(n):
        D = _mongean(D)
    return D



def pile_shuffle(D,n):
    D = D.copy()
    P = []
    for i in range(n):
        P.append([])
    
    cyc = cycle([i for i in range(n)])
    
    for pos in cyc:
        P[pos].append(D.pop(0))
        if len(D) == 0:
            break
    
    out = fisher_yates(P)
    return sum(out,[])