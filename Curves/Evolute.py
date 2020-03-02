import matplotlib.pyplot as plt
import numpy as np
from Spirogram import trochoid


def ellipse(a,b,n=1001):
    th = np.linspace(0,2*np.pi,n)
    x = a*np.sin(th)
    y = b*np.cos(th)
    
    return x,y


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
        
        plt.plot([X,x2],[Y,y2],color=color,alpha=alpha)
        plt.plot([X,x3],[Y,y3],color=color,alpha=alpha)


    return m,b


if __name__ == '__main__':
    
#    x,y = trochoid(5,2,1,hypo=False,n=2501)
    x,y = ellipse(1,1.5,n=1001)
    
#    x = np.linspace(-1,1,1000)
#    y = x**

    evolute(x,y,size=2,color="salmon",alpha=.1)
    plt.plot(x,y)