from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Spacer
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.shapes import Drawing
from math import sqrt, sin, cos, exp, acos

def ballistic_motion(V0,th,y0,x0,m,A,Cd,g,rho,dt):

    
    Vt = sqrt((2*m*g)/(rho*A*Cd))
    t = 0
    
    # Convert agle in degrees to radians
    thrad = th*0.0174
    
    # Keep track of coordinates and the size of the time steps
    # We do need to track the size of the time steps because it may change at
    # the end in order to accurately find the point where the ground is hit
    x, y, dtL = [x0], [y0], []
    tof = 0
    while True:
        t += dt
        d = (1-exp(-g*t/Vt))
        x.append(((V0*Vt*cos(thrad))/g)*d)
        y.append(y0+(Vt/g)*(V0*sin(thrad)+Vt)*d-(Vt*t))
        dtL.append(dt)
        tof += dt
        # Check if the object hit the ground
        if y[-1] < 0:
            # If it went through too far, go back one time step and halve the
            # size of the time step
            if abs(y[-1]) > .01:
                t -= dt
                del y[-1]
                del x[-1]
                dt = dt/2
            # Otherwise we're done
            else:
                break
        
    return {"V0" : V0,
            "th" : th,
            "x0" : x0,
            "y0" : y0,
            "g" : g,
            "m" : m,
            "A" : A,
            "Cd" : Cd,
            "rho" : rho,
            "Vt" : Vt,
            "tof" : tof}, x, y, dtL


def ballistic_tables(D,x,y,dtL):
    
    #Initial Conditions
    A = [[f"Initial Speed:     {round(D['V0'],2)} m/s"],
         [f"Angle of Release:  {round(D['th'],2)}°"],
         [f"Initial Height:    {round(D['y0'],2)} m"]]
    
    conditions = Table(A,
            style=[("BOX",(0,0),(-1,-1),2,colors.gray),
                   ("FONTNAME",(0,0),(-1,-1),"Courier")])

    B = [[f"Projectile Mass:   {round(D['m'],2)} kg"],
         [f"Cross Section:     {round(D['A'],2)} m²"],
         [f"Drag Coefficient:  {round(D['Cd'],2)}"],
         [f"Terminal Velocity: {round(D['Vt'],2)} m/s"]]
    
    # Object properties
    props = Table(B,
            style=[("BOX",(0,0),(-1,-1),2,colors.gray),
                   ("FONTNAME",(0,0),(-1,-1),"Courier")])

    
    #Environmental conditions
    C = [[f"Gravitation:       {-round(D['g'],2)} m/s²"],
         [f"Air Density:       {round(D['rho'],2)} kg/m³"]]
    
    environs = Table(C,
            style=[("BOX",(0,0),(-1,-1),2,colors.gray),
                   ("FONTNAME",(0,0),(-1,-1),"Courier")])
    
    # Triangle side lengths
    a = abs(x[-1]-x[-2])
    b = abs(y[-1]-y[-2])
    a2 = a*a
    b2 = b*b
    c2 = a2 + b2
    c = sqrt(c2)
    
    # Calculate angle and mulitiply to get degrees
    # Subtract from 90 to get angle relative to ground
    ang = 90-(acos( (b2+c2-a2) / (2*b*c) ) * 57.4712)
    
    outcomes = [[f"Final Distance:    {round(x[-1],2)} m"],
                [f"Max Height:        {round(max(y),2)} m"],
                [f"Final Speed:       {round(c/dtL[-1],2)} m/s"],
                [f"Time of Flight:    {round(D['tof'],2)} s"],
                [f"Impact Angle:      {round(ang,2)}°"]
                ]
    
    outcomes = Table(outcomes,
            style=[("BOX",(0,0),(-1,-1),2,colors.gray),
                   ("FONTNAME",(0,0),(-1,-1),"Courier")])
    
    return conditions, props, environs, outcomes


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
    drawing = Drawing(400, 300)
    
    data = [(a,b) for a,b in zip(x,y)]
    
    lp = LinePlot()
    lp.width = 300
    lp.height = 300
    lp.x = 80
    lp.y = 30
 
    lp.lineLabels.fontSize = 6
    lp.lineLabels.boxStrokeWidth = 0.5
    lp.lineLabels.visible = 1
    lp.lineLabels.boxAnchor = 'c'
    lp.lineLabels.angle = 0
    lp.lineLabelNudge = 10
    lp.joinedLines = 1
    lp.lines.strokeWidth = 1.5
    
    lp.xValueAxis.valueMin = 0
    lp.xValueAxis.valueMax = max(max(x),max(y))
 
    lp.yValueAxis.valueMin = 0
    lp.yValueAxis.valueMax = max(max(x),max(y))
    
    lp.data = [data]
    drawing.add(lp)
    
    return drawing

def line_plot_multi(X,Y):
    drawing = Drawing(400, 300)
    
    data = []
    for x,y in zip(X,Y):
        data.append([(a,b) for a,b in zip(x,y)])
    
    lp = LinePlot()
    lp.width = 300
    lp.height = 300
    lp.x = 80
    lp.y = 30
 
    lp.lineLabels.fontSize = 6
    lp.lineLabels.boxStrokeWidth = 0.5
    lp.lineLabels.visible = 1
    lp.lineLabels.boxAnchor = 'c'
    lp.lineLabels.angle = 0
    lp.lineLabelNudge = 10
    lp.joinedLines = 1
    lp.lines.strokeWidth = 1.5
    
    lp.xValueAxis.valueMin = 0
    lp.xValueAxis.valueMax = max(max(x),max(y))
 
    lp.yValueAxis.valueMin = 0
    lp.yValueAxis.valueMax = max(max(x),max(y))
    
    lp.data = data
    drawing.add(lp)
    
    return drawing


def ballistic_pdf(V0,th,y0,m,A,Cd,g=9.8,rho=1.27,dt=1/30,title="BallisticMotion"):
    if abs(th) > 90:
        raise Exception("Angle must be between -90 and 90 degrees")
    
    for var,name in zip([V0,y0,m,A,Cd,g,rho,dt],["V0","y0","m","A","Cd","g","rho","dt"]):
        if var < 0:
            raise Exception(f"{name} must be non-negative")

    
    data, x, y, dtL = ballistic_motion(V0,th,0,y0,m,A,Cd,g,rho,dt)
    datatabs = ballistic_tables(data,x,y,dtL)
    doc = SimpleDocTemplate(f"{title}.pdf", pagesize=letter)

    elements = []
    
    draw = line_plot(x,y)
    elements.append(draw)

    for t in datatabs:
        elements.append(Spacer(1, 20))
        elements.append(t)
    
    doc.build(elements)
    
    return data, x, y, dtL


def ballistic_pdf_multi(V0,th,y0,m,A,Cd,g=[9.8],rho=[1.2],dt=[1/30],title="BallisticMotion"):
    
    longest = max(len(V0),len(th),len(y0),len(m),len(A),len(Cd),len(g),len(rho),len(dt))
    
    if len(V0) == 1:
        V0 = V0*longest
    if len(th) == 1:
        th = th*longest
    if len(y0) == 1:
        y0 = y0*longest
    if len(m) == 1:
        m = m*longest
    if len(A) == 1:
        A = A*longest
    if len(Cd) == 1:
        Cd = Cd*longest
    if len(g) == 1:
        g = g*longest
    if len(rho) == 1:
        rho = rho*longest        
    if len(dt) == 1:
        dt = dt*longest 
        
    ctr = 1
    for info in zip(V0,th,y0,m,A,Cd,g,rho,dt):
        ballistic_pdf(*info,title=f"{title}{ctr}")
        ctr += 1


def ballistic_pdf_compare(V0,th,x0,y0,m,A,Cd,g=[9.8],rho=[1.2],dt=[1/30],title="BallisticMotionCompare"):
        
    longest = max(len(V0),len(th),len(x0),len(y0),len(m),len(A),len(Cd),len(g),len(rho),len(dt))
    
    if len(V0) == 1:
        V0 = V0*longest
    if len(th) == 1:
        th = th*longest
    if len(x0) == 1:
        x0 = x0*longest
    if len(y0) == 1:
        y0 = y0*longest
    if len(m) == 1:
        m = m*longest
    if len(A) == 1:
        A = A*longest
    if len(Cd) == 1:
        Cd = Cd*longest
    if len(g) == 1:
        g = g*longest
    if len(rho) == 1:
        rho = rho*longest        
    if len(dt) == 1:
        dt = dt*longest 
    
    X, Y = [], []
    for info in zip(V0,th,x0,y0,m,A,Cd,g,rho,dt):
        print(info)
        _, x, y, _ = ballistic_motion(*info)
        X.append(x)
        Y.append(y)
    
    drawing = line_plot_multi(X,Y)
    
    doc = SimpleDocTemplate(f"{title}.pdf", pagesize=letter)

    doc.build([drawing])





if __name__ == '__main__':
    
    ballistic_pdf(V0=100, th=25,
                  y0=50,  m=20,
                  A=.7,   Cd=.2,  
                  g=9.8,  rho=1.27,
                  dt=1/30)

    ballistic_pdf_compare(V0=[100,200], 
                          th=[25],
                          x0=[0,50],
                          y0=[50],  
                          m=[20],   
                          A=[.7],
                          Cd=[.2],
                          dt=[1/30])