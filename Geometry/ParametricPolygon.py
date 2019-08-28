import numpy as np

def parametric_polygon(n):
    th = np.linspace(0,1,100)
    a = np.cos(np.pi/n)
    b = np.cos(2*np.pi*((n*th)%1)/n-np.pi/n)
    r = a/b
    x = r*np.cos(2*np.pi*th)
    y = r*np.sin(2*np.pi*th)
    
    return [(a,b) for a,b in zip(x,y)]
