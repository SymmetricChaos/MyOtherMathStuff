## An iterated function system work by applying a family of functions repeatedly to the
## same input in very possible sequence.

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


X,Y = [],[]
for i in range(2**14):
    S = baseConvert(i,4)
    a = np.matrix([0,0])
    for j in S:
        a = f(a,j)
    X.append(a.item(0))
    Y.append(a.item(1))

import matplotlib.pyplot as plt
fig = plt.figure()
fig.set_size_inches(10,10)
plt.scatter(X,Y,color="green",s=.1)
plt.axes().set_aspect("equal","datalim")
plt.axis("off")
plt.savefig("BarnsleyFern.png",dpi=200)
