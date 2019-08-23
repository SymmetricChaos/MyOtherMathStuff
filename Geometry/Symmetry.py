from Polygons import Polygon, PolygonSet
from Utils.Drawing import make_canvas

F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])
F.scale(.4)
F.shift_center()


S1 = PolygonSet([F,F])
S1[1].rotate(.5)
S1[0].shift(.2,.5)
S1[1].shift(y=-.5)
S1.shift(-4,-.2)

S2 = PolygonSet([F,F])
S2[1].mirror("x")
S2[1].shift(1)
S2.shift(-3.8)

F.shift_centroid()
F.shift(-4)

ax,fig = make_canvas([-4,4],[-1.5,1.5],show_axes=False)
for i in range(9):
    F.draw(linewidth=3)
    F.shift(1)

ax,fig = make_canvas([-4,4],[-1.5,1.5],show_axes=False)
for i in range(9):
    S1.draw(linewidth=3)
    S1.shift(1)

ax,fig = make_canvas([-4,4],[-1.5,1.5],show_axes=False)
for i in range(4):
    S2.draw(linewidth=3)
    S2.shift(2)
