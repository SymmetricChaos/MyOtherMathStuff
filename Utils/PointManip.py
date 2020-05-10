import Utils.Drawing as draw
from Utils.PointTypes import points_to_xy
import numpy as np

# All functions here take points as an ordered pair and return a value withing
# altering the input(s)

def midpoint(A,B):
    """
    Return midpoint of A and B
    """
    return [ (A[0]+B[0])/2, (A[1]+B[1])/2 ]


def slope_between(A,B):
    """
    Slope from point A to point B
    """
    return (A[1]-B[1])/(A[0]-B[0])


def push_from_center(P,C,d):
    """
    Return a new point that is P shifted d units from C
    """
    a = np.arctan2(P[0]-C[0],P[1]-C[1])
    dx = np.sin(a)*d
    dy = np.cos(a)*d
    
    
    return [P[0]+dx,P[1]+dy]
    

    
    
if __name__ == '__main__':
    A = [2,1]
    B = [0,0]
    C = [1,1.2]
    D = push_from_center(A,C,.6)
    M = midpoint(A,B)
    Mx, My = points_to_xy([M])
    X,Y = points_to_xy([A,B,C,D])
    
    
    draw.make_blank_canvas([-3,3],[-3,3])
    draw.vertical_line(color='black',zorder=-10)
    draw.horizontal_line(color='black',zorder=-10)
    draw.draw_circles_xy(X,Y,R=[.05]*4)
    draw.draw_circle_xy(Mx[0],My[0],R=.03,color='red')
    draw.connect_p(C,D)