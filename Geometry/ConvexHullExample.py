from Polygons import Polygon, polygon_hull
from Utils.Drawing import make_canvas

F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])
F.scale(.6)
D = Polygon([[0,0],[.3,.5],[.5,1.5],[.2,1],[-.2,1],[-.7,1.2]])
A = Polygon([[0,-1.9],[.52,-2.8],[-.52,-2.8]])

ax,fig = make_canvas([-3,3])
for x,P in zip([-2,0,1.5],[F,D,A]):
    P.shift_center(x)
    chullP = polygon_hull(P)
    chullP.draw(linewidth=3,zorder=3)
    P.draw_points(zorder=2)
    P.draw(edgecolor='gray')