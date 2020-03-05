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
        
        if np.isclose(M,0):
            continue
        
        x2 = -size
        y2 = x2*M+B
        x3 = size
        y3 = x3*M+B
        
        plt.plot([x2,x3],[y2,y3],color=color,alpha=alpha)


    return m,b


if __name__ == "__main__":
    from Spirogram import trochoid
    from SimpleCurves import ellipse

    x,y = trochoid(4,1,2,hypo=True,n=2001,draw=False)
    tangents(x,y,size=8,color="salmon",alpha=.03)
    plt.plot(x,y)
    
    x,y = ellipse(1,2,n=1001)
    tangents(x,y,size=4,color="salmon",alpha=.03)
    plt.plot(x,y)