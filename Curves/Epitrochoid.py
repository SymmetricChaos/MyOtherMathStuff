import matplotlib.pyplot as plt
import numpy as np
from GCD import gcd

def epitrochoid(incirc,outcirc,d=0,draw=True):
    
    R, r = incirc, outcirc
    g = gcd(R,r)
    R, r = R//g, r//g
    s = r+R
    

    th = np.linspace(0,r*R*np.pi,1000)
    
    x = s*np.cos(th) - d*np.cos(s/r*th)
    y = s*np.sin(th) - d*np.sin(s/r*th)
    
    th = np.linspace(0,2*np.pi,1000)
    x_circ = np.cos(th)*R
    y_circ = np.sin(th)*R
    
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        plt.plot(x_circ,y_circ,color="black")
        plt.plot(x,y,color="CornflowerBlue")
        plt.title(f"Epitrochoid(R={R},r={r},d={d})",fontsize=25)

    return x,y


x,y = epitrochoid(4,3,5)