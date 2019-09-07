from ChainsAndTrees import Chain, Tree, chain_sum
from Utils.Drawing import make_canvas

make_canvas([-3,3],size=5)
C = Chain([[0,0],[.8,.4],[1,1.3],[-1,1]])
D = C.copy()
chain_sum(C,D,2)

make_canvas([-3,3],size=5)
v = [[0,0],[0,.5],[-.5,.7],[.3,.8],[.4,1.3]]
l = {0 : [1], 1 : [2,3], 2 : [], 3 : [4]}
T = Tree(v,l)
T.draw()

make_canvas([-3,3],size=5)
T2 = Tree(v)
T2.draw()
print(T2.links)