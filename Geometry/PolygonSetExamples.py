from Polygons import Polygon, PolygonSet, regular_polygon
from Utils.Drawing import make_canvas, scatter_points


    
    
A = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])
B = regular_polygon(5,r=.9,pos=[2,2])
C = regular_polygon(3,r=.6,pos=[0,-2.5])
D = Polygon([[0,0],[.3,.5],[.5,1.5],[.2,1],[-.2,1],[-.7,1.2]])


S1 = PolygonSet([A,B,C,D])
S1[0].scale(.5)
S1[0].rotate(-.1)
S1[1].rotate(.07)
S1[3].mirror("y",pos=[0,0])
S1[3].shift(-1,-.5)


ax,fig = make_canvas([-4,4])
S1.draw(linewidth=3)
S1[2].draw_points(zorder=3,color='orange',s=200)
for i in S1:
    scatter_points([i.centroid],color='black')

for i in S1:
    print(i)
    print()
    
# Show the originals have not been changed
ax,fig = make_canvas([-4,4])
for i in [A,B,C,D]:
    i.draw()