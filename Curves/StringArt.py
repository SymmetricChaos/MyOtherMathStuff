import matplotlib.pyplot as plt
import numpy as np

def string_bezier2(n=15,size=5):
    
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    for i in np.linspace(0,1,n):
            plt.plot([i,0],[0,1-i])

string_bezier2()