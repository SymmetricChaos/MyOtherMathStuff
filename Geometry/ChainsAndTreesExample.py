from ChainsAndTrees import Tree
from Utils.Drawing import make_canvas


make_canvas([-3,3],size=5)
v = [[0,0],[0,.5],[-.5,.7],[.5,1],[0,1.1]]
l = {0 : [1], 1 : [1,2], 2 : [], 3 : [1]}
T = Tree(v,l)
T.draw()
