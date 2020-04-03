def xy_to_complex(x,y):
    return [a+bj for a,b in zip(x,y)]

def xy_to_point(x,y):
    return [a,b for a,b in zip(x,y)]

def point_to_complex(P):
    return [a+bj for a,b in P]

def point_to_xy(P):
    return [p[0] for p in P], [p[1] for p in P]

def complex_to_xy(C):
    return [z.real for z in C], [z.imag for z in C]

def complex_to_point(C):
    return [z.real,z.imag for z in C]