import numpy as np
import matplotlib.pyplot as plt
from mbline import mbline

# Slope of the normal at a point
def tangent_slopes(x,y):
    
    xsh = np.roll(x,1)
    ysh = np.roll(y,1)
    
    return (y-ysh)/(x-xsh)

# y-intercept of the normal at a point
def tangent_intercepts(x,y):
    m = tangent_slopes(x,y)
    return -(m*x-y)


def tangents(x,y,size=5,color="blue",alpha=.1,draw=True):

    fig = plt.figure()
    fig.set_size_inches(12,12)

    ax = plt.axes(xlim=(-size,size), ylim=(-size,size))
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
        
    M = tangent_slopes(x,y)
    B = tangent_intercepts(x,y)

    if draw == True:
        mbline(M,B,xlim=(-size,size),ylim=(-size,size),color=color,alpha=alpha)
        
    return M,B


if __name__ == "__main__":
    from Spirogram import trochoid
    from SimpleCurves import ellipse

    x,y = trochoid(4,1,2,hypo=True,n=2001,draw=False)
    tangents(x,y,size=8,color="salmon",alpha=.03)
    plt.plot(x,y)
    
    x,y = ellipse(1,2,n=1001)
    tangents(x,y,size=4,color="salmon",alpha=.03)
    plt.plot(x,y)