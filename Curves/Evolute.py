import matplotlib.pyplot as plt
import numpy as np
from Spirogram import trochoid
from SimpleCurves import ellipse



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


def evolute(x,y,size=5,color="blue",alpha=.1):

    fig = plt.figure()
    fig.set_size_inches(12,12)

    ax = plt.axes(xlim=(-size,size), ylim=(-size,size))
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
        
    m = normal_slopes(x,y)
    b = normal_intercepts(x,y)
    ctr = 0
    for M,B,X,Y in zip(m,b,x,y):

        ctr += 1
        if abs(M) >= 1000:
            continue
        
        x2 = -size
        y2 = x2*M+B
        x3 = size
        y3 = x3*M+B

        plt.plot([x2,x3],[y2,y3],color=color,alpha=alpha)


    return m,b


if __name__ == '__main__':
    
    x,y = trochoid(4,1,2,hypo=True,n=3001,draw=False)
#    x,y = ellipse(1,2,n=1001)
    
#    x = np.linspace(-2,2,1001)
#    y = x**2

    evolute(x,y,size=8,color="salmon",alpha=.03)
#    plt.plot(x,y)