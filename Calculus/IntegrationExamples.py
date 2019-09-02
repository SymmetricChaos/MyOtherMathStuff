import matplotlib.pyplot as plt
import numpy as np
from IntegrationRules import rect_rule, trap_rule
from Utils.Drawing import make_canvas
from Geometry.Polygons import Polygon

## Some weird function
def func(x):
    return x**4/15 + x**3/3 - 2*x**2 - 4*x + 10 + 8*np.sin(x)



x = np.arange(-5,5,.1)
y = func(x)

make_canvas([-5,5],[-12,12])
plt.plot(x,y)
plt.fill_between(x,y,facecolor='lightgray')
plt.plot([-5,5],[0,0],"k-")

print("Area under the curve from -5 to 5")
for i in [1,.5,.1]:
    R = rect_rule(func,-5,5,i)
    T = trap_rule(func,-5,5,i)
    print("Step size {}".format(i))
    print("By the rectangular rule {:.3f}".format(R))
    print("By the trapezoidal rule {:.3f}".format(T))

make_canvas([-5.1,5.1],[-14,14])
plt.plot(x,y)
plt.plot([-5,5],[0,0],"k-")
a, b = -5, 5
s = .5
while a < b:
    P = Polygon([[a,0],
                 [a,func(a)],
                 [a+s,func(a)],
                 [a+s,0]
                ])
    P.draw(facecolor="#11111111")
    a += s
    
make_canvas([-5.1,5.1],[-14,14])
plt.plot(x,y)
plt.plot([-5,5],[0,0],"k-")
a, b = -5, 5
s = .5
while a < b:
    P = Polygon([[a,0],
                 [a,func(a)],
                 [a+s,func(a+s)],
                 [a+s,0]
                ])
    P.draw(facecolor="#11111111")
    a += s