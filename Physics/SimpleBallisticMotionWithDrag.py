from math import sqrt, sin, cos, exp, acos
import Utils.Drawing as draw


def ballistic_motion(V0,th,m,A,Cd=.5,x0=0,y0=0,g=9.86,rho=1.27,dt=1/32):
    
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
    
    #Initial Conditions
    print(f"Initial Speed:      {round(D['V0'],digits)} m/s\n"
          f"Angle of Release:   {round(D['th'],digits)}°\n"
          f"Initial Height:     {round(D['y0'],digits)} m\n\n"
          f"Projectile Mass:    {round(D['m'],digits)} kg\n"
          f"Cross Section:      {round(D['A'],digits)} m²\n"
          f"Projectile Mass:    {round(D['m'],digits)} kg\n"
          f"Drag Coefficient:   {round(D['Cd'],digits)}\n"
          f"Terminal Velocity:  {round(D['Vt'],digits)} m/s\n\n"
          f"Gravitation:        {-round(D['g'],digits)} m/s²\n"
          f"Air Density:        {round(D['rho'],digits)} kg/m³\n\n"
          f"Final Distance:     {round(x[-1],digits)} m\n"
          f"Max Height:         {round(max(y),digits)} m\n"
          f"Final Speed:        {round(c/dtL[-1],digits)} m/s\n"
          f"Time of Flight:     {round(D['tof'],digits)} s\n"
          f"Impact Angle:       {round(ang,digits)}°"
        )


def simple_ballistic_plot(D,x,y,dtL,title):
    
    fig = draw.make_blank_canvas()
    max_x = max(x)
    max_y = max(y)*1.5
    plt = draw.make_plot(xlim=(0,max_x),ylim=(0,max_y),aspect_ratio='equal')
    draw.title(title,size=25)
    draw.curve_xy(x,y)
    plt.grid()
    return fig,plt





if __name__ == '__main__':
    
    # G1 bullet model has nominal Cd .5
    # G7 bullet model has nominal Cd .25
    
    D,x,y,dtL = ballistic_motion(500,15,8.4,0.005,Cd=.5)
    
    simple_ballistic_plot(D,x,y,dtL,title="British 18-Pounder Field Gun (1914)")
    draw.now()
    print()
    ballistic_tables(D,x,y,dtL)
