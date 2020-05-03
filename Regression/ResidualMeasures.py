
# Differences between prediction funcion f(x) and data y
# Optionally raised to a power, usually squared
def residuals(X,Y,f,p=1):
    devs = []
    for x,y in X,Y:
        devs.append( abs(y-f(x))**p )
    
    return devs


# Differences between some central point c and actual values
# Optionally raised to a power, usually squared
def errors(D,c,p=1):
    devs = []
    for d in D:
        devs.append( abs(d-c)**p )
    
    return devs