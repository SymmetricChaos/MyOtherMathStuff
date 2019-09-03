import turtle
from LSystem import LSystem
def tree(S):
    if S == "A":
        return "AA"
    if S == "B":
        return "A[B]B"
    else:
        return S

for i in LSystem("B",tree,7):
    rules = i


pos_stack = []
ang_stack = []
turtle.setheading(90)
turtle.up()
turtle.setpos(0,-300)
turtle.down()
for i in rules:
    if i == "A":
        turtle.forward(5)
    if i == "B":
        turtle.forward(5)
    if i == "[":
        pos_stack.append(turtle.pos())
        ang_stack.append(turtle.heading())
        turtle.left(45)
    if i == "]":
        p = pos_stack.pop()
        h = ang_stack.pop()
        turtle.up()
        turtle.setpos(p)
        turtle.setheading(h)
        turtle.down()
        turtle.right(45)
turtle.up()
turtle.setpos(0,-300)
turtle.done()