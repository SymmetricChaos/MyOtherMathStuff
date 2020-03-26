import numpy as np

def circle(r=1,n=1001):
    th = np.linspace(0,2*np.pi,n)
    x = r*np.sin(th)
    y = r*np.cos(th)
    
    return x,y


def ellipse(a,b,n=1001):
    th = np.linspace(0,2*np.pi,n)
    x = a*np.sin(th)
    y = b*np.cos(th)
    
    return x,y


# Calculate ellipse from eccentricity and a scale factor
def ellipse_ecc(e,s=1,n=1001):
    
    if e < 0:
        raise Exception("Not a valid conic section")
    if e == 0:
        return circle(s,n)
    if e == 1:
        raise Exception("This eccentricity produces a parabola")
    if e > 1:
        raise Exception("This eccentricity produces a hyperbola")
        
    a = s
    b = s*np.sqrt(1-(e*e))
    th = np.linspace(0,2*np.pi,n)
    x = a*np.sin(th)
    y = b*np.cos(th)
    
    return x,y


def parabola(a=1,xlim=[-1,1],n=1001):
    x = np.linspace(xlim[0],xlim[1],n)
    y = x*x*a
    
    return x,y


# The positive part of the conjugate parabola
# Shows relationship with parabola and easier to work with when drawing
def hyperbola(a,b,xlim=[-1,1],n=1001):
    x = np.linspace(xlim[0],xlim[1],n)
    y = a*np.sqrt(b*b+x*x)/b

    return x,y


#def hyperbola_ecc(e,s,xlim=[-1,1],n=1001):
#    if e < 0:
#        raise Exception("Not a valid conic section")
#    if e == 0:
#        return Exception("This eccentricity produces a circle")
#    if e < 1:
#        return Exception("This eccentricity produces a ellipse")
#    if e == 1:
#        return parabola(s,xlim=xlim,n=n)
#        
#    a = s
#    b = s*
#    x = np.linspace(xlim[0],xlim[1],n)
#    y = a*np.sqrt(b*b+x*x)/b
#
#    return x,y


def catenary(lo=-1,hi=1,n=1001):
    x = np.linspace(lo,hi,n)
    y = np.cosh(x)
    return x,y


def polar_to_cart(r,th):
    return r*np.cos(th), r*np.sin(th)





if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    
    x1,y1 = catenary()
    x2,y2 = parabola(a=.7)
    plt.axes().set_aspect("equal","datalim")
    plt.plot(x1,y1-1)
    plt.plot(x2,y2)
    plt.show()
    
    x,y = ellipse_ecc(.7,1.5)
    plt.axes().set_aspect("equal","datalim")
    plt.plot(x,y)
    
    