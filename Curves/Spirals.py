import numpy as np
import matplotlib.pyplot as plt
from SimpleCurves import polar_to_cart

def draw_spiral(x,y,title=""):
    fig = plt.figure()
    fig.set_size_inches(10,10)
    plt.axes().set_aspect("equal","datalim")
    plt.axis("off")
    plt.title(title,size=20)
    plt.plot(x,y,color="CornflowerBlue",linewidth=2)


def archimedian_spiral(a=1,turns=1,bounded=False,draw=True,n=1001):
    th = np.linspace(0,2*turns*np.pi,n)
    
    if bounded:
        r = np.arctan(a*th)
    else:
        r = a*th
    
    x,y = polar_to_cart(r,th)
    
    if draw == True:
        draw_spiral(x,y,f"Archimedian Spiral with {turns} turns")
        
    return x,y


def hyperbolic_spiral(a=1,turns=1,draw=True,n=1001):
    th = np.linspace(0,2*turns*np.pi,n)
    
    r = a/th
    
    x,y = polar_to_cart(r,th)
    
    if draw == True:
        draw_spiral(x,y,f"Hyperbolic Spiral with {turns} turns")
    return x,y


def fermat_spiral(a=1,turns=1,draw=True,n=1001):
    th = np.linspace(0,2*turns*np.pi,n)
    
    r = a*th**.5
    
    x,y = polar_to_cart(r,th)
    
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        plt.title(f"Fermat Spiral with {turns} turns",size=20)
        plt.plot(x,y,color="CornflowerBlue",linewidth=2)
        plt.plot(-x,-y,color="CornflowerBlue",linewidth=2)

    
    return x,y,-x,-y


def logarithmic_spiral(a=1,e=np.e,k=1,turns=1,bounded=False,draw=True,n=1001):
    th = np.linspace(0,2*turns*np.pi,n)
    
    if bounded:
        r = np.arctan(a*e**(k*th))
    else:
        r = a*e**(k*th)
        
    x,y = polar_to_cart(r,th)
    
    if draw == True:
        draw_spiral(x,y,f"Logarithmic Spiral with {turns} turns")
    
    return x,y





if __name__ == '__main__':
    
    x,y = archimedian_spiral(a=.1,turns=5)
    x,y = archimedian_spiral(a=.1,turns=5,bounded=True)
    x,y = hyperbolic_spiral(turns=10,n=5001)
    x1,y2,x2,y2 = fermat_spiral(5,turns=3)
    x,y = logarithmic_spiral(e=1.2,turns=5)