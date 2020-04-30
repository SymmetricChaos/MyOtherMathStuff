import numpy as np
import matplotlib.pyplot as plt
#from Conversions import xy_to_points, points_to_xy
from Drawing import make_blank_canvas, draw_curve_xy, draw_dots_xy


# Difference between prediction f(x) and observed value y at x
def residual(x,y,f):
    return y - f(x)


# Quick function to evaluate a polynomial function
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


# Run regressions on numerous random subsets of the data
def bagged_regression(X,Y,degree=1,runs=20):

    for i in range(runs):
        R = np.random.random_integers(0,len(X)-1,len(X)//2)
        x_sub = [X[r] for r in R]
        y_sub = [Y[r] for r in R]
        yield polynomial_regression(x_sub,y_sub,degree)
        
    






if __name__ == '__main__':
    
    x1 = x2 = np.linspace(-1,6,300)
    y0 = np.cos(x1)
    y1 = np.cos(x1)+np.random.normal(0,.3,300)
    c = polynomial_regression(x1,y1,4)
    y2 = poly(x1,c)
    x3,y3 = simple_local_regression(x1,y1,width=.5,n=100,degree=1)
    
    
    make_blank_canvas(xlim=(-2,7),ylim=(-2,2),size=(12.5,6))
    draw_dots_xy(x1,y1,s=5)
    draw_curve_xy(x2,y2)
    draw_curve_xy(x1,y0,color='red')
    plt.title("4th Degree Polynomial Regression Curve",size=20)
    
    
    make_blank_canvas(xlim=(-2,7),ylim=(-2,2),size=(12.5,6))
    draw_dots_xy(x1,y1,s=5)
    for P in bagged_regression(x1,y1,4,runs=50):
        draw_curve_xy(x1,poly(x1,P),alpha=.2)
    draw_curve_xy(x1,y0,color='red')
    plt.title("4th Degree Polynomial Regression Curves on Random Subsets",size=20)


    