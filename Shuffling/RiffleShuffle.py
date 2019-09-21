from numpy.random import binomial, randint

def riffle(D,n):
    br = binomial(len(D),.5)
    L = D[:br]
    R = D[br:]
    out = []
    while len(L) > 0 and len(R) > 0:
        a = randint(2)
        if a == 0:
            out.append(L.pop(0))
        else:
            out.append(R.pop(0))

    return out + L + R


D = [i for i in range(30)]

print(riffle(D,1))