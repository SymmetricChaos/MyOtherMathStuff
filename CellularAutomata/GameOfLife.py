from collections import defaultdict
from itertools import product

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


def draw_gen(grid,s):
    
    for i in range(-s//2-1,s//2):
        for j in range(-s//2-1,s//2):
            if grid[(j,i)] == 1:
                print("#",end="")
            else:
                print(".",end="")
        print()
    print("\n\n\n")


grid = empty_grid(30)

grid[(0,0)] = 1
grid[(0,-1)] = 1
grid[(0,1)] = 1
grid[(1,-1)] = 1
grid[(-1,0)] = 1

draw_gen(grid,30)
for i in range(20):

    gen(grid)
    draw_gen(grid,30)