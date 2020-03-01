import matplotlib.pyplot as plt
import numpy as np

def ellipse(a,b,n=1001):
    th = np.linspace(0,2*np.pi,n)
    x = a*np.sin(th)
    y = b*np.cos(th)
    
    return x,y

# Vectorize these
def point_slope(x,y,n):
    n = n%len(x)
    return (y[n]-y[n+1])/(x[n]-x[n+1])

def normal_slope(x,y,n):
    m = point_slope(x,y,n)
    return -1/m

def normal_intercept(x,y,n):
    m = normal_slope(x,y,n)
    return -(m*x[n]-y[n])



if __name__ == '__main__':
    
    x,y = ellipse(2,1,201)
    
    fig = plt.figure()
    fig.set_size_inches(12,12)
    plt.axes().set_aspect("equal")
    plt.xlim(-3,3)
    plt.ylim(-3,3)
    plt.axis("off")
        

    plt.plot(x,y,color="CornflowerBlue",linewidth=2)


    for i in range(0,len(x)-1):
        m = normal_slope(x,y,i)
        b = normal_intercept(x,y,i)
        
        x2 = 0
        y2 = m*0+b
        
        plt.plot([x[i],x2],[y[i],y2],color="blue",alpha=.1)
    