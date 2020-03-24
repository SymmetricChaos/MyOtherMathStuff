import matplotlib.pyplot as plt
import numpy as np
from mbline import mbline
from Spirogram import trochoid
from Normals import normals
from Tangents import tangents
from SimpleCurves import ellipse

def double_ellipse():
    x,y = ellipse(1,2,501)
    m1,b1 = normals(x,y,draw=False)
    m2,b2 = tangents(x,y,draw=False)
    
    fig = plt.figure()
    fig.set_size_inches(14,14)
    ax = plt.axes(xlim=(-4.5,4.5), ylim=(-4.5,4.5))
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    mbline(m1,b1,alpha=.05,color='red')
    mbline(m2[1:],b2[1:],alpha=.05,color='red')
    
    

if __name__ == "__main__":
    double_ellipse()