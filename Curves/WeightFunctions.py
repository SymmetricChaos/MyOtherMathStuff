import numpy as np
import matplotlib.pyplot as plt

# Common weight functions.
# These take a list of values between -1 and 1 and assign a value to each to
# represent its "importance" in some sense. Then normalize the result to sum to
# one.

# Convenience function to take a range of values, center the mean on zero, and
# divide by the largest absolute value.
def center_and_squish(L):
    
    c = np.mean(L)
    out = [l-c for l in L]
    m = max([abs(o) for o in out])
    
    return [o/m for o in out]

def triangular_weights(U):
    
    out = [1-abs(u) for u in U]
    out = [max(val,0) for val in out]
    S = sum(out)
    
    return [val/S for val in out]


# Rebuild to make functions based on triangular_weight above
# Creates a functions from a paramatric family of weight functions based on the
# triangular. They give differing amounts of peakedness.
def parametric_weights(a=1,b=1):
    
    def func(U):
        out = [(1-abs(u)**a)**b if abs(u) <= 1 else 0 for u in U]
        S = sum(out)
        
        return [val/S for val in out]

    return func


#def exponential_weights(u):
    





if __name__ == '__main__':
    x = np.linspace(-1.4,1.4,101)    

    for a,b in zip([1,1,1,2,2,2,3,3,3],[1,2,3,1,2,3,1,2,3]):
        f = parametric_weights(a,b)
        
        plt.plot(x,f(x),color="gray",alpha=.5)
        
    print(triangular_weights(x))