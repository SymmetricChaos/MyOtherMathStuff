from collections import defaultdict
from itertools import product
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def empty_grid(s):
    grid = defaultdict(int)
    
    pos = [i for i in product(range(-s//2-1,s//2),range(-s//2-1,s//2))]
    for i in pos:
        grid[i] = 0
    return grid


def sum_neighbors(cell,grid):
    neighbors = [(-1,-1),(0,-1),(1,-1),
                 (-1,0) ,       (1,0),
                 (-1,1) ,(0,1), (1,1)]

    return sum([grid[(cell[0]+x, cell[1]+y)] for x,y in neighbors])


def gen(grid):

    counts = []
    for i in list(grid.keys()):
        counts.append((i,sum_neighbors(i,grid)))
    
    for pos,val in counts:
        if val < 2 or val > 3:
            grid[pos] = 0
        elif val == 3:
            grid[pos] = 1


def coord_gen(grid,s):

    x = []
    y = []
    for i in range(-s//2-1,s//2):
        for j in range(-s//2-1,s//2):
            if grid[(j,i)] == 1:
                x.append(j)
                y.append(i)
    return x,y          


N = 600
grid = empty_grid(N)

grid[(0,0)] = 1
grid[(0,-1)] = 1
grid[(0,1)] = 1
grid[(1,-1)] = 1
grid[(-1,0)] = 1


fig, ax = plt.subplots()
fig.set_size_inches(6, 6)
plt.xlim(-N//2-1, N//2)
plt.ylim(-N//2-1, N//2)

dots, = plt.plot([0], [0], 'ko', markersize=.4)

def anim_plot(num,grid,s):
    x,y = coord_gen(grid,s)
    dots.set_data(x,y)
    gen(grid)
    return dots

life_anim = animation.FuncAnimation(fig, anim_plot, 10, fargs=(grid, N),
                                   interval=100, blit=False)
life_anim.save('game_of_life.mp4')