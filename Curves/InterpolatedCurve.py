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
# Need to adapt this from SimpleCAS
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
    return final





if __name__ == '__main__':
    print(lagrange_interpolation([0,1,2],[1,1,0]))