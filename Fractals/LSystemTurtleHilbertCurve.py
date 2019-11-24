import turtle
from LSystem import LSystem
def hilbert_curve_rule(S):
    if S == "A":
        return "+BF-AFA-FB+"
    if S == "B":
        return "-AF+BFB+FA-"
    else:
        return S

for i in LSystem("B",hilbert_curve_rule,5):
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
        turtle.forward(10)
    elif i == "-":
        turtle.left(90)
    elif i == "+":
        turtle.right(90)

turtle.done()
