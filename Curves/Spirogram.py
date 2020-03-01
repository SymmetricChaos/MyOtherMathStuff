import matplotlib.pyplot as plt
import numpy as np
from GCD import gcd

def trochoid(incirc,outcirc,d=0,hypo=False,draw=True,n=2000):
    
    # Rename incirc and outcirc
    R, r = incirc, outcirc
    
    # Find gcd and reuce everything by it
    # We need the reduced values of R and r in order to determine how many times
    # we wind around the central circle
    g = gcd(R,r)
    R, r, d = R//g, r//g, d/g

    # Angles for the roulette
    th = np.linspace(0,((r+R)*r)*np.pi,n)
    
    # Calculate the roulette for either an epitrochoid or a hypotrochoid
    if hypo == False:
        s = r+R
        x = s*np.cos(th) - d*np.cos(s/r*th)
        y = s*np.sin(th) - d*np.sin(s/r*th)
    else:
        s = R-r
        x = s*np.cos(th) + d*np.cos(s/r*th)
        y = s*np.sin(th) - d*np.sin(s/r*th)
    
    # Points of the inner circle
    th = np.linspace(0,2*np.pi,1000)
    x_circ1 = np.cos(th)*R
    y_circ1 = np.sin(th)*R
    
    # Points of the outer circle position for either an epitrochoid or a hypotrochoid
    if hypo == False:
        x_circ2 = (np.cos(th)*r)+s
        y_circ2 = np.sin(th)*r
        start_point = s-d
        center_point = s
    else:
        x_circ2 = (np.cos(th)*r)+s
        y_circ2 = np.sin(th)*r
        start_point = s+d
        center_point = s
        
    # Draw everything
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

if __name__ == '__main__':
    x,y = trochoid(4,5,7)
    x,y = trochoid(3,4,2)
    x,y = trochoid(5,2,6,hypo=True)
    x,y = trochoid(5,2,1,hypo=True)