import matplotlib.pyplot as plt
import numpy as np
from GCD import gcd


def trochoid(fixed_circ,move_circ,d=0,hypo=False,draw=True,n=2001):
    
    # Rename incirc and outcirc
    R, r = fixed_circ, move_circ
    
    # Find gcd and reuce everything by it
    # We need the reduced values of R and r in order to determine how many times
    # we wind around the central circle
    g = gcd(R,r)
    Rg, rg = R//g, r//g

    # Angles for the roulette
    th = np.linspace(0,((rg+Rg)*r)*np.pi,n)
    
    # Calculate the roulette for either an epitrochoid or a hypotrochoid
    if hypo == False:
        s = R+r
        x = s*np.cos(th) - d*np.cos(s/r*th)
        y = s*np.sin(th) - d*np.sin(s/r*th)
    else:
        s = R-r
        x = s*np.cos(th) + d*np.cos(s/r*th)
        y = s*np.sin(th) - d*np.sin(s/r*th)

    # Draw everything
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        
        plt.plot(x,y,color="CornflowerBlue",linewidth=2)

    return x,y


def trochoid_explanation(fixed_circ,move_circ,d=0,hypo=False,size=10,draw=True,n=2001):
    
    # Rename incirc and outcirc
    R, r = fixed_circ, move_circ
    
    x,y = trochoid(R,r,d,hypo,False,n)
    
    # Points of the inner circle
    th = np.linspace(0,2*np.pi,1001)
    x_fixed = np.cos(th)*R
    y_fixed = np.sin(th)*R
    
    if hypo == False:
        s = R+r
    else:
        s = R-r
    
    # Points of the outer circle position for either an epitrochoid or a hypotrochoid
    if hypo == False:
        x_move = (np.cos(th)*r)+s
        y_move = np.sin(th)*r
        start_point = s-d
        center_point = s
    else:
        x_move = (np.cos(th)*r)+s
        y_move = np.sin(th)*r
        start_point = s+d
        center_point = s
        
    # Draw everything
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(size,size)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        
        if hypo == False:
            plt.title(f"Epitrochoid(R={R},r={r},d={d})",fontsize=25)
        else:
            plt.title(f"Hypotrochoid(R={R},r={r},d={d})",fontsize=25)
        
        plt.plot(x,y,color="CornflowerBlue",linewidth=2)
        plt.plot(x_fixed,y_fixed,color="black",zorder=10,linewidth=3)
        plt.plot(x_move,y_move,color="gray",zorder=10,linewidth=3)
        plt.scatter(start_point,0,color="gray",zorder=10)
        plt.plot([start_point,center_point],[0,0],color="gray",linewidth=3)
        
    return x,y,x_fixed,y_fixed,x_move,y_move





if __name__ == '__main__':
#    trochoid_explanation(4,5,7)
    trochoid_explanation(3,4,3)
#    trochoid_explanation(5,2,6,hypo=True)
    trochoid_explanation(10,4,1,hypo=True)