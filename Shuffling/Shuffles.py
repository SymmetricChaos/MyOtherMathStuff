from numpy.random import binomial, randint

def _riffle(D):
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



def riffle(D,n=1):
    for i in range(n):
        D = _riffle(D)
    return D



def cut_deck(D):
    br = binomial(len(D),.5)
    return D[br:] + D[:br]



#def cut_deck(D,n=1):
#    deck = D.copy()
#    for i in range(n):
#        deck = _cut_deck(deck)
#        print(deck)
#        print()
#    return deck
#
#
#print(cut_deck([i for i in range(20)],5))