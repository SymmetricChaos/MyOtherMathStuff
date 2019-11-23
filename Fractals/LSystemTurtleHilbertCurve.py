import turtle
from LSystem import LSystem
def hilbert_curve_rule(S):
    if S == "A":
        return "+BF-AFA-FB+"
    if S == "B":
        return "-AF+BFB+FA-"
    else:
        return S

for i in LSystem("B",hilbert_curve_rule,3):
    rules = i


coords = [(0,0)]

# Strip out anything unnceesaary for drawing
rules = rules.replace("A","")
rules = rules.replace("B","")
rules = rules.replace("-+","")
rules = rules.replace("+-","")
rules = rules[1:]

print(rules)

pos_stack = []
ang_stack = []
turtle.setheading(90)
turtle.hideturtle()
#turtle.up()
#turtle.setpos(0,-300)
#turtle.down()
for i in rules:
    if i == "F":
        turtle.forward(10)
        print(turtle.pos())
    elif i == "-":
        turtle.left(90)
    elif i == "+":
        turtle.right(90)

turtle.up()
turtle.setpos(0,-300)
turtle.done()
