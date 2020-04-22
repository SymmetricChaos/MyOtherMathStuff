import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull
from Spirogram import trochoid
from Normals import normals
from Tangents import tangents
from SimpleCurves import circle, ellipse, parabola, hyperbola
from Bezier import bezier
from SuperEllipse import superellipse
from Drawing import make_blank_canvas, draw_curve_xy, draw_dots_xy, draw_closed_curve_xy, make_blank_subplot, mbline
from matplotlib.patches import Rectangle

def double_ellipse():
    x,y = ellipse(1,2,501)
    m1,b1 = normals(x,y,draw=False)
    m2,b2 = tangents(x,y,draw=False)
    
    fig, ax = make_blank_canvas(xrange=(-4.5,4.5),yrange=(-4.5,4.5),size=(14,14))
    
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
    fig, ax = make_blank_canvas(size=(12,12))
    
    draw_curve_xy(X,Y)
    draw_dots_xy(xs,ys)
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
    a = .25
    para_x, para_y = parabola(a,xlim=[-4,4])
    para_y = para_y-(1/(4*a))
    
    # Make a hyperbola and shift it to put the focus at (0,0)
    a,b = 2,2.25
    hypr_x,hypr_y = hyperbola(a,b,xlim=[-4,4])
    hypr_y = hypr_y - np.sqrt(b*b+a*a)
    
    fig, ax = make_blank_canvas(xrange=(-4,4),yrange=(-2,6),size=(14,14))
    
    draw_dots_xy(0,0,color='black')
    draw_closed_curve_xy(circ_x,circ_y)
    draw_closed_curve_xy(elli_x,elli_y)
    draw_curve_xy(para_x,para_y)
    draw_curve_xy(hypr_x,hypr_y)
    

def mixed_spirograms():
    
    # Epitrochoids plotted along with their corresponding hypotrochoids

    fig, ax = make_blank_canvas(size=(16,16))
    
    ctr = 1
    
    for R in range(5,9):
        for r in range(1,5):
            make_blank_subplot(4,4,ctr,box=False)
            x,y = trochoid(R,r,3,draw=False,hypo=True)
            draw_curve_xy(x,y,color="cornflowerblue")
            x,y = trochoid(R,r,3,draw=False)
            draw_curve_xy(x,y,color="cornflowerblue")
            ctr += 1


def yolk():
    
    x,y = superellipse(6,4,4,draw=False,n=2001)
    m,b = normals(x,y,draw=False)

    fig, ax = make_blank_canvas([-7,7],[-5,5],size=(12,8))
    
    draw_closed_curve_xy(x,y,color='white',zorder=10,linewidth=9)
    mbline(m,b,color="yellow",alpha=.03,xlim=[-7,7],ylim=[-5,5])
    
    R = Rectangle((-7,-5),14,10,fc='black')
    ax.add_patch(R)
    




if __name__ == "__main__":
#    double_ellipse()
#    bezier_example()
#    conics_example()
#    mixed_spirograms()
    yolk()