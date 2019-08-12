from DomainColoring import domain_coloring_contour
from numpy import sin

def func1(z):
    return (z*z*z)-5/z

def func2(z):
    return sin(z*z)*z+sin(z)*5

def func3(z):
    return sin(z)

r = 4
X = (-r,r)
Y = (-r,r)

for f in [func1,func2,func3]:

    domain_coloring_contour(f,X,Y,501)