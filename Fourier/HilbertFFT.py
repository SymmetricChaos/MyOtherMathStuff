import numpy as np
from Utils import make_canvas,plot_points
from numpy.fft import fft2, ifft2
from Fractals.LSystem import LSystem

def hilbert_curve_rule(S):
    if S == "A":
        return "+BF-AFA-FB+"
    if S == "B":
        return "-AF+BFB+FA-"
    else:
        return S


def hilbert_points(n,**kwargs):

    for i in LSystem("B",hilbert_curve_rule,n+1):
        rules = i
    
    coords = [(0,0)]
    
    # Strip out anything unnceesaary for drawing
    rules = rules.replace("A","")
    rules = rules.replace("B","")
    rules = rules.replace("-+","")
    rules = rules.replace("+-","")
    while rules[0] == "+" or rules[0] == "-":
        rules = rules[1:]
        
    ang = n%2
    for i in rules:
        if i == "F":
            oldx = coords[-1][0] 
            oldy = coords[-1][1]
            if ang == 0:
                coords.append( (oldx,oldy+1) )
            elif ang == 1:
                coords.append( (oldx+1,oldy) )
            elif ang == 2:
                coords.append( (oldx,oldy-1) )
            elif ang == 3:
                coords.append( (oldx-1,oldy) )
        elif i == "-":
            ang = (ang-1)%4
        elif i == "+":
            ang = (ang+1)%4
    
    return coords

xy = hilbert_points(6)

f = fft2(xy)
print(f)

xy = ifft2(f[:-1])

xmax = max([i[0] for i in xy])
make_canvas([-(xmax/20),xmax+(xmax/20)],size=6)

plot_points(xy)