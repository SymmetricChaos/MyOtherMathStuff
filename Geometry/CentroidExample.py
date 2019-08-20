from Polygons import Polygon
from Utils.Drawing import make_canvas, scatter_points

F1 = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])
F2 = F1.copy()
F1.scale(.9)
F1.shift_centroid()
F2.scale(.9)
F2.shift_center()
for i in range(5):
    make_canvas([-3,3],size=3)
    scatter_points([[0,0]],color='black')
    F1.draw()
    F1.rotate(.2)
    F2.draw(edgecolor='gray')
    F2.rotate(.2)
    