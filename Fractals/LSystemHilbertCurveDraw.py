from LSystem import LSystem
from Utils import make_canvas, plot_points


def hilbert_curve_rule(S):
    if S == "A":
        return "+BF-AFA-FB+"
    if S == "B":
        return "-AF+BFB+FA-"
    else:
        return S

for i in LSystem("B",hilbert_curve_rule,5):
    rules = i


coords = [(0,0)]

# Strip out anything unnceesaary for drawing
rules = rules.replace("A","")
rules = rules.replace("B","")
rules = rules.replace("-+","")
rules = rules.replace("+-","")
rules = rules[1:]

#print(rules)

ang = 0
for i in rules:
    if i == "F":
        oldx = coords[-1][0] 
        oldy = coords[-1][1]
        if ang == 0:
            coords.append( (oldx,oldy+1) )
        elif ang == 1:
            coords.append( (oldx+1,oldy) )
        elif ang == 2:
            coords.append( (oldx,oldy-1) )
        elif ang == 3:
            coords.append( (oldx-1,oldy) )
    elif i == "-":
        ang = (ang-1)%4
    elif i == "+":
        ang = (ang+1)%4

make_canvas([-40,40],size=6)
plot_points(coords)
