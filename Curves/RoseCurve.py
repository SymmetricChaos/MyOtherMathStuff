import matplotlib.pyplot as plt
import numpy as np

def polar_to_cart(r,th):
    return r*np.cos(th), r*np.sin(th)


def rose(n,d=1,c=0,k=1000,draw=True):
    
    assert type(n) == type(d) == type(k) == int
    
    if n%2 == 0 or d%2 == 0:
        th = np.linspace(0,2*d*np.pi,k)
    else:
        th = np.linspace(0,d*np.pi,k)
    
    r = np.cos(n/d*th)+c
    
    x,y = polar_to_cart(r,th)

    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        plt.plot(x,y)
        plt.title(f"Rose(n={n}, d={d}, c={c})",fontsize=25)
        
    return x,y


#def maurer_rose(n,m=361,ang=10,draw=True):
#    
#    assert type(n) == type(d) == type(m) == int
#    
#    degrees = ang*np.pi/180
#    print(ang)
#    print(degrees)
#    angles = np.array([degrees*x for x in range(m)])
#    print(angles%(2*np.pi))
#    radii = np.sin(n*angles)
#    
#    x,y = polar_to_cart(radii,angles)
#
#    if draw == True:
#        fig = plt.figure()
#        fig.set_size_inches(10,10)
#        plt.axes().set_aspect("equal","datalim")
#        plt.axis("off")
#        plt.plot(x,y)
#        plt.title(f"MaurerRose(n={n}, d={d}, c={c})",fontsize=25)
#        
#    return x,y



if __name__ == '__main__':
    x,y = rose(4,7,1)
#    maurer_rose(2)