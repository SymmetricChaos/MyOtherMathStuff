import matplotlib.pyplot as plt

def make_canvas(x,y=None,size=None):
    if not y:
        y = x
    if not size:
        xlim = abs(x[0]-x[1])
        ylim = abs(y[0]-y[1])
        xco = min(xlim,ylim)/ylim
        yco = min(xlim,ylim)/xlim
        size = [xco*7,yco*7]
    fig = plt.figure()
    fig.set_size_inches(size[0], size[1])
    ax = plt.axes(xlim=x, ylim=y)
    ax.axis('off')
    return fig, ax