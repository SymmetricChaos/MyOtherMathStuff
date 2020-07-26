from math import floor, sqrt

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


def cantor_pair(x,y):
    """A unique positive integer that represents the order pair (x,y), x and y positive"""
    if type(x) != int or type(y) != int:
        raise TypeError("arguments must be integers")
    if x < 0 or y < 0:
        raise ValueError("arguments must be positive")
    return ((x+y)*(x+y+1))//2+y


def cantor_tuple(*ks):
    """A unique integer that represents the given tuple"""
    if len(ks) == 2:
        return cantor_pair(ks[0],ks[1])
    else:
        return cantor_tuple(cantor_tuple(*ks[:-1]),ks[-1])


def cantor_pair_inv(n):
    """Inverse of the cantor pairing function"""
    if type(n) != int :
        raise TypeError("n must be an integer")
    if n < 0 :
        raise ValueError("n must be positive")

    w = floor(sqrt(8*n+1)-1)//2
    t = (w*w+w)//2
    y = n - t
    x = w - y
    return x,y


def cantor_tuple_inv(n,k):
    """Inverse of the cantor tuple function"""
    out = []
    for i in range(k-1):
        n,r = cantor_pair_inv(n)
        out = [r] + out
    out = [n] + out
    return tuple(out)





if __name__ == '__main__':
    print(cantor_pair(7,9))
    print(cantor_pair_inv(145))
    
    N = cantor_tuple(21,1,1,3,6)
    print(N)
    print(cantor_tuple_inv(N,5))