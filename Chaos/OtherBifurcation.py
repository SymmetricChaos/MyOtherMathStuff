from numpy import linspace
import matplotlib.pyplot as plt
from Utils import make_canvas
from math import sqrt, sin

# A function that calculates the logistic function out to n iterations and
# returns the last few
def bifurcation_map(x,r,n,last=1):
    for i in range(n):
        if i > n-last:
            yield x
        x = r*sin(sqrt(x)*3.14)
        
        
xmin = 0
xmax = 1

# Calculate for various values of r
X = []
Y = []
for x in linspace(xmin,xmax,1000):
    for y in bifurcation_map(.5,x,200,100):
        X.append(x)
        Y.append(y)

# In order to see the attractors we use transparent dots
make_canvas([xmin,xmax],[-.5,1.5],[15,15])
plt.scatter(X,Y,s=1,alpha=.1)
 