from Polygons import Polygon, regular_polygon, polygon_hull, Chain
from Utils.Drawing import make_canvas, scatter_points
import matplotlib.pyplot as plt


letter_F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])

make_canvas([-3,3],size=5)
plt.title("Letter F Polygon\nWith Center")
letter_F.rotate(.15)
letter_F.shift_center()
letter_F.draw()

scatter_points([letter_F.center],color='red',zorder=3)

make_canvas([-3,3],size=5)
plt.title("Convex Hull of F")
F_chull = polygon_hull(letter_F)
F_chull.draw_points(zorder=3)
F_chull.draw(edgecolor="black")



letter_F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])

make_canvas([-3,3],size=5)
plt.title("Letter F Rotated Around Own Center")
letter_F.scale(.7)
letter_F.draw(edgecolor='gray')
letter_F.rotate(.15)
letter_F.draw()
scatter_points([letter_F.center],color='red',zorder=3)
scatter_points([[0,0]],color='black',zorder=3)



pent = regular_polygon(5)
hexa = regular_polygon(6,.8,[0,.9])
make_canvas([-3,3],size=4)
hexa.draw(edgecolor="black")
pent.draw(edgecolor="black")
C = Chain([[0,0],[.8,.4],[1,1.3],[-1,1]])
C.draw()
print(C.length)