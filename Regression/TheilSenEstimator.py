import numpy as np
import matplotlib.pyplot as plt
from Conversions import xy_to_points
from Drawing import make_blank_canvas, mbline, draw_dots_xy, make_blank_subplot



def points_to_slope(A,B):
    if A[0]-B[0] == 0:
        return float("Inf")
    return (A[1]-B[1])/(A[0]-B[0])


def theil_sen_estimator(X,Y):
    
    if len(X) != len(Y):
        raise Exception("Length of X and Y must match")
    
    n = len(X)
    
    points = xy_to_points(X,Y)
    
    # Find the median of the slopes
    slopes = []
    
    for i in range(n):
        for j in range(n):
            if i != j:
                m = points_to_slope(points[i],points[j])
                slopes.append(m)
    
    slope = np.median(slopes)
    
    intercepts = []
    
    for i in range(n):
        intercepts.append(points[i][1]-slope*points[i][0])
            
    intercept = np.median(intercepts)
    
    return slope, intercept


def repeated_medians(X,Y):
    
    if len(X) != len(Y):
        raise Exception("Length of X and Y must match")
    
    n = len(X)
    
    points = xy_to_points(X,Y)
    
    median_slopes = []
    for i in range(n):
        slopes = []
        for j in range(n):
            if i != j:
                m = points_to_slope(points[i],points[j])
                slopes.append(m)
        median_slopes.append(np.median(slopes))
    
    slope = np.median(median_slopes)
    
    intercepts = []
    
    for i in range(n):
        intercepts.append(points[i][1]-slope*points[i][0])
            
    intercept = np.median(intercepts)
    
    return slope, intercept





if __name__ == '__main__':
    
    from PolynomialRegression import linear_least_squares
    
    n_points = 100
    n_corrupted = 40
    x = np.linspace(0,12,n_points)
    y = x+np.random.normal(0,.5,n_points)
    
    # Corrupt the data with meaningless datapoints
    for i in range(n_corrupted):
        r = int(np.random.randint(0,n_points))
        y[r] = np.random.uniform(0,12,1)
    
    m1,b1 = theil_sen_estimator(x,y)
    m2,b2 = repeated_medians(x,y)
    m3,b3 = linear_least_squares(x,y)
    
    make_blank_canvas()
    for m,b,pos,T in zip([m1,m2,m3],[b1,b2,b3],[1,2,3],["Theil-Sen","Repeated Medians","Least Squares"]):
        make_blank_subplot(2,2,pos)
        draw_dots_xy(x,y,color='lightgrey',zorder=0)
        mbline(m,b,color='red',zorder=2)
        print(f"{T}\nm = {m:.3}\nb = {b:.3}\n")
        mbline(1,0,color='gray',linewidth=3,zorder=1)
        plt.title(T,size=20)