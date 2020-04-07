# Treat lists as polynomial coefficients and multiplies them
def poly_mult(P, Q):
    
    out = [0]*(len(P)+len(Q))
    
    for i in range(len(P)):
        for j in range(len(Q)):
            out[i+j] += P[i]*Q[j]
            out[i+j] = out[i+j]

    
    while out[-1] == 0 and len(out) > 1:
        if len(out) == 1:
            break
        out.pop()

    return out


# Interpolation using lagrange polynomials
def lagrange_interpolation(X,Y):
    
    final = []
    
    for x,y in zip(X,Y):
        out = [y]
        for m in X:
            if m != x:
                d = [1/(x-m)]
                P = [-m,1]
                out = poly_mult(out,poly_mult(P,d))
        final += out
    
    # Probably a more efficient way to do this
    def polynomial_func(x):
        
        c = 0
        for pwr,co in enumerate(final):
            c = c + co*(x**pwr)
        return c
        
    return polynomial_func





if __name__ == '__main__':
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    X = [1,3,4]
    Y = [1,2,1.5]
    P = lagrange_interpolation(X,Y)
    
    x = np.linspace(X[0]-1,X[-1]+1,1001)
    y = [P(i) for i in x]
    
    fig = plt.figure()
    fig.set_size_inches(6,6)
    ax = plt.axes(xlim=[-2,5],ylim=[-3,3])
        
    plt.scatter(X,Y)
    plt.plot(x,y)