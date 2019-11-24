from LSystem import LSystem
from Utils import make_canvas, plot_points


def hilbert_curve_rule(S):
    if S == "A":
        return "+BF-AFA-FB+"
    if S == "B":
        return "-AF+BFB+FA-"
    else:
        return S


def draw_hilbert(n):

    for i in LSystem("B",hilbert_curve_rule,n+2):
        rules = i
    
    coords = [(0,0)]
    
    # Strip out anything unnceesaary for drawing
    rules = rules.replace("A","")
    rules = rules.replace("B","")
    rules = rules.replace("-+","")
    rules = rules.replace("+-","")
    while rules[0] == "+" or rules[0] == "-":
        rules = rules[1:]
    
    ang = (n+1)%2
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
    
    xmax = max([i[0] for i in coords])
    make_canvas([-1,xmax+1],size=6)
    plot_points(coords)

if __name__ == '__main__':
    for i in range(5):
        draw_hilbert(i)