from Utils.Drawing import make_canvas
import matplotlib.pyplot as plt
from numpy import linspace


def B_order_0(x,i,knots):
    if knots[i] <= x and x <= knots[i+1]:
        return 1
    return 0

def B_spline_recur(x,i,order,knots):
    if order == 0:
        return B_order_0(x,i,knots)
    else:
        lower_1 = B_spline_recur(x,i,order-1,knots)
        cons_1 = (x-knots[i])/(knots[i+order]-knots[i])
        
        lower_2 = B_spline_recur(x,i+1,order-1,knots)
        cons_2 = (knots[i+order+1]-x)/(knots[i+order+1]-knots[i+1])
        
        return lower_1*cons_1 + lower_2*cons_2

# To be a wrapper function
#def B_spline(knots):
    
    
        

knots = [0,1,2,3,4,5]
control = [0,1,0]
degree = len(knots)-len(control)-1

print(degree)

# B-Splines of order zero are step functions
make_canvas([0,5])
for i in range(5):
    X = []
    Y = []
    for pt in linspace(0,5,100):
        X.append(pt)
        Y.append(B_order_0(pt,i,knots))
        
    plt.plot(X,Y)
    
# B-Splines of order one are triangles
make_canvas([0,5])
for i in range(4):
    X = []
    Y = []
    for pt in linspace(0,5,100):
        X.append(pt)
        Y.append(B_spline_recur(pt,i,1,knots))
        
    plt.plot(X,Y)
    
# B-Splines of order one are triangles
make_canvas([0,5])
for i in range(3):
    X = []
    Y = []
    for pt in linspace(0,5,100):
        X.append(pt)
        Y.append(B_spline_recur(pt,i,2,knots))
        
    plt.plot(X,Y)