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
def exponential_weights(U,e=2):
    
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
    
    from Drawing import make_blank_canvas, make_blank_subplot
    
    make_blank_canvas()
    
    x = np.linspace(-1.2,1.2,51)    
    ctr = 1
    for a,b in zip([1,1,1,2,2,2,3,3,3],[1,2,3,1,2,3,1,2,3]):
        make_blank_subplot(3,3,ctr)
        f = parametric_weights(a,b)
        
        plt.plot(x,[y for y in f(x)],color="gray",alpha=.5)
        if a == 1:
            a_sym = ""
        else:
            a_sym = "^"+str(a)
        if b == 1:
            b_sym = ""
        else:
            b_sym = "^"+str(b)
        plt.title(f"$(1-|u|{a_sym}){b_sym}$")
        ctr += 1

    y = exponential_weights(x,4)
    
    make_blank_canvas()
    plt.plot(x,y)
    