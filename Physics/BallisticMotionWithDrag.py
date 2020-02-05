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
            "Vt" : Vt,
            "x" : x,
            "y" : y}
    
    
    
def ballistic_table(D):
    L = []
    L.append(f"Initial Speed: {D['V0']}")
    L.append(f"Angle of Release (Radians): {D['th']}")
    L.append(f"Gravitation: -{D['g']}m/s^2")
    L.append(f"Projectile Mass: {D['m']}")
    L.append(f"Cross Sectional Area: {D['A']}")
    L.append(f"Drag Coefficient: {D['Cd']}")
    L.append(f"Air Density: {D['rho']}")
    L.append(f"Terminal Velocity: {round(D['Vt'],3)}")
    return L

if __name__ == '__main__':
    
    data = ballistic_motion(70,.8,10,20,.7,.2,1.2,1/30)
    print(ballistic_table(data))
    plt.plot(data["x"],data["y"])
    

#    doc = SimpleDocTemplate("BallisticMotion.pdf", pagesize=letter)
#    # container for the 'Flowable' objects
#    elements = []
#    data = ballistic_motion(70,.8,10,20,.7,.2,1.2,1/30)
#    datalist = Table(data,style=[("BOX",(0,0),(-1,-1),2,colors.gray)])
#
#    elements.append(t)
#    # write the document to disk
#    doc.build(elements)