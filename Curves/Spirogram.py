import matplotlib.pyplot as plt
import numpy as np
from GCD import gcd

def trochoid(incirc,outcirc,d=0,hypo=False,draw=True,n=2000):
    
    R, r = incirc, outcirc
    g = gcd(R,r)
    R, r, d = R//g, r//g, d/g

    th = np.linspace(0,((r+R)*r)*np.pi,n)
    
    if hypo == False:
        s = r+R
        x = s*np.cos(th) - d*np.cos(s/r*th)
        y = s*np.sin(th) - d*np.sin(s/r*th)
    else:
        s = R-r
        x = s*np.cos(th) + d*np.cos(s/r*th)
        y = s*np.sin(th) - d*np.sin(s/r*th)
        
    th = np.linspace(0,2*np.pi,1000)
    x_circ1 = np.cos(th)*R
    y_circ1 = np.sin(th)*R
    
    if hypo == False:
        x_circ2 = (np.cos(th)*r)+s
        y_circ2 = np.sin(th)*r
        start_point = s-d
        center_point = s
    else:
        x_circ2 = (np.cos(th)*r)+R-r
        y_circ2 = np.sin(th)*r
        start_point = R-r+d
        center_point = R-r
        
    
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        
        if hypo == False:
            plt.title(f"Epitrochoid(R={R},r={r},d={d})",fontsize=25)
        else:
            plt.title(f"Hypotrochoid(R={R},r={r},d={d})",fontsize=25)
        
        plt.plot(x,y,color="CornflowerBlue",linewidth=2)
        plt.plot(x_circ1,y_circ1,color="black",zorder=10,linewidth=3)
        plt.plot(x_circ2,y_circ2,color="black",zorder=10,linewidth=3)
        plt.scatter(start_point,0,color="black",zorder=10)
        plt.plot([start_point,center_point],[0,0],color="black",linewidth=3)



    return x,y


x,y = trochoid(4,5,8)
x,y = trochoid(3,4,2)
x,y = trochoid(5,2,6,hypo=True)
x,y = trochoid(5,2,1,hypo=True)