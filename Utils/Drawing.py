import matplotlib.pyplot as plt
import matplotlib.collections as collections
import matplotlib.lines as lines
from Utils.PointTypes import complex_to_xy, points_to_xy

def make_blank_canvas(xlim=None,ylim=None,size=[12,12],box=False):
    fig = plt.figure()
    fig.set_size_inches(size[0],size[1])
    # If no coordinate range is given fit everything into a square
    if not xlim and not ylim:
        ax = plt.axes()
        ax.set_aspect("equal","datalim")
    # If only xrange is given fit a square
    elif not ylim:
        ax = plt.axes(xlim=xlim,ylim=xlim)
    # If both are given fit the rectangle
    else:
        ax = plt.axes(xlim=xlim,ylim=ylim)
        
    if box == False:
        ax.axis('off')
        
    ax.set_xticks([])
    ax.set_yticks([])
    
    return fig,ax


def make_blank_subplot(a,b,p,xlim=None,ylim=None,box=True):
    ax = plt.subplot(a,b,p)
    
    # If no coordinate range is given fit everything into a square
    if not xlim and not ylim:
        ax.set_aspect("equal","datalim")
    # If only xrange is given fit a square
    elif not ylim:
        ax.set_xlim(xlim)
        ax.set_ylim(xlim)
    # If both are given fix the rectangle
    else:
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
    
    if box == False:
        ax.axis('off')
        
    ax.set_xticks([])
    ax.set_yticks([])
    
    return ax


# Convenience function for solving mbline equations
def calc_y(m,x,b):
    return m*x+b

def calc_x(m,y,b):
    return (y-b)/m

# Draw an infinite slope-intercept line
def mbline(m,b,xlim=[],ylim=[],ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    
    if xlim == []:
        xlim = ax.get_xlim()
        
    if ylim == []:
        ylim = ax.get_ylim()
           
    x_lo = xlim[0]
    y_lo = ylim[0]
    
    x_hi = xlim[1]
    y_hi = ylim[1]
    
    x0 = x_lo
    y0 = calc_y(m,x_lo,b)
    
    if y0 < y_lo:
        x0 = calc_x(m,y_lo,b)
        y0 = y_lo
    elif y0 > y_hi:
        x0 = calc_x(m,y_hi,b)
        y0 = y_hi
            
    x1 = x_hi
    y1 = calc_y(m,x_hi,b)
    if y1 > y_hi:
        x1 = calc_x(m,y_hi,b)
        y1 = y_hi
    elif y1 < y_lo:
        x1 = calc_x(m,y_lo,b)
        y1 = y_lo

    line = lines.Line2D([x0,x1], [y0,y1], axes=ax,**kwargs)
    ax.add_line(line)
    
    return [[x0,y0],[x1,y1]],line

# Draw multiple slope-intercept lines
def mblines(M,B,xlim=[],ylim=[],ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    if xlim == []:
        xlim = ax.get_xlim()
    if ylim == []:
        ylim = ax.get_ylim()
    out = []
    for m,b in zip(M,B):
        l = mbline(m,b,xlim,ylim,ax,**kwargs)
        out.append(l)
    return out


# Draw an infinite line through a given point with a given line
def point_slope_line(P,m,xlim=[],ylim=[],ax=None,**kwargs):    
    b = m*P[1]+P[0]
    return mbline(m,b,xlim,ylim,ax,**kwargs)

# Draw multiple point-slope lines
def point_slope_lines(P,M,xlim=[],ylim=[],ax=None,**kwargs):    
    B = [m*p[0]+p[1] for m,p in zip(M,P)]
    return mblines(M,B,xlim,ylim,ax,**kwargs)
    

# Vertical and horizontal lines
def vertical_line(xpos=0,ylim=[],ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    if ylim == []:
        ylim = ax.get_ylim()
    line = lines.Line2D([xpos,xpos],ylim, axes=ax,**kwargs)
    ax.add_line(line)
    return [[xpos,xpos],ylim],line
    
def horizontal_line(ypos=0,xlim=[],ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    if xlim == []:
        xlim = ax.get_xlim()
    line = lines.Line2D(xlim,[ypos,ypos], axes=ax,**kwargs)
    ax.add_line(line)
    return [xlim,[ypos,ypos]],line

# Draw a curve from:
#   seperate lists of x and y coordinates
#   a list of (x,y) points
#   a list of complex numbers
def draw_curve_xy(x,y,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    line = lines.Line2D(x,y, axes=ax,**kwargs)
    ax.add_line(line)

def draw_curve_p(P,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    x,y = points_to_xy(P)
    line = lines.Line2D(x,y, axes=ax,**kwargs)
    ax.add_line(line)

def draw_curve_c(C,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    x,y = complex_to_xy(C)
    line = lines.Line2D(x,y, axes=ax,**kwargs)
    ax.add_line(line)


# Draw a curve that attaches the start to the end. Same options
def draw_closed_curve_xy(x,y,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    # Convert to list because an np.array doesn't play nice
    X = list(x) + [x[0]]
    Y = list(y) + [y[0]]
    line = lines.Line2D(X,Y, axes=ax,**kwargs)
    ax.add_line(line)
    
def draw_closed_curve_p(P,ax=None,**kwargs):
    x,y = points_to_xy(P)
    draw_closed_curve_xy(x,y,ax,**kwargs)
    
def draw_closed_curve_c(P,ax=None,**kwargs):
    x,y = complex_to_xy(P)
    draw_closed_curve_xy(x,y,ax,**kwargs)


# Draw scatterplot from
def draw_dots_xy(x,y,**kwargs):
    plt.scatter(x,y,**kwargs)

def draw_dots_p(P,**kwargs):
    x,y = points_to_xy(P)
    plt.scatter(x,y,**kwargs)

def draw_dots_c(C,**kwargs):
    x,y = complex_to_xy(C)
    plt.scatter(x,y,**kwargs)


# Connect points A and B, complex version provided, xy version doesn't make much sense
def connect_p(A,B,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    line = lines.Line2D([A[0],B[0]], [A[1],B[1]], axes=ax,**kwargs)
    ax.add_line(line)

def connect_c(A,B,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    line = lines.Line2D([A.real,B.real], [A.imag,B.imag], axes=ax,**kwargs)
    ax.add_line(line)


# Convenience functions for titles
def title(text="",ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    ax.set_title(text,**kwargs)

def canvas_title(text="",fig=None,**kwargs):
    if fig == None:
        fig = plt.gcf()
    fig.suptitle(text,**kwargs)


# Creates circles with more control than draw_dots, created a PatchCollection
# Can use setters to change all elements of the collection at once
# Accepts single **kwargs for args other than X,Y,and R, these are reused for
# all of the circles
# KWARGS IS BUGGED
def draw_circles_xy(X,Y,R,ax=None, **kwargs):
    if ax == None:
        ax = plt.gca()
    circles = [plt.Circle((x,y), radius=r, **kwargs) for x,y,r in zip(X,Y,R)]
    C = collections.PatchCollection(circles)
    ax.add_collection(C)
    return C


# Convenient function for a single circle, can be used for finer control of
# lots of different circles
def draw_circle_xy(X,Y,R,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    circle = plt.Circle((X,Y), radius=R, **kwargs)
    ax.add_patch(circle)
    return circle





if __name__ == '__main__':
    
    import numpy as np
    
    ## SIMPLE PLOT ## 
    
    make_blank_canvas([-5,5],[-5,5])
    draw_curve_xy([1,2,3],[1,2,1])
    draw_closed_curve_xy([1,2,3],[0,1,0],color="green")
    horizontal_line(-2)
    vertical_line(1,color='brown')
    
    
    ## PLOTS AND SUBPLOTS ##
    
    # Make a circle
    # Then make a circle with exactly half the radius
    draw_circle_xy(-1.5,.8,2,ec='black',linewidth=3)
    draw_circle_xy(-.5,.8,1,fc='salmon')
    
    # Subplots example
    make_blank_canvas()
    
    # Make and use a subplot
    sp1 = make_blank_subplot(2,2,1,[-3,3])
    
    # mbline takes ylim and xlim from axes to automatically appear infinite
    mbline(-.5,0)
    # mbline can be manually limited
    slopes = np.linspace(0,5,10)
    mblines(slopes,[0]*20,xlim=[-2,2],ylim=[-2,2],color='red')
    
    # Subplots of different layouts can coexist
    sp2 = make_blank_subplot(4,4,4,[-2,2])
    draw_closed_curve_xy([1,2,3],[0,1,0])
    # Create an mbline on the most recently created axes
    mbline(1,1)
    
    # Plots can be created out of order
    # When subplots are not square shapes are warped
    sp3 = make_blank_subplot(2,2,4,[-3,3],[-5,5])
    draw_circle_xy(1.5,-.5,1,fc='white',ec='black')
    
    # Show automatic xlim and ylim settings
    sp4 = make_blank_subplot(4,4,7)
    x = np.random.uniform(-2,2,200)
    y = x+np.random.uniform(-2,2,200),
    draw_dots_xy(x,y,alpha=.5,color='limegreen')
    title("BLOOPS",size=30)
    
    # Add lines to a chosen axes
    mblines([1,2,3,4,5],[0,0,0,0,0],ax=sp3)
    
    # Make some circles
    draw_circles_xy([0,1,2],[0,0,0],[.5,.3,1],sp2,fc='green')
    
    # Title on selected axis
    title(r'We can use LaTeX $\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$',ax=sp1,size=16,pad=20)
    canvas_title("A Title for the whole Canvas")