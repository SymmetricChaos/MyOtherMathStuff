import matplotlib.pyplot as plt
import matplotlib.lines as lines
from Conversions import complex_to_xy, points_to_xy

def make_blank_canvas(xrange=None,yrange=None,size=[12,12]):
    fig = plt.figure()
    fig.set_size_inches(size[0],size[1])
    # If no coordinate range is given fit everything into a square
    if not xrange and not yrange:
        ax = plt.axes()
        ax.set_aspect("equal","datalim")
    # If only xrange is given fit a square
    elif not yrange:
        ax = plt.axes(xlim=xrange,ylim=xrange)
    # If both are given fix the rectangle
    else:
        ax = plt.axes(xlim=xrange,ylim=yrange)
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    return fig,ax


def make_blank_subplot(a,b,p,xrange=None,yrange=None,box=True):
    
    ax = plt.subplot(a,b,p)
    
    # If no coordinate range is given fit everything into a square
    if not xrange and not yrange:
        ax.set_aspect("equal","datalim")
    # If only xrange is given fit a square
    elif not yrange:
        ax.set_xlim(xrange)
        ax.set_ylim(xrange)
    # If both are given fix the rectangle
    else:
        ax.set_xlim(xrange)
        ax.set_ylim(yrange)
    
    if box == False:
        ax.axis('off')
        
    ax.set_xticks([])
    ax.set_yticks([])
    
    return ax


def calc_y(m,x,b):
    return m*x+b


def calc_x(m,y,b):
    return (y-b)/m


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
    
    return [[x0,y0],[x1,y1]]


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


def vertical_line(xpos=0,ylim=[],ax=None,**kwargs):
    
    if ax == None:
        ax = plt.gca()
        
    if ylim == []:
        ylim = ax.get_ylim()
        
    line = lines.Line2D([xpos,xpos],ylim, axes=ax,**kwargs)
    ax.add_line(line)
    
    
def horizontal_line(ypos=0,xlim=[],ax=None,**kwargs):
    
    if ax == None:
        ax = plt.gca()
        
    if xlim == []:
        xlim = ax.get_xlim()
    
    line = lines.Line2D(xlim,[ypos,ypos], axes=ax,**kwargs)
    ax.add_line(line)


# Draw a curve from:
#   seperate lists of x and y coordinates
#   a list of (x,y) points
#   a list of complex numbers
def draw_curve_xy(x,y,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    line = lines.Line2D(x,y, axes=ax,**kwargs)
    ax.add_line(line)

def draw_curve_points(P,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    x,y = points_to_xy(P)
    line = lines.Line2D(x,y, axes=ax,**kwargs)
    ax.add_line(line)

def draw_curve_complex(C,ax=None,**kwargs):
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
    
def draw_closed_curve_points(P,ax=None,**kwargs):
    x,y = points_to_xy(P)
    draw_closed_curve_xy(x,y,ax,**kwargs)
    
def draw_closed_curve_complex(P,ax=None,**kwargs):
    x,y = complex_to_xy(P)
    draw_closed_curve_xy(x,y,ax,**kwargs)
    

# Draw scatterplot from:
#   seperate lists of x and y coordinates
#   a list of (x,y) points
#   a list of complex numbers
def draw_dots_xy(x,y,**kwargs):
    plt.scatter(x,y,**kwargs)

def draw_dots_points(P,**kwargs):
    x,y = points_to_xy(P)
    plt.scatter(x,y,**kwargs)

def draw_dots_complex(C,**kwargs):
    x,y = complex_to_xy(C)
    plt.scatter(x,y,**kwargs)


def connect(A,B,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    line = lines.Line2D([A[0],B[0]], [A[1],B[1]], axes=ax,**kwargs)
    ax.add_line(line)


if __name__ == '__main__':
    
    make_blank_canvas([-5,5],[-5,5])
    draw_curve_xy([1,2,3],[1,2,1])
    draw_closed_curve_xy([1,2,3],[0,1,0],color="green")
    horizontal_line(-2)
    vertical_line(1,color='brown')
    
    # Subplots example
    make_blank_canvas()
    
    # Make and use a subplot
    sp1 = make_blank_subplot(2,2,1)
    draw_closed_curve_xy([1,2,3],[0,1,0])
    
    # Subplots of different layouts can coexist
    sp2 = make_blank_subplot(4,4,4,[-2,2])
    draw_closed_curve_xy([1,2,3],[0,1,0])
    # Create an mbline on the most recently created axes
    mbline(1,1)
    
    # Plots can be created out of order
    sp3 = make_blank_subplot(2,2,4,[-3,3],[-5,5])
    draw_closed_curve_xy([1,2,3],[0,1,0])
    
    sp4 = make_blank_subplot(4,4,7,[-3,3])
    draw_closed_curve_xy([1,2,3],[0,1,0])
    
    # Add lines to a previous axis
    mblines([1,2,3,4,5],[0,0,0,0,0],ax=sp3)
    
    # mbline takes ylim and xlim from axes so it might get cut off
    mbline(1,-.4,ax=sp1)
    # mbline can be manually corrected
    mbline(1,-.6,ylim=[-2,2],ax=sp1,color='red')