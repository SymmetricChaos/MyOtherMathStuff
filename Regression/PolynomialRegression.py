import numpy as np
import matplotlib.pyplot as plt
#from Conversions import xy_to_points, points_to_xy
from Drawing import make_blank_canvas, make_blank_subplot, draw_curve_xy, draw_dots_xy





# Quick function to evaluate a polynomial function
def poly(x,coefs):
    out = 0
    for p,c in enumerate(coefs):
        out += c*x**p
    return out


#http://polynomialregression.drque.net/math.html
# Find a polynomial that fits some dataset using least squares
# Returns coefficients in ascending order
def ordinary_least_squares(X,Y,degree=1):
    
    if len(X) != len(Y):
        raise Exception("Length of X and Y must match")
    
    if len(X) <= degree:
        raise Exception("Must have strictly more points than the degree of the polynomial fitted")
    
    N = degree+1
    
    M = np.matrix( [[0]*N]*N )
    T = np.matrix( [[0]*N] )
    
    # Each antidiagonal of M is a sum of powers of the x values
    # There is a precision issue with numpy matricies when the degree is high
    # since the values of the sums get too high to write as 64 bit floats
    D = dict()
    for i in range(2*N):
        S = sum([x**i for x in X])
        D[i] = S
        
    for i in range(N):
        for j in range(N):
            M[i,j] = D[i+j]
        T[0,i] = sum([y*x**i for x,y in zip(X,Y)])
    
    # Solve the system of linear equations
    out = M.I*T.T
    
    return [float(i[0]) for i in out]


# Convenience function that returns the coefficients of a OLS linear regression
# in the order "slope" then "intercept"
def linear_least_squares(X,Y):
    b,m = ordinary_least_squares(X,Y)
    return m,b


# Least squares with weighted values
def weighted_least_squares(X,Y,degree=1,weights=[]):
    
    if len(X) != len(Y):
        raise Exception("Length of X and Y must match")
    
    if len(X) <= degree:
        raise Exception("Must have strictly more points than the degree of the polynomial fitted")
    
    N = degree+1
    
    M = np.matrix( [[0]*N]*N )
    T = np.matrix( [[0]*N] )
    
#    # Each antidiagonal of M is a sum of powers of the x values
#    # There is a precision issue with numpy matricies when the degree is high
#    # since the values of the sums get too high to write as 64 bit floats
#    D = dict()
#    for i in range(2*N):
#        S = sum([x**i for x in X])
#        D[i] = S
#        
#    for i in range(N):
#        for j in range(N):
#            M[i,j] = D[i+j]
#        T[0,i] = sum([y*x**i for x,y in zip(X,Y)])
#    
#    # Solve the system of linear equations
#    out = M.I*T.T
#    
#    return [float(i[0]) for i in out]


# Run regressions on numerous random subsets of the data
def bagged_regression(X,Y,degree=1,runs=20):

    for i in range(runs):
        R = np.random.random_integers(0,len(X)-1,len(X)//2)
        x_sub = [X[r] for r in R]
        y_sub = [Y[r] for r in R]
        yield ordinary_least_squares(x_sub,y_sub,degree)
        
    



if __name__ == '__main__':
    
    x1 = x2 = np.linspace(-1,6,300)
    y0 = np.cos(x1)
    y1 = np.cos(x1)+np.random.normal(0,.3,300)

    
    make_blank_canvas(size=[15,15])
    
    for deg in [1,2,3,4]:
        
        c = ordinary_least_squares(x1,y1,deg)
        y2 = poly(x1,c)
        
        make_blank_subplot(2,2,deg,xlim=(-2,7),ylim=(-2,2))
        draw_dots_xy(x1,y1,s=5,color="lightgrey")
        draw_curve_xy(x2,y2)
        draw_curve_xy(x1,y0,color='red')
        plt.title(f"Degree {deg} Polynomial Regression",size=20)
        
    
    make_blank_canvas(xlim=(-2,7),ylim=(-2,2),size=(12.5,6))
    draw_dots_xy(x1,y1,s=5,color="lightgrey")
    for P in bagged_regression(x1,y1,4,runs=50):
        draw_curve_xy(x1,poly(x1,P),alpha=.2)
    draw_curve_xy(x1,y0,color='red')
    plt.title("4th Degree Polynomial Regressions on Random Subsets",size=20)


    