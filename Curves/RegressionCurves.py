import numpy as np
import matplotlib.pyplot as plt
from Conversions import xy_to_points, points_to_xy

# Difference between prediction f(x) and observed value y at x
def residual(x,y,f):
    return y - f(x)


# Polynomial function
def poly(x,coefs):
    out = 0
    for p,c in enumerate(coefs):
        out += c*x**p
    return out
    

#http://polynomialregression.drque.net/math.html
# Find a polynomial that fits some dataset using least squares
# Returns coefficients in ascending order
def polynomial_regression(X,Y,degree=2):
    
    N = degree+1
    
    M = np.matrix( [[0]*N]*N )
    T = np.matrix( [[0]*N] )
    
    # Each antidiagonal of M is a sum of powers of the x values
    # There is a precision loss issue with numpy matricies when the degree is high
    D = dict()
    for i in range(2*N):
        S = sum([x**i for x in X])
        D[i] = S
        
    for i in range(N):
        for j in range(N):
            M[i,j] = D[i+j]
        T[0,i] = sum([y*x**i for x,y in zip(X,Y)])
    
    out = M.I*T.T
    
    return [float(i[0]) for i in out]
    

# Basically works but a bit unstable
def local_regression(X,Y,width,n,degree=1):
    
    C = np.linspace(min(X),max(X),n)
    P = xy_to_points(X,Y)
    
    out = []
    
    def inrange(x,c,w):
        return x>c-w and x<c+w
    
    for cen in C:
        xy = [p for p in P if inrange(p[0],cen,width)]
        x,y = points_to_xy(xy)
        coef = polynomial_regression(x,y,degree=degree)
        
        out.append(poly(cen,coef))

    return C,out



if __name__ == '__main__':
    
    x = np.linspace(-1,7,100)
    y1 = np.cos(x)+np.random.normal(0,.3,100)
    c = polynomial_regression(x,y1,4)
    y2 = poly(x,c)
    x2,y3 = local_regression(x,y1,.5,30,1)
    
    plt.title([round(i,3) for i in c])
    plt.scatter(x,y1)
    plt.plot(x,y2)
    plt.plot(x2,y3)