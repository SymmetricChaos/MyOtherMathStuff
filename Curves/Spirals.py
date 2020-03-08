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


def archimedian_spiral(a=1,turns=1,both_branches=False,bounded=False,draw=True,n=1001):
    th = np.linspace(0,2*turns*np.pi,n)
    
    if bounded:
        r = np.arctan(a*th)
    else:
        r = a*th
    
    x,y = polar_to_cart(r,th)
    
    if both_branches:
        x = np.append(np.flip(x),-x)
        y = np.append(np.flip(y),-y)
    
    if draw == True:
        if bounded:
            draw_spiral(x,y,f"Bounded Archimedian Spiral with {turns} turns")
        else:
            draw_spiral(x,y,f"Archimedian Spiral with {turns} turns")
        
    return x,y


def hyperbolic_spiral(a=1,turns=1,draw=True,n=1001):
    th = np.linspace(.1,2*turns*np.pi,n)
    
    r = a/th
    
    x,y = polar_to_cart(r,th)
    
    print(x[0],y[0])
    print(x[-1],y[-1])
    
    if draw == True:
        draw_spiral(x,y,f"Hyperbolic Spiral with {turns} turns")
    return x,y


def fermat_spiral(a=1,k=.5,turns=1,both_branches=True,draw=True,n=1001):
    th = np.linspace(0,2*turns*np.pi,n)
    
    r = a*th**k
    
    x,y = polar_to_cart(r,th)
    
    if both_branches:
        x = np.append(np.flip(x),-x)
        y = np.append(np.flip(y),-y)
    
    if draw == True:
        draw_spiral(x,y,f"Fermat Spiral with {turns} turns")

    
    return x,y


def logarithmic_spiral(a=1,e=np.e,k=1,turns=1,both_branches=False,draw=True,n=1001):
    th = np.linspace(0,2*turns*np.pi,n)
    
    r = a*e**(k*th)
        
    x,y = polar_to_cart(r,th)
    
    if both_branches:
        x = np.append(np.flip(x),-x)
        y = np.append(np.flip(y),-y)
    
    if draw == True:
        draw_spiral(x,y,f"Logarithmic Spiral with {turns} turns")
    
    return x,y





if __name__ == '__main__':
    
    archimedian_spiral(a=.1,turns=5)
    archimedian_spiral(a=.1,turns=5,both_branches=True)
    logarithmic_spiral(e=1.2,turns=5)
    logarithmic_spiral(e=1.2,turns=5,both_branches=True)
#    x,y = archimedian_spiral(a=.1,turns=5,bounded=True)
#    x,y = hyperbolic_spiral(.1,turns=10,n=5001)
#    x,y = fermat_spiral(1,k=.5,turns=10,n=1001)
