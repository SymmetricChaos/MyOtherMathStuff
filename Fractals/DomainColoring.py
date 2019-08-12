# http://nbviewer.jupyter.org/github/empet/Math/blob/master/DomainColoring.ipynb

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import hsv_to_rgb

def Hcomplex(z): # compute the hue (color) based on angle
    H=np.angle(z)/(2*np.pi)+1
    return np.mod(H,1)

def Vcomplex(z): # compute the value (darkess) based on absolute value
    x = np.absolute(z)
    return (1.0-1/(1+x**4))**0.1


def domain_coloring(f, X = (-1,1), Y = (-1,1), res = 3000):
    xx = np.linspace(X[0],X[1],res) 
    yy = np.linspace(Y[0],Y[1],res) 
    x,y = np.meshgrid(xx,yy)
    z = x + 1j*y
    
    w = f(z)
    
    infpos = np.where(np.isinf(w)) #find infinities
    nanpos = np.where(np.isnan(w)) #find NaNs
    
    # Calculate hue, saturation, and value
    H = Hcomplex(w)
    S = 0.9*np.ones_like(H)
    V = Vcomplex(w)

    
    # Make infinities white
    H[infpos] = 0.0 
    S[infpos] = 0.0  
    V[infpos] = 1.0
    
    # Make NaNs gray
    H[nanpos] = 0.0 
    S[nanpos] = 0.0  
    V[nanpos] = 0.5

    HSV = np.dstack((H,S,V))
    RGB = hsv_to_rgb(HSV)
    
    fig = plt.figure()
    fig.set_size_inches(10,10)
    ax = plt.Axes(fig,[0.,0.,1.,1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    
    plt.imshow(RGB,interpolation="bicubic")
    
def domain_coloring_contour(f, X = (-1,1), Y = (-1,1), res = 3000):
    xx = np.linspace(X[0],X[1],res,dtype=np.float64) 
    yy = np.linspace(Y[0],Y[1],res,dtype=np.float64) 
    x,y = np.meshgrid(xx,yy)
    z = x + 1j*y
    
    w = f(z)
    
    infpos = np.where(np.isinf(w)) #find infinities
    nanpos = np.where(np.isnan(w)) #find NaNs
    
    # Calculate hue and saturation
    H = Hcomplex(w)
    S = 0.9*np.ones_like(H)

    # Calculate value (darkness) contours based on fractional part
    # of the logarithm of the absolute valaue
    modulus=np.absolute(w)
    Logm=np.log(modulus)
    Logm=np.nan_to_num(Logm)
    V=Logm-np.floor(Logm)
    V = V**0.4
    
    # Make infinities white
    H[infpos] = 0.0 
    S[infpos] = 0.0  
    V[infpos] = 1.0
    
    # Make NaNs gray
    H[nanpos] = 0.0 
    S[nanpos] = 0.0  
    V[nanpos] = 0.5

    HSV = np.dstack((H,S,V))
    RGB = hsv_to_rgb(HSV)

    fig = plt.figure()
    fig.set_size_inches(10,10)
    ax = plt.Axes(fig,[0.,0.,1.,1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    plt.imshow(RGB,interpolation="bicubic")