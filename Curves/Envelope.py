import matplotlib.pyplot as plt
import numpy as np

def envelope(slopes,intercepts):

    shifted_slopes = np.roll(slopes,1)
    shifted_intercepts = np.roll(intercepts,1)
    
    print(slopes[:10])
    print(shifted_slopes[:10])
    
    x = (slopes-shifted_slopes)/(shifted_intercepts-intercepts)
    y = slopes*x+intercepts
    
#    fig = plt.figure()
#    fig.set_size_inches(12,12)
#    ax = plt.axes(xlim=(-5,5), ylim=(-5,5))
#    ax.axis('off')
#    ax.set_xticks([])
#    ax.set_yticks([])
#    
#    plt.plot(x,y)
    return x,y
        
        
if __name__ == '__main__':
    from Normals import normals
    from SimpleCurves import ellipse
    
    x,y = ellipse(1,2,81)
    m,b = normals(x,y,draw=True)
    x1,y1 = envelope(m,b)
    plt.plot(x,y)
    plt.scatter(x1,y1)