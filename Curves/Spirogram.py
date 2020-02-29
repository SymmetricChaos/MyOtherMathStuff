import matplotlib.pyplot as plt
import numpy as np
from GCD import gcd

def spirogram(incirc,outcirc,d=0,hypo=False,draw=True,n=2000):
    
    R, r = incirc, outcirc
    g = gcd(R,r)
    R, r = R//g, r//g
    s = r+R
    

    th = np.linspace(0,(s*r)*np.pi,n)
    
    if hypo == False:
        x = s*np.cos(th) - d*np.cos(s/r*th)
        y = s*np.sin(th) - d*np.sin(s/r*th)
    else:
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
        start_point = s+d
        center_point = R-r
        
    
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        plt.plot(x_circ1,y_circ1,color="black")
        plt.plot(x_circ2,y_circ2,color="black")
        plt.scatter(start_point,0,color="black")
        plt.plot([start_point,center_point],[0,0],color="black")
        plt.plot(x,y,color="CornflowerBlue")
        if hypo == False:
            plt.title(f"Epitrochoid(R={R},r={r},d={d})",fontsize=25)
        else:
            plt.title(f"Hypotrochoid(R={R},r={r},d={d})",fontsize=25)

    return x,y


x,y = spirogram(4,3,2)
x,y = spirogram(4,3,2,hypo=True)

print(x[0])