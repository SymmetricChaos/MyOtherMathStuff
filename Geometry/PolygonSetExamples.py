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
    S.draw_points(color='red')
    S.shift(1.5)
    S.rotate_center(.035)

    
    
A = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])
B = regular_polygon(5,r=.9,pos=[2,2])
C = regular_polygon(3,r=.6,pos=[0,-2.5])
D = Polygon([[0,0],[.3,.5],[.5,1.5],[.2,1],[-.2,1],[-.7,1.2]])


S1 = PolygonSet([F,B,C,D])
S1[0].scale(.9)
S1[0].rotate_centroid(-.1)
S1[1].rotate(.07)
S1[3].mirror_center("y")
S1[3].shift(-1,-.5)


ax,fig = make_canvas([-4,4])
S1.draw(linewidth=3)
S1[2].draw_points(zorder=3,color='orange',s=200)
for i in S1:
    scatter_points([i.centroid],color='black')
    
# Show the originals have not been changed
ax,fig = make_canvas([-4,4])
for i in [A,B,C,D]:
    i.draw()