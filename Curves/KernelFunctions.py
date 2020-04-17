import numpy as np
import matplotlib.pyplot as plt

def triangular_kernel(u):
    if abs(u) > 1:
        return 0
    return 1-abs(u)


def tricubic_kernel(u):
    if abs(u) > 1:
        return 0
    return 70/81*(1-abs(u)**3)**3


# Precomputed constants to normalize integral to 1
def parametric_kernel(U,a,b):
    assert a > 0 and a < 4
    assert b > 0 and b < 4
    
    D = {(1,1):1, (1,2):3/2, (2,1):3/4, (2,2):15/16,
         (3,1):2/3, (1,3):2/1, (3,2):7/9, (2,3):35/32,
         (3,3):70/81}
    
    C = D[(a,b)]
    
    def func(u):
        if abs(u) > 1:
            return 0
        return C*(1-abs(u)**a)**b

    return [func(u) for u in U]



if __name__ == '__main__':
    x = np.linspace(-1.2,1.2,101)
#    y1 = [triangular_kernel(i) for i in x]
#    y2 = [tricubic_kernel(i) for i in x]
#    

    
    for a,b in zip([1,1,1,2,2,2,3,3,3],[1,2,3,1,2,3,1,2,3]):
        y = parametric_kernel(x,a,b)
        
        plt.plot(x,y)