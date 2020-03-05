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
        for m,b in zip(M,B):
            
            if np.isclose(m,0):
                continue
            
            x2 = -size
            y2 = x2*m+b
            x3 = size
            y3 = x3*m+b
            
            plt.plot([x2,x3],[y2,y3],color=color,alpha=alpha)
    

    return M,B


if __name__ == "__main__":
    from Spirogram import trochoid
    from SimpleCurves import ellipse
    from Spirals import fermat_spiral

    x,y = trochoid(4,1,2,hypo=True,n=2001,draw=False)
    tangents(x,y,size=8,color="salmon",alpha=.03)
#    plt.plot(x,y)
    
    x,y = ellipse(1,2,n=1001)
    tangents(x,y,size=4,color="salmon",alpha=.03)
#    plt.plot(x,y)
    
    x1,y2,x2,y2 = fermat_spiral(turns=3,draw=False)
    tangents(x,y,size=4,color="salmon",alpha=.1)
#    plt.plot(x,y)