from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Image
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.shapes import Drawing
from math import sqrt, sin, cos, exp
from matplotlib import pyplot as plt

def ballistic_motion(V0,th,y0,g,m,A,Cd,rho,dt):

    if y0 < 0:
        raise Exception("y0 must be non-negative")
    
    Vt = sqrt((2*m*g)/(rho*A*Cd))
    t = 0
    
    x, y = [0], [y0]
    while True:
        t += dt
        d = (1-exp(-g*t/Vt))
        x.append(((V0*Vt*cos(th))/g)*d)
        y.append(y0+(Vt/g)*(V0*sin(th)+Vt)*d-(Vt*t))
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
    L.append(f"Initial Speed:     {D['V0']}m/s")
    L.append(f"Angle of Release:  {round(D['th'],3)}")
    L.append(f"Gravitation:       {-round(D['g'])}m/s^2")
    L.append(f"Projectile Mass:   {D['m']}kg")
    L.append(f"Cross Section:     {D['A']}m^2")
    L.append(f"Drag Coefficient:  {D['Cd']}")
    L.append(f"Air Density:       {D['rho']}")
    L.append(f"Terminal Velocity: {round(D['Vt'],3)}m/s")
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


def line_plot(x,y):
    drawing = Drawing(400, 200)
    
    data = [(a,b) for a,b in zip(x,y)]
    
    lp = LinePlot()
    lp.y = 40
    lp.x = 30 
    lp.width = 400
    lp.height = 200
 
 
    lp.lineLabels.fontSize = 6
    lp.lineLabels.boxStrokeWidth = 0.5
    lp.lineLabels.visible = 1
    lp.lineLabels.boxAnchor = 'c'
    lp.lineLabels.angle = 0
    lp.lineLabelNudge = 10
    lp.joinedLines = 1
    lp.lines.strokeWidth = 1.5
 
    lp.data = [data]
    drawing.add(lp)
     
     
    return drawing


def ballistic_pdf(V0,th,y0,g,m,A,Cd,rho,dt):
    data, x, y = ballistic_motion(V0,th,y0,g,m,A,Cd,rho,dt)
    datalist = ballistic_table(data)
    doc = SimpleDocTemplate("BallisticMotion.pdf", pagesize=letter)


    elements = []
    
    draw = line_plot(x,y)
    elements.append(draw)

    tab = Table(list_to_intervals(datalist,1),
                style=[("BOX",(0,0),(-1,-1),2,colors.gray),
                       ("FONTNAME",(0,0),(-1,-1),"Courier")])
    elements.append(tab)

    
    doc.build(elements)


if __name__ == '__main__':
    
    ballistic_pdf(7,.8,10,10,20,.7,.2,1.2,1/30)
    