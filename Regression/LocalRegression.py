import numpy as np
import matplotlib.pyplot as plt
from Conversions import xy_to_points, points_to_xy
from Drawing import make_blank_canvas, draw_curve_xy, draw_dots_xy
from PolynomialRegression import polynomial_regression, poly

# Basically works but a bit unstable
def simple_local_regression(X,Y,width,n,degree=1):
    
    C = np.linspace(min(X),max(X),n)
    P = xy_to_points(X,Y)
    
    out = []
    
    def inrange(x,c,w):
        return x>=c-w and x<=c+w
    
    for cen in C:
        xy = [p for p in P if inrange(p[0],cen,width)]
        if xy == []:
            raise Exception(f"Width is too narrow at x={cen}")
        x,y = points_to_xy(xy)
        coef = polynomial_regression(x,y,degree=degree)
        
        out.append(poly(cen,coef))

    return C,out





if __name__ == '__main__':
    x_data = x_base = np.linspace(-1,6,300)
    y_base = np.cos(x_data)
    y_data = y_base+np.random.normal(0,.3,300)
    
    
    x1,y1 = simple_local_regression(x_data,y_data,width=.5,n=100,degree=1)
    
    make_blank_canvas(xlim=(-2,7),ylim=(-2,2),size=(12.5,6))
    draw_dots_xy(x_data,y_data,s=5)
    draw_curve_xy(x_base,y_base)
    draw_curve_xy(x1,y1,color='red')
    plt.title("Simple Local Linear Regression Curve",size=20)