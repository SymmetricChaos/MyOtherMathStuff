from numpy import linspace
import matplotlib.pyplot as plt

def logistic_map(x,r,n,last=1):
    for i in range(n):
        if n > n-last:
            yield x
        x = r*x*(1-x)

X = []
Y = []
for x in linspace(-1.5,3.5,200):
    for y in logistic_map(.5,x,25):
        X.append(x)
        Y.append(y)
print(len(Y))
plt.scatter(X,Y,s=1)