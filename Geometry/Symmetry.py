from Polygons import Polygon, PolygonSet
from Utils.Drawing import make_canvas

F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])
F.scale(.4)
Frot = F.copy()
Frot.rotate(.5)
Frot.shift_xy(.5,.5)


S = PolygonSet([F,Frot])
S.shift_xy(-4,-.2)


F.shift_centroid()
F.shift_xy(-4)
ax,fig = make_canvas([-4,4],[-1.5,1.5],show_axes=False)
for i in range(9):
    F.draw(linewidth=3)
    F.shift_xy(1)

ax,fig = make_canvas([-4,4],[-1.5,1.5],show_axes=False)
for i in range(9):
    S.draw(linewidth=3)
    S.shift_xy(1)