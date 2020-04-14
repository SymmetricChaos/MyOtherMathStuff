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
def polynomial_regression(X,Y,degree=2):
    
    degree = degree+1
    
    M = np.matrix( [[0]*degree]*degree )
    T = np.matrix( [[0]*degree] )
    
    # Each antidiagonal is a sum of power
    # There's definitely a more efficient way to do this but we run out of
    # precision from long ints before it becomes an issue
    for i in range(degree):
        for j in range(degree):
            M[i,j] = sum([x**(i+j) for x in X])
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