import random
from itertools import product
from Utils import make_canvas
import matplotlib.pyplot as plt

X = 50
Y = 50
grid = [i for i in product(range(-X//2-1,X//2),range(-Y//2-1,Y//2))]
myStack = []

def neighbors(x):
    ne = [(x[0]-1,x[1]),(x[0]+1,x[1]),(x[0],x[1]-1),(x[0],x[1]+1)]
    return [i for i in ne if i in grid]


make_canvas([-28,28],size=[15,15])
plt.scatter(.5,.5,color='red')
pos_cur = (0,0)
grid.remove(pos_cur)
while len(grid) > 0:
    ne = neighbors(pos_cur)
    if len(ne) > 0:
        myStack.append(pos_cur)
        pos_new = random.sample(ne,1)[0]
        grid.remove(pos_new)
        plt.plot( [pos_cur[0], pos_new[0]], [pos_cur[1], pos_new[1]] ,color='black')
        pos_cur = pos_new
    else:
        pos_cur = myStack.pop()