from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Spacer, PageBreak, Paragraph
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.shapes import Drawing
from math import sqrt, sin, cos, exp, acos

def ballistic_motion(V0,th,m,A,Cd=.5,x0=0,y0=0,g=9.86,rho=1.27,dt=1/16):
    
    if x0 < 0 or y0 < 0:
        raise Exception("x0 and y0 must be non-negative")
    
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
        x.append(x0+((V0*Vt*cos(thrad))/g)*d)
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


def ballistic_tables(D,x,y,dtL,digits=2):
    
    #Initial Conditions
    conditions = [[f"Initial Speed:     {round(D['V0'],digits)} m/s"],
                  [f"Angle of Release:  {round(D['th'],digits)}°"],
                  [f"Initial Height:    {round(D['y0'],digits)} m"]
                 ]
    
    conditions_tab = Table(conditions,colWidths=210,
                     style=[("BOX",(0,0),(-1,-1),2,colors.gray),
                            ("FONTNAME",(0,0),(-1,-1),"Courier")])
    
    # Object properties
    props = [[f"Projectile Mass:       {round(D['m'],digits)} kg"],
             [f"Cross Section:         {round(D['A'],digits)} m²"],
             [f"Drag Coefficient:      {round(D['Cd'],digits)}"],
             [f"Terminal Velocity:     {round(D['Vt'],digits)} m/s"]
            ]
    
    props_tab = Table(props,colWidths=210,
                     style=[("BOX",(0,0),(-1,-1),2,colors.gray),
                            ("FONTNAME",(0,0),(-1,-1),"Courier")])
    
    #Environmental conditions
    environs = [[f"Gravitation:       {-round(D['g'],digits)} m/s²"],
                [f"Air Density:       {round(D['rho'],digits)} kg/m³"]
               ]
    
    environs_tab = Table(environs,colWidths=210,
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
    
    outcomes = [[f"Final Distance:    {round(x[-1],digits)} m"],
                [f"Max Height:        {round(max(y),digits)} m"],
                [f"Final Speed:       {round(c/dtL[-1],digits)} m/s"],
                [f"Time of Flight:    {round(D['tof'],digits)} s"],
                [f"Impact Angle:      {round(ang,digits)}°"]
               ]
    
    outcomes_tab = Table(outcomes,colWidths=210,
                     style=[("BOX",(0,0),(-1,-1),2,colors.gray),
                            ("FONTNAME",(0,0),(-1,-1),"Courier")])
    
    return Table([[conditions_tab], [props_tab], [environs_tab], [outcomes_tab]])


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


def line_plot(x,y,title):
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


def line_plot_compare(X,Y):
    drawing = Drawing(400, 300)
    maxW = 0
    maxH = 0
    data = []
    for x,y in zip(X,Y):
        data.append([(a,b) for a,b in zip(x,y)])
        maxW = max(maxW,max(x))
        maxH = max(maxH,max(y))
    
    lp = LinePlot()
    lp.width = 400
    lp.height = 400
    lp.x = 20
    lp.y = -100
    
    lp.lines.strokeWidth = 1.5
    
    lp.xValueAxis.valueMin = 0
    lp.xValueAxis.valueMax = max(maxW,maxH)
    
    lp.yValueAxis.valueMin = 0
    lp.yValueAxis.valueMax = max(maxW,maxH)
    
    lp.data = data
    
    cls = [colors.HexColor("#000000"),  #Black
           colors.HexColor("#E69F00"),  #Orange
           colors.HexColor("#56B4E9"),  #Sky Blue
           colors.HexColor("#009E73"),  #Bluish Green
           colors.HexColor("#F0E442"),  #Yellow
           colors.HexColor("#0072B2"),  #Blue
           colors.HexColor("#D55E00"),  #Vermillion
           colors.HexColor("#CC79A7")   #Reddish Purple
          ]
    
    for i in range(len(data)):
        lp.lines[i].strokeColor = cls[i%8]
    
    drawing.add(lp)
    
    return drawing


def ballistic_pdf(V0,th,m,A,Cd=.5,x0=0,y0=0,g=9.86,rho=1.27,dt=1/16,title="BallisticMotion"):
    if abs(th) > 90:
        raise Exception("Angle must be between -90 and 90 degrees")
    
    for var,name in zip([V0,y0,m,A,Cd,g,rho,dt],["V0","y0","m","A","Cd","g","rho","dt"]):
        if var < 0:
            raise Exception(f"{name} must be non-negative")
    
    
    data, x, y, dtL = ballistic_motion(V0,th,m,A,Cd,x0,y0,g,rho,dt)
    datatabs = ballistic_tables(data,x,y,dtL)
    doc = SimpleDocTemplate(f"{title}.pdf", pagesize=letter)
    
    elements = []
    
    draw = line_plot(x,y,title)
    elements.append(draw)
    
    elements.append(datatabs)
    
    doc.build(elements)
    
    return data, x, y, dtL


def ballistic_pdf_compare(V0,th,m,A,Cd=[.5],x0=[0],y0=[0],g=[9.86],rho=[1.27],dt=[1/16],title="BallisticMotionCompare"):
        
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
    tabs = []
    all_data = []
    all_dtL = []
    for info in zip(V0,th,m,A,Cd,x0,y0,g,rho,dt):
        data, x, y, dtL = ballistic_motion(*info)
        tabs.append(ballistic_tables(data,x,y,dtL))
        X.append(x)
        Y.append(y)
        all_data.append(data)
        all_dtL.append(dtL)
    
    drawing = line_plot_compare(X,Y)
    
    elements = [drawing]
    elements.append(PageBreak())
    
    ctr = 0
    temp = []
    
    for T in tabs:
        
        if ctr % 2 == 0 and ctr > 0:
            elements.append(Table([temp]))
            elements.append(Spacer(1, 15))
            temp = []
        
        if ctr % 4 == 0 and ctr > 0:
            elements.append(PageBreak())
            
        temp.append(T)
        
        ctr += 1
    
    if len(temp) > 0:
        elements.append(Table([temp]))
        elements.append(PageBreak())
    
    doc = SimpleDocTemplate(f"{title}.pdf", pagesize=letter)
    
    doc.build(elements)
    
    return all_data, X, Y, all_dtL





if __name__ == '__main__':
    
    ballistic_pdf(V0=500,  th=15,
                  y0=0,    m=8.4,
                  A=0.005, Cd=.5,
                  g=9.8,   rho=1.27,
                  dt=1/16)
    
    ballistic_pdf_compare(V0 = [500,500,500,500], 
                          th = [5,10,15,20],
                          m  = [8.4],   
                          A  = [0.005])