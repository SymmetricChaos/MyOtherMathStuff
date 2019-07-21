import matplotlib.pyplot as plt

def make_canvas(x,y=None,size=[7,7]):
    if not y:
        y = x
    fig = plt.figure()
    fig.set_size_inches(size[0], size[1])
    ax = plt.axes(xlim=x, ylim=y)
    ax.axis('off')
    return fig, ax