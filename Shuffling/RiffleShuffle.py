from numpy.random import binomial, randint

def riffle(D):
    # Cut the deck
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

def multi_riffle(D,n):
    for i in range(n):
        D = riffle(D)
    return D