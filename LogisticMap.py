from numpy import linspace
import matplotlib.pyplot as plt
from Utils import make_canvas

# A function that calculates the logistic function out to n iterations and
# returns the last few
def logistic_map(x,r,n,last=1):
    for i in range(n):
        if i > n-last:
            yield x
        x = r*x*(1-x)

# Calculate for various values of r
X = []
Y = []
for x in linspace(2,4,1000):
    for y in logistic_map(.5,x,100,30):
        X.append(x)
        Y.append(y)

# In order to see the attractors we use transparent dots
make_canvas([2,4],[-.5,1.5],[15,15])
plt.scatter(X,Y,s=1,alpha=.1)
