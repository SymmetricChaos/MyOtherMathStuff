from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from math import sqrt, sin, cos, exp
from matplotlib import pyplot as plt

def ballistic_motion(V0,th,g,m,A,Cd,rho,dt):

    Vt = sqrt((2*m*g)/(rho*A*Cd))
    t = 0
    
    x, y = [0], [0]
    while True:
        t += dt
        d = (1-exp(-g*t/Vt))
        x.append(((V0*Vt*cos(th))/g)*d)
        y.append((Vt/g)*(V0*sin(th)+Vt)*d-(Vt*t))
        if y[-1] < 0:
            y[-1] = 0
            break
    
    return {"V0" : V0,
            "th" : th,
            "g" : g,
            "m" : m,
            "A" : A,
            "Cd" : Cd,
            "rho" : rho,
            "Vt" : Vt}, x, y
    
    
    
def ballistic_table(D):
    L = []
    L.append(f"Initial Speed:     {D['V0']}")
    L.append(f"Angle of Release:  {D['th']}")
    L.append(f"Gravitation:       {-D['g']}m/s^2")
    L.append(f"Projectile Mass:   {D['m']}")
    L.append(f"Cross Section:     {D['A']}")
    L.append(f"Drag Coefficient:  {D['Cd']}")
    L.append(f"Air Density:       {D['rho']}")
    L.append(f"Terminal Velocity: {round(D['Vt'],3)}")
    return L


def list_to_intervals(L,n):
    out = []
    row = []
    for pos,val in enumerate(L,1):
        row.append(val)
        if pos % n == 0:
            out.append(row)
            row = []
    if len(row) > 0:
        out.append(row)
    return out


def ballistic_pdf(V0,th,g,m,A,Cd,rho,dt):
    data, x, y = ballistic_motion(70,.8,10,20,.7,.2,1.2,1/30)
    datalist = ballistic_table(data)
    doc = SimpleDocTemplate("BallisticMotion.pdf", pagesize=letter)

    elements = []

    tab = Table(list_to_intervals(datalist,1),
                style=[("BOX",(0,0),(-1,-1),2,colors.gray),
                       ("FONTNAME",(0,0),(-1,-1),"Courier")])

    elements.append(tab)
    
    doc.build(elements)


if __name__ == '__main__':
    
    ballistic_pdf(70,.8,10,20,.7,.2,1.2,1/30)
    