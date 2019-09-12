from Tree import Tree, tree_sum
from Utils.Drawing import make_canvas


make_canvas([-3,3],size=5)
v = [[0,0],[0,.5],[-.5,.7],[.5,1],[0,1.1]]
l = [ [1], [1,2], [], [1], [] ]
T = Tree(v,l)
T.draw()

make_canvas([-3,3],size=5)
T1 = Tree(v,l)
T2 = Tree(v,l)
T2.rotate(.2)
U = tree_sum(T2,T1,3)
U.draw()


make_canvas([-3,3],size=5)
v = [[0,0],
     [-1,.5], [1,.5],
     [-1.5,1], [-.5,1], [.5,1], [1.5,1]]
l = [ [1,2], [2,3], [3,4], [], [], [], []]
T = Tree(v,l)
T.draw()

make_canvas([-3,3],size=5)
v = [[0,0],
     [-1,.5], [1,.5]
    ]
l = [ [1,2], [], []]
T = Tree(v,l)
U = tree_sum(T.copy(),T,1)
U.draw()
U.draw_verts()
print(T.links)
print(U.links)