from Utils.Drawing import make_canvas
import matplotlib.pyplot as plt
from numpy import linspace

knots = [0,1,2,3]
control = [0,0,1,0,0]

def B_order_1(x,i,knots):
    if knots[i] <= x or x <= knots[i+1]:
        return 1
    return 0

def B_order_2(x,i,knots):
    cons_a = (x-knots[i])/(knots[i+1]-knots[i])
    cons_b = (knots[i+1+1] - x)/(knots[i+1+1] - knots[i+1])
    return cons_a*B_order_1(x,i,knots) + cons_b*B_order_1(x,i+1,knots)

X = []
Y = []
for pt in linspace(-2,2,50):
    X.append(pt)
    Y.append(B_order_1(pt,1,knots))
    
plt.plot(X,Y)