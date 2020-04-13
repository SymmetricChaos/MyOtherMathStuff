import matplotlib.pyplot as plt
import numpy as np

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


def draw_curve(x,y=None,**kwargs):
    if not y:
        plt.plot([i[0] for i in x],[i[1] for i in x],**kwargs)
    else:
        plt.plot(x,y,**kwargs)
    
    
def draw_closed_curve(x,y=None,**kwargs):
    if not y:
        x += [x[0]]
        plt.plot([i[0] for i in x],[i[1] for i in x],**kwargs)
    else:
        x += [x[0]]
        y += [y[0]]
        plt.plot(x,y,**kwargs)
    
    
def draw_dots(x,y=None,**kwargs):
    if not y:
        plt.scatter([i[0] for i in x],[i[1] for i in x],**kwargs)
    else:
        plt.scatter(x,y,**kwargs)





if __name__ == '__main__':
    
    make_blank_canvas([-5,5],[-5,5])
    draw_curve([1,2,3],[0,1,0])
    
    make_blank_canvas([-5,5],[-5,5])
    draw_closed_curve([1,2,3],[0,1,0])