from Polygons import Polygon, PolygonSet, regular_polygon
from Utils.Drawing import make_canvas, scatter_points

F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])
F.scale(.4)
Frot = F.copy()
Frot.rotate(.5)
Frot.shift(.5,.5)


S = PolygonSet([F,Frot])
S.shift(-3.5,-.2)

ax,fig = make_canvas([-4,4],[-1.5,1.5],show_axes=False)
for i in range(5):
    S.draw(linewidth=3)
    S.shift(1.5)
    S.rotate_center(.035)
    
    
F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])
F.scale(.4)
B = regular_polygon(5,r=.9,pos=[2,2])
C = regular_polygon(3,r=.2,pos=[0,-2.5])

S = PolygonSet([F,B,C])
S[0].rotate_centroid(-.1)
S[1].rotate(.07)

ax,fig = make_canvas([-4,4])
S.draw(linewidth=3)
scatter_points([S.center],color='red')
scatter_points([S.centroid],color='blue')