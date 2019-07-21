from numpy import linspace
import matplotlib.pyplot as plt
from Utils import make_canvas

def logistic_map(x,r,n,last=1):
    for i in range(n):
        if i > n-last:
            yield x
        x = r*x*(1-x)

X = []
Y = []
for x in linspace(0,3.7,1000):
    for y in logistic_map(.5,x,50,20):
        X.append(x)
        Y.append(y)
print(len(Y))


make_canvas([0,4],[-.5,1.5],[12,8])
plt.scatter(X,Y,s=1,alpha=.2)
