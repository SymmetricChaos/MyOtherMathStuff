import matplotlib.pyplot as plt
import numpy as np
from mbline import mbline
from Spirogram import trochoid
from Normals import normals
from Tangents import tangents
from SimpleCurves import ellipse

def double_ellipse():
    x,y = ellipse(1,2)
    m1,b1 = normals(x,y,draw=False)
    m2,b2 = tangents(x,y,draw=False)
    
    fig = plt.figure()
    fig.set_size_inches(12,12)
    ax = plt.axes(xlim=(-6,6), ylim=(-6,6))
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    mbline(m1[1:],b1[1:],alpha=.02,color='red')
    mbline(m2,b2,alpha=.02,color='blue')
    
    

if __name__ == "__main__":
    double_ellipse()