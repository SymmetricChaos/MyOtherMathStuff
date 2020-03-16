import matplotlib.pyplot as plt
import numpy as np

def interpolation(A,B,p):
    """The point that is some exactly p percent of the way between A and B"""
    x = A[0]*(1-p) + B[0]*p
    y = A[1]*(1-p) + B[1]*p
    return [x,y]


def string_bezier2(P1=[0,1],P2=[1,0],n=15,size=5,colormap="plasma"):
    
    t = np.linspace(0,1,n)
    X0,Y0 = interpolation(P1,[0,0],t)
    X1,Y1 = interpolation([0,0],P2,t)

    #Higher order function to create a color function from the named colormap
    color_func = plt.get_cmap(colormap)

    fig = plt.figure()
    fig.set_size_inches(7,7)
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    for x0,y0,x1,y1,color_pt in zip(X0,Y0,X1,Y1,t):
        plt.plot([x0,x1],[y0,y1],color=color_func(color_pt))

    return X0,Y0,X1,Y1


# Change to use a closed curve
def string_stars(s=3,n=1):
    th = np.linspace(0,2*np.pi,s+1)
    p = [p for p in zip(np.sin(th), np.cos(th))]

    pos = n
    L = [p[0]]
    while pos != 0:
        L.append(p[pos])
        pos = (pos+n)%s
    L.append(p[0])

    x = [pt[0] for pt in L]
    y = [pt[1] for pt in L]

    
    fig = plt.figure()
    fig.set_size_inches(7,7)
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    
    plt.plot(x,y)
    
    return x,y
    

if __name__ == '__main__':
    string_bezier2([-.5,1],n=35,colormap="winter")
    
    string_stars(50,15)