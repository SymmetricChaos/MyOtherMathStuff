import matplotlib.pyplot as plt

def make_canvas(x=[-3,3],y=[-3,3],size=[7,7]):
    fig = plt.figure()
    fig.set_size_inches(size[0], size[1])
    ax = plt.axes(xlim=x, ylim=y)
    ax.axis('off')
    return fig, ax

def lists_to_tuples(*args):
    """Convert lists to a list of tuples"""
    L = []
    for i in zip(*args):
        L.append(i)
    return L


def tuples_to_lists(L):
    """Convert a list of tuples to lists"""
    out = []
    W = len(L[0])
    for w in range(W):
        out.append( [i[w] for i in L] )
    return out