import numpy as np
import matplotlib.pyplot as plt


def simple_sandpile(width=101,size=pow(2,14)):
    

    G = np.zeros((width,width),dtype=int)
    G[width//2][width//2] = size

    while(True):
        c = (G > 3).sum()
        if(c == 0):
            break
        x = np.where(G >= 4)
        m = G[x]//4
        G[x] = G[x] % 4
        G[x[0]+1,x[1]] += m
        G[x[0]-1,x[1]] += m
        G[x[0],x[1]+1] += m
        G[x[0],x[1]-1] += m
    return(G)

x = simple_sandpile()

fig = plt.figure()
fig.set_size_inches(10,10)
ax = plt.Axes(fig,[0.,0.,1.,1.])
ax.set_axis_off()
fig.add_axes(ax)
plt.imshow(x,cmap='Accent',interpolation='none')