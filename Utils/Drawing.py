import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.patches as patches
from Utils.PointTypes import points_to_xy
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data
from matplotlib.table import table as mpltable



### DRAWING SURFACES ###
def make_blank_canvas(size=[12,12],**kwargs):
    fig = plt.figure(**kwargs)
    fig.set_size_inches(size[0],size[1])
    return fig


def make_plot(a=1,b=1,p=1,xlim=None,ylim=None,fig=None,**kwargs):
    
    if fig == None:
        fig = plt.gcf()
        
    ax = fig.add_subplot(a,b,p,**kwargs)
    
    # If no coordinate range is given fit everything into a square
    if not xlim and not ylim:
        pass
    # If only xrange is given fit a square
    elif not ylim:
        ax.set_xlim(xlim)
        ax.set_ylim(xlim)
    # If both are given fix the rectangle
    else:
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)

    return ax


def make_blank_plot(a=1,b=1,p=1,xlim=None,ylim=None,box=True,fig=None,**kwargs):

    if fig == None:
        fig = plt.gcf()
        
    ax = fig.add_subplot(a,b,p,**kwargs)
    
    # If no coordinate range is given fit everything into a square
    if not xlim and not ylim:
        pass
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




### STRAIGHT LINES ###
# Convenience functions for solving mbline equations
def calc_y(m,x,b):
    return m*x+b

def calc_x(m,y,b):
    return (y-b)/m

# Draw a line based on its slope-intercept form
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


# Draw an line given the point-slope form
def point_slope_line(P,m,xlim=[],ylim=[],ax=None,**kwargs):    
    b = m*P[1]+P[0]
    return mbline(m,b,xlim,ylim,ax,**kwargs)

# Draw multiple point-slope lines
def point_slope_lines(P,M,xlim=[],ylim=[],ax=None,**kwargs):    
    B = [m*p[0]+p[1] for m,p in zip(M,P)]
    return mblines(M,B,xlim,ylim,ax,**kwargs)
    

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


# Straight line connecting two points
def connect_p(A,B,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    line = lines.Line2D([A[0],B[0]], [A[1],B[1]], axes=ax,**kwargs)
    ax.add_line(line)

def connect_xy(X,Y,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    line = lines.Line2D([X[0],X[1]], [Y[0],Y[1]], axes=ax,**kwargs)
    ax.add_line(line)


# Straight arrow connecting two points
def arrow_p(A,B,ax=None,facecolor="black",edgecolor="black",**kwargs):
    if ax == None:
        ax = plt.gca()
    dx = B[0]-A[0]
    dy = B[1]-A[1]
    ax.arrow(A[0],A[1],dx,dy,facecolor=facecolor,edgecolor=edgecolor,**kwargs)

def arrow_xy(X,Y,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    dx = X[1]-X[0]
    dy = Y[1]-Y[0]
    ax.arrow(X[0],Y[0],dx,dy,**kwargs)





### CURVES ###
# Draw an open curve
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


# Draw a closed curve that attaches the start to the end
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





### TEXT ###
def title(text="",ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    ax.set_title(text,**kwargs)


def canvas_title(text="",fig=None,**kwargs):
    if fig == None:
        fig = plt.gcf()
    fig.suptitle(text,**kwargs)
    
    
def text_xy(x,y,t,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    ax.text(x,y,t,**kwargs)


def text_p(P,t,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    ax.text(P[0],P[1],t,**kwargs)
        

def table(cell_text,yscale=1,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
        
    T = mpltable(cellText = cell_text,ax=ax,**kwargs)
    T.scale(1,yscale)
    
    return ax.add_table(T)





### CIRCLES ###
def draw_circle_xy(X,Y,R,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    circle = plt.Circle((X,Y), radius=R, **kwargs)
    ax.add_patch(circle)
    return circle

def draw_circle_p(P,R,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    circle = plt.Circle(P, radius=R, **kwargs)
    ax.add_patch(circle)
    return circle


# Convenience for drawing many circles with varying position and size but
# identical for all other arguments
def draw_circles_xy(X,Y,R,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    circles = []
    for x,y,r in zip(X,Y,R):  
        C = draw_circle_xy(x,y,r,ax,**kwargs)
        circles.append(C)
    return circles

def draw_circles_p(P,R,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    circles = []
    for p,r in zip(P,R):  
        C = draw_circle_p(p,r,ax,**kwargs)
        circles.append(C)
    return circles





### RECTANGLE ###
def draw_rect_xy(x0,y0,x1,y1,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    rect = patches.Rectangle([x0,y0],x1-x0,y1-y0,**kwargs)
    ax.add_patch(rect)
    return rect





### IMAGES ###
def image(path,x=0,y=0,scale=1,ax=None):
    if ax == None:
        ax = plt.gca()
        
    with get_sample_data(path) as file:
        arr_img = plt.imread(file, format='png')
    
    imagebox = OffsetImage(arr_img, zoom=scale)
    
    ab = AnnotationBbox(imagebox, [x,y],
                        xycoords='data',
                        boxcoords="offset points",
                        frameon=False)

    ax.add_artist(ab)
    

def image_box(path,x=0,y=0,scale=1,pad=0,ax=None):
    if ax == None:
        ax = plt.gca()
        
    with get_sample_data(path) as file:
        arr_img = plt.imread(file, format='png')
    
    imagebox = OffsetImage(arr_img, zoom=scale)
    
    ab = AnnotationBbox(imagebox, [x,y],
                        xycoords='data',
                        boxcoords="offset points",
                        frameon=True,
                        pad=pad)

    ax.add_artist(ab)





### SHOW ###
def show_now():
    plt.show()





### MATHEMATICAL PLOTS ###
# Scatter plots
def draw_dots_xy(x,y,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    ax.scatter(x,y,**kwargs)

def draw_dots_p(P,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    x,y = points_to_xy(P)
    ax.scatter(x,y,**kwargs)

    
def histogram(L,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    return ax.hist(L,**kwargs)


def pie_chart(L,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    return ax.pie(L,**kwargs)


def boxplot(L,ax=None,positions=[],labels=[],vert=True,**kwargs):
    if ax == None:
        ax = plt.gca()
    
    if positions == []:
        positions = [i for i in range(len(L))]
    
    return ax.boxplot(L,positions=positions,labels=labels,vert=vert,**kwargs)


def violin_plot(L,ax=None,positions=[],labels=[],vert=True,**kwargs):
    if ax == None:
        ax = plt.gca()
    
    # MPL doesn't support this by default like it does for boxplots
    if positions == []:
        positions = [i for i in range(len(L))]

    if labels != []:        
        if vert:
            ax.set_xticks(positions)
            ax.set_xticklabels(labels)
        else:
            ax.set_yticks(positions)
            ax.set_yticklabels(labels)
    
    return ax.violinplot(L,positions=positions,vert=vert,**kwargs)


def quiver_plot(X,Y,U,V,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
        
    return ax.quiver(X,Y,U,V)
