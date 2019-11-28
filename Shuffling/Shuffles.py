from numpy.random import binomial, randint, geometric

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
    # Repeatedly drop the top few cards of the right pile
    # on top of the left pile
    while len(R) > 0:
        br = geometric(.1)
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