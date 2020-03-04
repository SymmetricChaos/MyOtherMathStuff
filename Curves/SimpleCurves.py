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


def parabola(lo=-1,hi=1,n=1001):
    x = np.linspace(lo,hi,n)
    y = x*x
    
    return x,y


def conic(e,n=1001):
    
    # Circle
    if e == 0:
        return circle(1,n=n)
    # Ellipse
    elif e < 1:
        return ellipse()
    # Parabola
    elif e ==1:
        return parabola(n=n)
    # Hyperbola
    else:
        


def polar_to_cart(r,th):
    return r*np.cos(th), r*np.sin(th)