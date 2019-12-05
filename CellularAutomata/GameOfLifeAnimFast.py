from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Rather than track every point we track only the live points

def filter_by_rule(D,cells):
    newDict = defaultdict(int)
    for (key, val) in D.items():
        if key in cells:
            if val == 2 or val == 3:
                newDict[key] = 1
        else:
            if val == 3:
                newDict[key] = 1
    return newDict


def add_neighbors(cell,grid):
    neighbors = [(-1,-1),(0,-1),(1,-1),
                 (-1,0) ,       (1,0),
                 (-1,1) ,(0,1), (1,1)]
    
    for x,y in neighbors:
        grid[cell[0]+x,cell[0]+y] += 1
        
def gen(grid):
    live_cells = set(k for k,v in grid.items() if v == 1)
    for c in live_cells:
        add_neighbors(c,grid)

    return filter_by_rule(grid,live_cells)

def coord_gen(grid):

    x = []
    y = []
    for k,v in grid.items():
        if v == 1:
            x.append(k[1])
            y.append(k[0])
    print(grid)
    print(x,y)
    return x,y          


def draw_gen(grid,s):
    
    for i in range(-s//2-1,s//2):
        for j in range(-s//2-1,s//2):
            if grid[(j,i)] == 1:
                print(" # ",end="")
            else:
                print(" . ",end="")
        print()
    print("\n\n\n")

N = 10
grid = defaultdict(int)

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

def anim_plot(num,grid,*args):
    print(num,grid,args)
    x,y = coord_gen(grid)
    dots.set_data(x,y)
    grid = gen(grid)
    return dots

life_anim = animation.FuncAnimation(fig, anim_plot, 10, fargs=(grid),
                                   interval=100, blit=False)
#life_anim.save('game_of_life_fast.mp4')
