import numpy as np
import matplotlib.pyplot as plt

# Common weight functions.
# These take a list of values assign a value to each to represent its
# "importance" in some sense. Not normalized

# Convenience function to take a range of values, center the mean on zero, and
# divide by the largest absolute value.
def center_and_squish(L,c=None,m=None):
    
    if c == None:
        c = np.mean(L)
    out = [l-c for l in L]
    
    if m == None:
        m = max([abs(o) for o in out])
    
    return [o/m for o in out]


# Goes to zero very quickly but covers the whole real line
def exponential_weights(U,e=np.e):
    
    out = [e**-abs(u) for u in U]
    out = [max(val,0) for val in out]
    
    return out


# Rebuild to make functions based on triangular_weight above
# Creates a functions from a paramatric family of weight functions based on the
# triangular. They give differing amounts of peakedness. Limited to the interval
# [-1,1]
def parametric_weights(a=1,b=1):
    
    def func(U):
        out = [(1-abs(u)**a)**b if abs(u) <= 1 else 0 for u in U]

        
        return out

    return func


# Common special case of parametric weights
def triangular_weights(U):
    
    out = [1-abs(u) for u in U]
    out = [max(val,0) for val in out]
    
    return out







if __name__ == '__main__':
    
    from Drawing import make_blank_canvas, make_blank_subplot, horizontal_line, draw_curve_xy
    
    make_blank_canvas()
    
    x = np.linspace(-1.2,1.2,51)    
    y1 = triangular_weights(x)
    epanechnikov = parametric_weights(2,1)
    y2 = epanechnikov(x)
    tricube = parametric_weights(3,3)
    y3 = tricube(x)
    y4 = exponential_weights(x)
    
    Y = [y1,y2,y3,y4]
    
    t1 = "Triangular   $1-|x|$"
    t2 = "Epanechnikov   $1-|x|^2$"
    t3 = "Tricube   $(1-|x|^3)^3$"
    t4 = "Exponential   $e^{-|x|}$"
    
    T = [t1,t2,t3,t4]
    
    ctr = 1
    for y,t in zip(Y,T):
        ax = make_blank_subplot(3,3,ctr)
        
        draw_curve_xy(x,y,color="lightgray")
        horizontal_line(0,[-1.2,1.2],color="black",linewidth=.5)
        plt.title(t)
        
        ctr += 1
    