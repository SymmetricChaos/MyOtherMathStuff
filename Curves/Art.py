import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull
from mbline import mbline
from Spirogram import trochoid
from Normals import normals
from Tangents import tangents
from SimpleCurves import circle, ellipse, parabola
from Bezier import bezier

def double_ellipse():
    x,y = ellipse(1,2,501)
    m1,b1 = normals(x,y,draw=False)
    m2,b2 = tangents(x,y,draw=False)
    
    fig = plt.figure()
    fig.set_size_inches(14,14)
    ax = plt.axes(xlim=(-4.5,4.5), ylim=(-4.5,4.5))
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    mbline(m1,b1,alpha=.05,color='red')
    mbline(m2[1:],b2[1:],alpha=.05,color='red')
    
    
def bezier_example():
    
    points = np.array([ (-4,0), 
                        (2,-4),
                        (3,-2),
                        (-2,4), 
                        (-1,2), 
                        (2,0) ])

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    
    X,Y = bezier(points)
    
    # Plot the curve, the points, and annotations
    fig = plt.figure()
    fig.set_size_inches(12,12)
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.plot(X,Y)
    plt.scatter(xs,ys)
    plt.title(f"Bezier Curve with {len(points)} Control Points\nBounding Property of Convex Hull Shown\n",size=20)
    for num,pos in enumerate(points):    
        plt.annotate(f"{num+1}: ({pos[0]},{pos[1]})",[pos[0],pos[1]+.1],size=14)


    # Show convex hull property
    hull = ConvexHull(points)
    for simplex in hull.simplices:
         plt.plot(points[simplex, 0], points[simplex, 1], 'lightgray',zorder=-1)


def conics_example():

    # Its a circle
    circ_x, circ_y = circle(1,101)
    
    # Make an ellipse and shift it to put the focus at (0,0)
    a,b = 2,2.5
    elli_x, elli_y = ellipse(a,b,101)
    elli_y = elli_y+np.sqrt(b**2-a**2)
    
    # Make a parabola and shift it to put the focus at (0,0)
    a = 12
    para_x, para_y = parabola(lo=-4,hi=4)
    para_y = para_y-(1/4*a)
    
    fig = plt.figure()
    fig.set_size_inches(12,12)
    ax = plt.axes(xlim=(-4,4), ylim=(-2,6))
    ax.set_aspect("equal","datalim")
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.scatter(0,0,color='black')
    plt.plot(circ_x,circ_y)
    plt.plot(elli_x,elli_y)
    plt.plot(para_x,para_y)
    

if __name__ == "__main__":
#    double_ellipse()
#    bezier_example()
    conics_example()