from Polygons import Polygon, PolygonSet
from Utils.Drawing import make_canvas

F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],
             [1.5,2],[.5,2],[.5,2.5],[2,2.5],
             [2,3],[0,3]])
F.scale(.4)
F.shift_center()


S1 = PolygonSet([F,F])
S1[1].rotate(.5)
S1[0].shift(0,.5)
S1[1].shift(y=-.5)
S1.shift(-3.5,-.2)

S2 = PolygonSet([F,F])
S2[1].mirror("x")
S2[1].shift(1)
S2.shift(-3.5)


S3 = PolygonSet([F,F])
S3[1].mirror("y")
S3[0].shift(y=-.6)
S3[1].shift(y=.6)
S3.shift(-3.5)

F.shift_centroid()
F.shift(-3.6)

ax,fig = make_canvas([-4,4],[-1.5,1.5])
for i in range(8):
    F.draw(linewidth=3)
    F.shift(1)

ax,fig = make_canvas([-4,4],[-1.5,1.5])
for i in range(8):
    S1.draw(linewidth=3)
    S1.shift(1)

ax,fig = make_canvas([-4,4],[-1.5,1.5])
for i in range(4):
    S2.draw(linewidth=3)
    S2.shift(2)

ax,fig = make_canvas([-4,4],[-1.5,1.5])
for i in range(8):
    S3.draw(linewidth=3)
    S3.shift(1)
