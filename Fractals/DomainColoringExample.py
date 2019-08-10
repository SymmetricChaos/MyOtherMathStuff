from DomainColoring import domain_coloring_contour

def complex_func(z):
    return (z*z*z)-5/z

r = 4
X = (-r,r)
Y = (-r,r)


domain_coloring_contour(complex_func,X,Y,1000)