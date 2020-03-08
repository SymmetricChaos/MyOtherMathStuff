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


def parabola(a=1,lo=-1,hi=1,n=1001):
    x = np.linspace(lo,hi,n)
    y = x*x*a
    
    return x,y


def hyperbola(a,b,lo=-1,hi=1,n=1001):
    x = np.linspace(lo,hi,n)
    b2 = b*b
    a2 = a*a
    x2 = x*x
    y = np.sqrt(-b2*(a2-x2))/a
    
    return x,y


def conic(e,n=1001):
    
    # Circle
    if e == 0:
        return circle(1,n=n)
    # Ellipse
    elif e < 1:
        a = 1
        b = np.sqrt(1-e*e)
        return ellipse(a,b,n=n)
    # Parabola
    elif e ==1:
        return parabola(n=n)
    # Hyperbola
#    else:
#        return hyperbola()

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
    