# https://lsandig.org/blog/2014/08/apollon-python/en/

import numpy as np
from Geometry.Shapes import Circle
from Utils.Drawing import make_canvas

def complex_center(C):
    assert type(C) == Circle
    return complex(C.pos[0],C.pos[1])

def outer_circ(A,B,C):
    Acen = complex_center(A)
    Bcen = complex_center(B)
    Ccen = complex_center(C)
    c4 = -2*np.sqrt(A.cur*B.cur + B.cur*C.cur + A.cur*C.cur) + A.cur + B.cur + C.cur
    m4 = (-2 * np.sqrt(A.cur*Acen*B.cur*Bcen + 
                       A.cur*Acen*C.cur*Ccen + 
                       B.cur*Bcen*C.cur*Ccen) + A.cur*Acen + B.cur*Bcen + C.cur*Ccen)/c4
    
    return Circle(1/c4,[m4.real,m4.imag])


def tan_circ_from_radii(a,b,c):
    C2 = Circle(a,[0,0])
    C3 = Circle(b,[0,a+b])
    p4x = (a*a + a*b + a*c - b*c)/(a+b)
    p4y = np.sqrt((a+c)*(a+c) - p4x*p4x)
    C4 = Circle(c,[p4x,p4y])
    C1 = outer_circ(C2,C3,C4)
    
    ## Center the cirlces
#    C2.pos[0] -= C1.pos[0]
#    C2.pos[1] -= C1.pos[1]
#    C3.pos[0] -= C1.pos[0]
#    C3.pos[1] -= C1.pos[1]
#    C4.pos[0] -= C1.pos[0]
#    C4.pos[1] -= C1.pos[1]
#    C1.pos = [0,0]
    
    return C1,C2,C3,C4


def second_solution(F,A,B,C):
    Acen = complex_center(A)
    Bcen = complex_center(B)
    Ccen = complex_center(C)
    Fcen = complex_center(F)
    curn = 2*(A.cur+B.cur+C.cur) - F.cur
    posn = (2*(A.cur*Acen+B.cur*Bcen+C.cur*Ccen) - F.cur*Fcen)/curn
    return Circle(1/curn,[posn.real,posn.imag])

    
def apollo_recur(a,b,c,d,lim,itr,lines,circles):
    
#    if lines == True:
#        if a.r > 0 and b.r > 0:
#            connect([a.pos.real,a.pos.imag],[b.pos.real,b.pos.imag])
#        if a.r > 0 and c.r > 0:
#            connect([a.pos.real,a.pos.imag],[c.pos.real,c.pos.imag])
#        if a.r > 0 and d.r > 0:
#            connect([a.pos.real,a.pos.imag],[d.pos.real,d.pos.imag])
    

    if itr == 0:
        e0 = second_solution(a,b,c,d)
        if circles == True:
            e0.draw()
        apollo_recur(e0,b,c,d,lim,itr+1,lines,circles)
    
    e1 = second_solution(b,a,c,d)
    if e1.cur < lim:
        if circles == True:
            e1.draw()
        apollo_recur(e1,a,c,d,lim,itr+1,lines,circles)
    
    e2 = second_solution(c,a,b,d)
    if e2.cur < lim:
        if circles == True:
            e2.draw()
        apollo_recur(e2,a,b,d,lim,itr+1,lines,circles)
        
    e3 = second_solution(d,a,b,c)
    if e3.cur < lim:
        if circles == True:
            e3.draw()
        apollo_recur(e3,a,b,c,lim,itr+1,lines,circles)
        

def ApollonianGasket(A,B,C,lim=10,lines=False,circles=True):
    a,b,c,d = tan_circ_from_radii(A,B,C)

    ax,fig = make_canvas([-a.r-(a.r/20),a.r+(a.r/20)],[-a.r-(a.r/20),a.r+(a.r/20)],[16,16])
    
    if circles == True:
        a.draw(color='red')
        b.draw(color='blue')
        c.draw()
        d.draw()
        
#    if lines == True:
#        connect([b.pos.real,b.pos.imag],[c.pos.real,c.pos.imag])
#        connect([c.pos.real,c.pos.imag],[d.pos.real,d.pos.imag])
#        connect([d.pos.real,d.pos.imag],[b.pos.real,b.pos.imag])
        
#    apollo_recur(a,b,c,d,lim,0,lines,circles)
    

N = 10
ApollonianGasket(1,1,1,N,lines=False,circles=True)
#plt.savefig("ApollonianLines{}.png".format(N),dpi=400)