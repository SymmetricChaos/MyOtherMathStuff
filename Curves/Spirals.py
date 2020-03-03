import numpy as np
import matplotlib.pyplot as plt
from SimpleCurves import polar_to_cart

def archimedian_spiral(a=0,b=1,turns=1,n=1001):
    th = np.linspace(0,2*turns*np.pi,n)
    
    r = a+(b*th)
    
    return polar_to_cart(r,th)

x,y = archimedian_spiral(turns=2)

plt.plot(x,y)