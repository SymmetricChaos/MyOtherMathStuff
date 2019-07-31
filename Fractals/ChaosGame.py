# The chaos game creates a variety of related fractals.
# We choose a set of points and a starting position. Then we start selecting
# from the set of points at random moving half way to the one chosen.

import numpy as np
from matplotlib import pyplot as plt
from random import randint
from Utils.Drawing import make_canvas

def ChaosGame(xy,S,n,d = .5):
    
    def midpoint(a,b):
        x = (a[0]+b[0])*d
        y = (a[1]+b[1])*d
        return x,y
    
    L = []
    for i in range(n):
        r = randint(0,len(S)-1)
        xy = midpoint(xy,S[r])
        L.append(xy)
    
    L = np.asarray(L)
    
    plt.scatter(L[:,0],L[:,1],s=.1)
    

make_canvas([-.1,1])
ChaosGame([0.5,0.5],[[0,0],[1,0],[1,1],[0,1]],20000,8/17)
#plt.savefig("ChaosGame2.png",dpi=100)