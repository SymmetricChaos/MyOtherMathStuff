from collections import defaultdict
from itertools import product

def empty_grid():
    grid = defaultdict(int)
    
    s = 10
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
        else:
            grid[pos] = 1


def draw_gen(grid):
    



grid = empty_grid()