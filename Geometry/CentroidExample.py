from Shapes import Polygon
from Utils.Drawing import make_canvas, scatter_points

F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])
F.scale(.9)
F.shift_center()
for i in range(3):
    make_canvas([-3,3],size=3)
#    scatter_points([[0,0]],color='black')
    F.rotate(.1)
    F.draw()
    t = F.centroid()
    print(t)
    scatter_points([t],color='blue',zorder=3)
    print()
    
#F = Polygon([[0,0],[0,1],[1,1],[1,0]])
#F.scale(.9)
#F.shift_center()
#for i in range(3):
#    make_canvas([-3,3],size=3)
#    F.rotate(.2)
#    F.draw()
#    t = F.centroid()
#    scatter_points([t],color='blue',zorder=3)

