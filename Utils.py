import matplotlib.pyplot as plt

def make_canvas(x=[-3,3],y=[-3,3],size=[7,7]):
    fig = plt.figure()
    fig.set_size_inches(size[0], size[1])
    ax = plt.axes(xlim=x, ylim=y)
    ax.axis('off')
    return fig, ax