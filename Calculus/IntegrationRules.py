import matplotlib.pyplot as plt
import numpy as np


## The rectangular rule
def rect_rule(func,a,b,s):
    out = 0
    while a < b:
        out += s*func((2*a+s)/2)
        a += s
    return out

## The trapezoidal rule
def trap_rule(func,a,b,s):
    out = 0
    while a < b:
        out += s*(func(a)+func(a+s))/2
        a += s
    return out

## Some weird function
def func(x):
    return x**4/15 + x**3/3 - 2*x**2 - 4*x + 10 + 8*np.sin(x)



x = np.arange(-5,5,.1)
y = func(x)

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
    