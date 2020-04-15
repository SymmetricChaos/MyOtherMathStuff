import numpy as np

# Treat lists as polynomial coefficients and multiplies them
def poly_mult(P,Q):
    
    out = [0]*(len(P)+len(Q))
    
    for i in range(len(P)):
        for j in range(len(Q)):
            out[i+j] += P[i]*Q[j]
            out[i+j] = out[i+j]

    poly_normalize(out)

    return out


def poly_normalize(P):
    """Remove trailing zeroes"""
    while P[-1] == 0 and len(P) > 1:
        if len(P) == 1:
            break
        P.pop()


def poly_pad(P,n):
    """Add trailing zeroes"""
    out = P.copy()
    while len(out) < n:
        out.append(0)
    return out
	

def poly_add(P, Q):
    """Take list of polynomial coefficients and add them"""
        
    pad = max(len(P),len(Q))
    
    P = poly_pad(P,pad)
    Q = poly_pad(Q,pad)
    
    out = []
    
    for x,y in zip(P,Q):
        out.append( x+y )

    poly_normalize(out)

    return out


# Interpolation using lagrange polynomials
def lagrange_interpolation(X,Y):
    
    final = [0]
    
    for x,y in zip(X,Y):
        out = [y]
        for m in X:
            if m != x:
                P = [-m/(x-m),1/(x-m)]
                out = poly_mult(out,P)
        final = poly_add(out,final)

    
    # Probably a more efficient way to do this
    def polynomial_func(a):
        c = 0
        for pwr,co in enumerate(final):
            c = c + co*(a**pwr)
        return c
        
    return polynomial_func


# FIND OUT IF NEWTON POLYNOMIALS ARE DIFFERENT
#def newton_interpolation(X,Y):


# Simple moving average of equally spaced data
def simple_moving_average(Y,width=1):
    
    # Number of values considered at each step
    N = 2*width+1
    
    # Padded version of Y
    y = Y[:]
    y = [y[0]]*width + y + [y[-1]]*width

    m_av = []
    for i in range(len(Y)):
        m_av.append(sum(y[i:N+i])/N)
    
    return m_av

def simple_moving_median(Y,width=1):
    
    # Number of values considered at each step
    N = 2*width+1
    
    # Padded version of Y
    y = Y[:]
    y = [y[0]]*width + y + [y[-1]]*width

    m_av = []
    for i in range(len(Y)):
        m_av.append(np.median(y[i:N+i]))
    
    return m_av






if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    
    X = [1,2,3]
    Y = [1,4,6]
    P = lagrange_interpolation(X,Y)
    
    x = np.linspace(X[0]-1,X[-1]+1,1001)
    y = [P(i) for i in x]
        
    fig = plt.figure()
    fig.set_size_inches(12,12)
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
        
    plt.scatter(X,Y)
    plt.plot(x,y)
    
    
    Y = [1,2,3,6,9,12,15,10,14,13,12,10,5,2,1]
    av1 = simple_moving_average(Y,2)
    av2 = simple_moving_median(Y,2)
    
    fig = plt.figure()
    fig.set_size_inches(12,12)
    ax = plt.axes()
    ax.set_aspect("equal","datalim")
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
        
    plt.scatter([i for i in range(len(Y))],Y)
    plt.plot([i for i in range(len(Y))],av1)
    plt.plot([i for i in range(len(Y))],av2)