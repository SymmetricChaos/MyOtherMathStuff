import Utils.Drawing as Drawing
import Utils.MatPlotTurtle as mplt
import LSystem as LS

r1 = LS.rewrite_rule("X","X+YF+")
r2 = LS.rewrite_rule("Y","-FX-Y")
dragon = LS.LSystem([r1,r2],"XYF+-")
S = "FX"
for i in range(6):
    S = dragon(S)

Drawing.make_blank_canvas()
Drawing.make_plot(xlim=[-50,50])
turt = mplt.mplTurtle()
for char in S:
    if char == "F":
        turt.forward(2)
    if char == "-":
        turt.left(90)
    if char == "+":
        turt.right(90)
