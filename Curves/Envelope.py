import matplotlib.pyplot as plt
import numpy as np
from mbline import mbline

def envelope(slopes,intercepts,draw=True):

    shifted_slopes = np.roll(slopes,1)
    shifted_intercepts = np.roll(intercepts,1)

    x = (shifted_intercepts-intercepts)/(slopes-shifted_slopes)
    y = slopes*x+intercepts
    
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(12,12)
        ax = plt.axes(xlim=(-5,5), ylim=(-5,5))
        ax.axis('off')
        ax.set_xticks([])
        ax.set_yticks([])
        
    plt.plot(x,y)
    return x,y





if __name__ == '__main__':
    from Normals import normals
    from SimpleCurves import ellipse
    
    fig = plt.figure()
    fig.set_size_inches(12,12)
    ax = plt.axes(xlim=(-5,5), ylim=(-5,5))
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])

    x,y = ellipse(2,1,n=201)
    m,b = normals(x,y,draw=False)
    x1,y1 = envelope(m,b,draw=False)
    
    plt.plot(x,y)
    plt.plot(x1,y1)
    mbline(m,b,[-4,4],alpha=.1)
