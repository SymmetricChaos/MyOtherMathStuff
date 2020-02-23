import matplotlib.pyplot as plt
import numpy as np

def rose_path(k):
    pts = np.linspace(0,2*np.pi,1000)
    pts_spaced = pts*k
    
    x = np.cos(pts_spaced)*np.cos(pts)
    y = np.cos(pts_spaced)*np.sin(pts)
    
    return x,y
    
x,y = rose_path(7)

fig = plt.figure()
fig.set_size_inches(10,10)
plt.axes().set_aspect("equal","datalim")
plt.axis("off")
plt.plot(x,y)