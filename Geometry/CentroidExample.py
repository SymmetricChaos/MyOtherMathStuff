from Shapes import Polygon
from Utils.Drawing import make_canvas, scatter_points

F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])
F.scale(.9)
F.shift_center()
for i in range(6):
    make_canvas([-3,3],size=3)
    scatter_points([[0,0]],color='black')
    F.rotate(.2)
    F.draw()
    F.shift_center()
    t = F.centroid()
    scatter_points([t],color='blue',zorder=3)