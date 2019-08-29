import numpy as np

def parametric_polygon(n,r=1,pts=None):
    if pts:
        th = np.linspace(0,1,pts)
    else:
        th = np.linspace(0,1,n*20+1)
    a = np.cos(np.pi/n)
    b = np.cos(2*np.pi*((n*th)%1)/n-np.pi/n)
    h = a/b
    x = r*h*np.cos(2*np.pi*th)
    y = r*h*np.sin(2*np.pi*th)
    
    return [(a,b) for a,b in zip(x,y)]
