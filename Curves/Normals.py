import matplotlib.pyplot as plt
import numpy as np
from mbline import mbline


# Vectorized calculations

# Slope of the normal at a point
def normal_slopes(x,y):
    xsh = np.roll(x,1)
    ysh = np.roll(y,1)
    return -(x-xsh)/(y-ysh)


# y-intercept of the normal at a point
def normal_intercepts(x,y):
    m = normal_slopes(x,y)
    return -(m*x-y)


def normals(x,y,size=5,color="blue",alpha=.1,draw=True):

    m = normal_slopes(x,y)
    b = normal_intercepts(x,y)

    if draw == True:
        
        fig = plt.figure()
        fig.set_size_inches(12,12)
    
        ax = plt.axes(xlim=(-size,size), ylim=(-size,size))
        ax.axis('off')
        ax.set_xticks([])
        ax.set_yticks([])
        
        mbline(m,b,xlim=[-size,size],ylim=[-size,size],color=color,alpha=alpha)

    return m,b





if __name__ == '__main__':
    from Spirogram import trochoid
    from SimpleCurves import ellipse

    x,y = trochoid(4,1,2,hypo=True,n=2001,draw=False)
    normals(x,y,size=7,color="salmon",alpha=.01)
    plt.plot(x,y)
    
    x,y = ellipse(1,2,n=1001)
    normals(x,y,size=4,color="salmon",alpha=.03)
    plt.plot(x,y)