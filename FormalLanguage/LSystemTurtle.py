import Utils.Drawing as Drawing
import Utils.MatPlotTurtle as mplt
import LSystem as LS


def dragon_curve(n):
    r1 = LS.rewrite_rule("X","X+YF+")
    r2 = LS.rewrite_rule("Y","-FX-Y")
    dragon = LS.LSystem([r1,r2],"XYF+-")
    S = "FX"
    for i in range(n):
        S = dragon(S)
    
    Drawing.make_blank_canvas()
    ax = Drawing.make_blank_plot(xlim=[-50,50])
    turt = mplt.mplTurtle()
    maxx = 0
    minx = 0
    maxy = 0
    miny = 0
    for char in S:
        if char == "F":
            turt.forward(1)
        if char == "-":
            turt.left(90)
        if char == "+":
            turt.right(90)
        maxx = max(turt.pos[0],maxx)
        minx = min(turt.pos[0],minx)
        maxy = max(turt.pos[1],maxy)
        miny = min(turt.pos[1],miny)
    
    true_max = max(maxx,maxy)
    true_min = min(minx,miny)
    ax.set_xlim((true_min-1,true_max+1))
    ax.set_ylim((true_min-1,true_max+1))
    
def sierpinski_curve(n,ax=None):
    r1 = LS.rewrite_rule("A","B-A-B")
    r2 = LS.rewrite_rule("B","A+B+A")
    sierpinski = LS.LSystem([r1,r2],"AB+-")
    S = "A"
    for i in range(n):
        S = sierpinski(S)
    
    turt = mplt.mplTurtle(angle=30,ax=ax)
    P = []
    turt.draw = False
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

#dragon_curve(8)
Drawing.make_blank_canvas()
for i in range(1,5):
    ax = Drawing.make_blank_plot(2,2,i)
    sierpinski_curve(i,ax)