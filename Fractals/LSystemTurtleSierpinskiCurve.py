import turtle
from LSystem import LSystem
def sierpinski_arrowhead_rule(S):
    if S == "A":
        return "BF+AF+B"
    if S == "B":
        return "AF-BF-A"
    else:
        return S

for i in LSystem("B",sierpinski_arrowhead_rule,6):
    rules = i


# Strip out anything unnceesaary for drawing
rules = rules.replace("A","")
rules = rules.replace("B","")
rules = rules.replace("-+","")
rules = rules.replace("+-","")
rules = rules[1:]

print(rules)

turtle.setheading(90)
turtle.hideturtle()
for i in rules:
    if i == "F":
        turtle.forward(5)
    elif i == "-":
        turtle.left(60)
    elif i == "+":
        turtle.right(60)

turtle.done()
