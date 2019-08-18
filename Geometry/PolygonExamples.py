from Shapes import Polygon, regular_polygon, polygon_hull
from Utils.Drawing import make_canvas, scatter_points
import matplotlib.pyplot as plt

letter_F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])

make_canvas([-3,3],size=5)
plt.title("Letter F Polygon\nWith Centroid and Center")
letter_F.rotate(.15)
letter_F.shift_center()
letter_F.draw()

scatter_points([letter_F.center()],color='red',zorder=3)
scatter_points([letter_F.centroid()],color='blue',zorder=3)


make_canvas([-3,3],size=5)
plt.title("Convex Hull of F")
F_chull = polygon_hull(letter_F)
F_chull.draw()
scatter_points(F_chull.verts,zorder=3)

pent = regular_polygon(5)
hexa = regular_polygon(6,.8,[0,.9])
make_canvas([-3,3],size=4)
hexa.draw()
pent.draw()
