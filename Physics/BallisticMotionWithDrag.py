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
    
    print(f"Initial Speed: {V0}")
    print(f"Angle of Release (Radians): {th}")
    print(f"Gravitation: -{g}m/s^2")
    print(f"Projectile Mass: {m}")
    print(f"Cross Sectional Area: {A}")
    print(f"Drag Coefficient: {Cd}")
    print(f"Air Density: {rho}")
    print(f"Terminal Velocity: {round(Vt,3)}")
    plt.plot(x,y)

if __name__ == '__main__':

    doc = SimpleDocTemplate("BallisticMotion.pdf", pagesize=letter)
    # container for the 'Flowable' objects
    elements = []
    data = ballistic_motion(70,.8,10,20,.7,.2,1.2,1/30)
    datalist = Table(data,style=[("BOX",(0,0),(-1,-1),2,colors.gray)])

    elements.append(t)
    # write the document to disk
    doc.build(elements)