import numpy as np

def ellipse(a,b,n=1001):
    th = np.linspace(0,2*np.pi,n)
    x = a*np.sin(th)
    y = b*np.cos(th)
    
    return x,y

def circle(r,n=1001):
    th = np.linspace(0,2*np.pi,n)
    x = r*np.sin(th)
    y = r*np.cos(th)
    
    return x,y