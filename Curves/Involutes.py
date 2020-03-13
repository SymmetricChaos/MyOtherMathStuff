import numpy as np
import matplotlib.pyplot as plt

def circle_involute(t=0,r=1,turns=1,n=1001,draw=True):
    
    th = np.linspace(t,2*turns*np.pi+t,n)
    x = r*(np.cos(th)+(th-t)*np.sin(th))
    y = r*(np.sin(th)-(th-t)*np.cos(th))

    if draw:
        fig = plt.figure()
        fig.set_size_inches(7,7)
        ax = plt.axes()
        ax.set_aspect("equal","datalim")
        ax.axis('off')
        ax.set_xticks([])
        ax.set_yticks([])
        
        plt.plot(x,y)
        
    return x,y

def ellipse_involute(t=0,a=1,b=1,turns=1,n=1001,draw=True):
    
    th = np.linspace(t,2*turns*np.pi+t,n)
    x = a*(np.cos(th)+(th-t)*np.sin(th))
    y = b*(np.sin(th)-(th-t)*np.cos(th))

    if draw:
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
    fig = plt.figure()
    fig.set_size_inches(7,7)
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
    x1,y1 = circle_involute(t=0,turns=1,draw=False)
    x2,y2 = circle_involute(t=2,turns=1,draw=False)
    x3,y3 = circle_involute(t=4,turns=1,draw=False)
    
    th = np.linspace(0,2*np.pi,101)
    x,y = np.sin(th), np.cos(th)
    plt.plot(x,y)
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.plot(x3,y3)



    fig = plt.figure()
    fig.set_size_inches(7,7)
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
    x1,y1 = ellipse_involute(t=0,a=1,b=3,turns=1,draw=False)
    x2,y2 = ellipse_involute(t=2,a=1,b=3,turns=1,draw=False)
    x3,y3 = ellipse_involute(t=4,a=1,b=3,turns=1,draw=False)
    
    th = np.linspace(0,2*np.pi,101)
    x,y = np.sin(th), 3*np.cos(th)
    plt.plot(x,y)
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.plot(x3,y3)