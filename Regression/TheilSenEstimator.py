import numpy as np
import matplotlib.pyplot as plt
from Conversions import xy_to_points
from Drawing import make_blank_canvas, mbline, draw_dots_xy



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





if __name__ == '__main__':
    
    x = np.linspace(0,10,50)
    y = x+np.random.normal(0,.25,50)*x
    
    m,b = theil_sen_estimator(x,y)
    
    make_blank_canvas()
    draw_dots_xy(x,y)
    mbline(m,b)
    plt.title("Theil-Sen Estimator With Heteroskedastic Data",size=20)