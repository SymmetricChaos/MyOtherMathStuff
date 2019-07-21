import turtle
import random
from itertools import product

X = 150
Y = 150
grid = [i for i in product(range(-X//2-1,X//2),range(-Y//2-1,Y//2))]
myStack = []

turt = turtle.Turtle()
turt.shape("circle")
turt.shapesize(.2,.2)
turt.speed(100)
turtle.screensize(1500,1500)

def neighbors(x):
    ne = [(x[0]-1,x[1]),(x[0]+1,x[1]),(x[0],x[1]-1),(x[0],x[1]+1)]
    return [i for i in ne if i in grid]

pos = (0,0)
grid.remove(pos)
while len(grid) > 0:
    ne = neighbors(pos)
    if len(ne) > 0:
        myStack.append(pos)
        pos =  random.sample(ne,1)[0]
        grid.remove(pos)
        turt.goto(pos[0]*10,pos[1]*10)
    else:
        pos = myStack.pop()
        turt.setpos(pos[0]*10,pos[1]*10)
        
turtle.done()