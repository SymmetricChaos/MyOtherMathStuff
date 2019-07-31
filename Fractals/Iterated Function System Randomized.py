## An iterated function system work by applying a family of functions repeatedly to the
## same input in every possible sequence. It can be more efficient to randomize this
## process.

def baseConvert(n,b,bigendian=False):
    if(n == 0):
        return([0])
    out = []
    while(n > 0):
        out.append(n%b)
        n //= b
    if(bigendian==True):
        return(out)
    return(out[::-1])


def makeCanvas(xlim=[-3,3],ylim=[-3,3],size=[7,7]):
    fig = plt.figure()
    fig.set_size_inches(size[0], size[1])
    ax = plt.axes(xlim=xlim, ylim=ylim)
    ax.axis('off')
    return fig, ax

import numpy as np

def f(x,n):

    M1 = [np.matrix([[0,0],[0,0.16]]),
         np.matrix([[0.85,-0.04],[0.04,0.85]]),
         np.matrix([[0.2,0.23],[-0.26,0.22]]),
         np.matrix([[-0.15,0.26],[0.28,0.24]])]
    
    M2 = [np.matrix([0,0]),
          np.matrix([0,1.6]),
          np.matrix([0,1.6]),
          np.matrix([0,0.44])]
    
    return np.dot(x,M1[n]) + M2[n]

def IFSrand(N,D):
    out = []
    for x in range(N):
        a = np.matrix([0,0])
        r = np.random.choice(4, D, p=[0.01, 0.75, 0.12, 0.12])
        for i in r:
            a = f(a,i)
        out.append((a.item(0),a.item(1)))

    return np.asarray(out)

N = 4000
D = 30
L = IFSrand(N,D)

import matplotlib.pyplot as plt
fig, ax = makeCanvas([-5,5],[0,10],[10,10])
plt.scatter(L[:,0],L[:,1],facecolor="green",edgecolor=None,alpha=.5,s=.2)
plt.savefig("BarnsleyFernRandomized_N{}_D{}.png".format(N,D),dpi=300)
