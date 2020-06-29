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
            P.append(turt.pos)
        if char == "-":
            turt.left(90)
        if char == "+":
            turt.right(90)
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
            P.append(turt.pos)
        elif char == "-":
            turt.left(60)
        elif char == "+":
            turt.right(60)

    Drawing.draw_dots_p(P,ax=ax,color='white',zorder=-1)
    ax.set_aspect('equal','datalim')


def barnsley_ferm(n,ax=None,**kwargs):
    r1 = LS.rewrite_rule("X","F+[[X]-X]-F[-FX]+X")
    r2 = LS.rewrite_rule("F","FF")
    barnsley = LS.LSystem([r1,r2],"XF+-[]")
    S = "X"
    for i in range(n):
        S = barnsley(S)
    
    turt = mplt.mplTurtle(angle=25,ax=ax,**kwargs)
    P = []
    stack = []
    for char in S:
        if char == "F":
            turt.forward(1)
            P.append(turt.pos)
        elif char == "-":
            turt.left(25)
        elif char == "+":
            turt.right(25)
        elif char == "[":
            stack.append((turt.pos,turt.angle))
        elif char == "]":
            turt.pos, turt.angle = stack.pop()

    Drawing.draw_dots_p(P,ax=ax,color='white',zorder=-1)
    ax.set_aspect('equal','datalim')


def binary_tree(n,ax,color='brown'):
    r1 = LS.rewrite_rule("0","1[0]0")
    r2 = LS.rewrite_rule("1","11")
    tree = LS.LSystem([r1,r2],"01[]")
    S = "0"
    for i in range(n):
        S = tree(S)
    
    turt = mplt.mplTurtle(ax=ax,color=color)
    P = []
    stack = []
    dist = 0
    for char in S:
        if dist > 248:
            turt.color = 'green'
        else:
            turt.color = 'brown'
        P.append(turt.pos)
        if char in "1":
            dist += 1
            turt.forward(1)
        if char in "0":
            turt.forward(1)       
        elif char == "[":
            stack.append((turt.pos,turt.angle,dist))
            turt.left(45)
        elif char == "]":
            turt.pos, turt.angle, dist = stack.pop()
            turt.right(45)

    Drawing.draw_dots_p(P,ax=ax,color='white',zorder=-1)
    ax.set_aspect('equal','datalim')
    

def custom_tree(n,ax,color='salmon'):
    r1 = LS.rewrite_rule("0","1[0[0]]0")
    r2 = LS.random_rewrite_rule("1",["11","1"],[1,1])
    tree = LS.LSystem([r1,r2],"01[]")
    S = "0"
    for i in range(n):
        S = tree(S)
    
    turt = mplt.mplTurtle(ax=ax,color=color)
    P = []
    stack = []
    dist = 0
    for char in S:
        P.append(turt.pos)
        if char in "1":
            dist += 1
            turt.forward(1)
        if char in "0":
            turt.forward(1)       
        elif char == "[":
            stack.append((turt.pos,turt.angle,dist))
            turt.left(20)
        elif char == "]":
            turt.pos, turt.angle, dist = stack.pop()
            turt.right(20)

    Drawing.draw_dots_p(P,ax=ax,color='white',zorder=-1)
    ax.set_aspect('equal','datalim')
    
    
#Drawing.make_blank_canvas([15,15])
#Drawing.canvas_title("Dragon Curves",size=25)
#for i in range(1,10):
#    ax = Drawing.make_blank_plot(3,3,i)
#    dragon_curve(i,ax,color='red')
    
#Drawing.make_blank_canvas([16,10])
#Drawing.canvas_title("Sierpinski Curves",size=25)
#for i in range(1,7):
#    ax = Drawing.make_blank_plot(2,3,i)
#    sierpinski_curve(i,ax)
    
#Drawing.make_blank_canvas([12,12])
#Drawing.canvas_title("\nBarnsley Fern",size=25)
#ax = Drawing.make_blank_plot()
#barnsley_ferm(7,ax,color='green')

Drawing.make_blank_canvas([12,12])
Drawing.canvas_title("Tree",size=25)
ax = Drawing.make_blank_plot()
custom_tree(6,ax)
