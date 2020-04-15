import numpy as np
import matplotlib.pyplot as plt


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
    
    


if __name__ == '__main__':
    
    x = np.linspace(-1,7,100)
    y1 = np.cos(x)+np.random.normal(0,.3,100)
    c = polynomial_regression(x,y1,4)
    y2 = poly(x,c)
    
    plt.scatter(x,y1)
    plt.plot(x,y2)