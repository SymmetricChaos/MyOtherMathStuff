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


def parabola(a=1,xlim=[-1,1],n=1001):
    x = np.linspace(xlim[0],xlim[1],n)
    y = x*x*a
    
    return x,y


# The positive part of the conjugate parabola
# Needs work for a better interface
def hyperbola(a,b,xlim=[-1,1],n=1001):
    x = np.linspace(xlim[0],xlim[1],n)
    y = a*np.sqrt(b*b+x*x)/b

    return x,y


def conic(e,s=1,n=1001):
    
    # Circle
    if e == 0:
        return circle(s,n=n)
    # Ellipse
    elif e < 1:
        a = s
        b = s*np.sqrt(1-e*e)
        return ellipse(a,b,n=n)
    # Parabola
    elif e ==1:
        return parabola(s,n=n)
    # Hyperbola
    else:
        return hyperbola()


def catenary(lo=-1,hi=1,n=1001):
    x = np.linspace(lo,hi,n)
    y = np.cosh(x)
    return x,y




def polar_to_cart(r,th):
    return r*np.cos(th), r*np.sin(th)

if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    
    x1,y1 = catenary()
    x2,y2 = parabola(a=.5)
    plt.axes().set_aspect("equal","datalim")
    plt.plot(x1,y1-1)
    plt.plot(x2,y2)
    