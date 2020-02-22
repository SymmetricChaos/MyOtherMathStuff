#from Drawing import make_canvas, connect
from math import atan, atan2

# Ray casting is a simple way to represent fields of view with obstructions

# To do this we find which verticies of the walls are visible from a given
# position. Then the space can be divided into triangles and everything within
# those triangles is visible.

# First we sort all the vertices by relative angle. This is called the sweepline.

def sort_verts(pos,verts):
    angs = []
    for v in verts:
        angs.append(atan2(v[1],v[0]))

    return [x for _,x in sorted(zip(angs,verts))]
    
print(sort_verts( (0,0),[ (-1,1), (1,1), (-1,-1), (1,-1)]))


