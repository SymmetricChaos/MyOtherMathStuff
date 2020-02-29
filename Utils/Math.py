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

