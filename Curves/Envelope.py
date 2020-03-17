import matplotlib.pyplot as plt
import numpy as np

def envelope(slopes,intercepts,roll=True,draw=True):

    if roll == True:
        shifted_slopes = np.roll(slopes,1)
        shifted_intercepts = np.roll(intercepts,1)
    else:
        shifted_slopes = slopes[1:]
        shifted_intercepts = intercepts[1:]
        slopes = slopes[:-1]
        intercepts = intercepts[:-1]
        
    
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
    
    x,y = ellipse(2,1,n=101)
    x,y = x[:25],y[:25]
    m,b = normals(x,y,size=8,color="salmon",alpha=.5)
    plt.plot(x,y)
    
    x1,y1 = envelope(m,b,roll=False,draw=False)
    plt.plot(x1,y1)