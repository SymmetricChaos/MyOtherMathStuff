import numpy as np
import matplotlib.pyplot as plt

# Slope of the normal at a point
def tangent_slopes(x,y):
    
    xsh = np.roll(x,1)
    ysh = np.roll(y,1)
    
    return (y-ysh)/(x-xsh)

# y-intercept of the normal at a point
def tangent_intercepts(x,y):
    m = tangent_slopes(x,y)
    return -(m*x-y)


def tangents(x,y,size=5,color="blue",alpha=.1):

    fig = plt.figure()
    fig.set_size_inches(12,12)

    ax = plt.axes(xlim=(-size,size), ylim=(-size,size))
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
        
    m = tangent_slopes(x,y)
    b = tangent_intercepts(x,y)

    for M,B,X,Y in zip(m,b,x,y):

#        if abs(M) >= 1000:
#            continue
        
        x2 = -size
        y2 = x2*M+B
        x3 = size
        y3 = x3*M+B
        
        plt.plot([X,x2],[Y,y2],color=color,alpha=alpha)
        plt.plot([X,x3],[Y,y3],color=color,alpha=alpha)


    return m,b


if __name__ == "__main__":
    from Spirogram import trochoid

    x,y = trochoid(4,5,7,2001)

    tangents(x,y,size=10)