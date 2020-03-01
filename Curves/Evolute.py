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


def evolute(x,y,alpha=.1):

    fig = plt.figure()
    fig.set_size_inches(12,12)
    plt.axes().set_aspect("equal")
    plt.xlim(min(x)*1.5,max(x)*1.5)
    plt.ylim(min(y)*1.5,max(y)*1.5)
    plt.axis("off")
        

#    plt.plot(x,y,color="black",linewidth=1)

    m = normal_slopes(x,y)
    b = normal_intercepts(x,y)
    for M,B,X,Y in zip(m,b,x,y):

        if abs(M) >= 1000:
            continue
        
        x2 = min(x)*1.5
        y2 = x2*M+B
        
        plt.plot([X,x2],[Y,y2],color="blue",alpha=.1)
        
        x2 = max(x)*1.5
        y2 = x2*M+B
        
        plt.plot([X,x2],[Y,y2],color="blue",alpha=.1)



if __name__ == '__main__':
    
    x,y = trochoid(5,2,1,hypo=True,draw=False,n=2001)
    evolute(x,y)
    