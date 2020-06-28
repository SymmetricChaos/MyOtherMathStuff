import Utils.Drawing as Drawing
import Utils.MatPlotTurtle as mplt
import LSystem as LS


def dragon_curve(n,ax,**kwargs):
    r1 = LS.rewrite_rule("X","X+YF+")
    r2 = LS.rewrite_rule("Y","-FX-Y")
    dragon = LS.LSystem([r1,r2],"XYF+-")
    S = "FX"
    for i in range(n):
        S = dragon(S)
    
    turt = mplt.mplTurtle(ax=ax,**kwargs)
    P = []
    for char in S:
        if char == "F":
            turt.forward(1)
        if char == "-":
            turt.left(90)
        if char == "+":
            turt.right(90)
        P.append(turt.pos)
    Drawing.draw_dots_p(P,ax=ax,color='white',zorder=-1)
    ax.set_aspect('equal','datalim')
    
    
def sierpinski_curve(n,ax=None,**kwargs):
    r1 = LS.rewrite_rule("A","B-A-B")
    r2 = LS.rewrite_rule("B","A+B+A")
    sierpinski = LS.LSystem([r1,r2],"AB+-")
    S = "A"
    for i in range(n):
        S = sierpinski(S)
    
    tilt = lambda n: 90 if n%2 == 0 else 30
    
    turt = mplt.mplTurtle(angle=tilt(n),ax=ax,**kwargs)
    P = []
    for char in S:
        if char in ("A","B"):
            turt.forward(1)
        if char == "-":
            turt.left(60)
        if char == "+":
            turt.right(60)
        P.append(turt.pos)
    Drawing.draw_dots_p(P,ax=ax,color='white',zorder=-1)
    ax.set_aspect('equal','datalim')


#Drawing.make_blank_canvas([15,15])
#Drawing.canvas_title("Dragon Curves",size=25)
#for i in range(1,10):
#    ax = Drawing.make_blank_plot(3,3,i)
#    dragon_curve(i,ax,color='red')
    
Drawing.make_blank_canvas([16,10])
Drawing.canvas_title("Sierpinski Curves",size=25)
for i in range(1,7):
    ax = Drawing.make_blank_plot(2,3,i)
    sierpinski_curve(i,ax)