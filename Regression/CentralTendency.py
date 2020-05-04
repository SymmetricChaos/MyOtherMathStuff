#import numpy as np
from Utils.Math import sort_by_nth

def median(L):
    L = sorted(L)
    parity = len(L)%2
    half_range = len(L)//2
    
    if parity == 1:
        return L[half_range]
    else:
        return (L[half_range-1]+L[half_range])/2
    

def weighted_median(L,W):
    LW = [(l,w) for l,w in zip(L,W)]
    LW = sort_by_nth(LW,0)
    
    s = sum(W)
    
    t = 0
    ctr = 0
    while t <= s/2:
        t += LW[ctr][1]
        ctr += 1
    
    return LW[ctr-1][0]
    


def mean(L):
    return sum(L)/len(L)


# Arithmetic mean with quartiles beyond t and 1-t removed
#def truncated_mean(L,t=.05):

    
def weighted_mean(L,W=[]):
    if W == []:
        W = [1]*len(L)
    T = [l*w for l,w in zip(L,W)]
    return sum(T)/sum(W)


#def geometric_mean(L):


#def harmonic_mean(L):


if __name__ == '__main__':
    
    A = [1,1,3,4,5]
    B = [1,2,3,6]
    
    print(median(A))
    print(median(B))
    
    print(mean(A))
    print(mean(B))
    
    print(weighted_median(A,[1,2,3,4,5]))