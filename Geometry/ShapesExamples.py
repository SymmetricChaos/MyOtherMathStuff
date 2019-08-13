from Shapes import Circle, Ellipse, Polygon
from Utils.Drawing import make_canvas, plot_points, scatter_points
import matplotlib.pyplot as plt
from AffineTransforms import rotate, reflect_y, shift_xy
import numpy as np


c = Circle(2)
make_canvas([-3,3],size=4)
plot_points(c.points())
plt.scatter(c.pos[0],c.pos[1])


e = Ellipse(2.5,2)
E = e.points()
E += e.foci()
E = np.asarray(E)


letter_F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])

make_canvas([-3,3],size=4)
letter_F.draw()

letter_F.verts = rotate(np.array(letter_F.verts),1)
letter_F.verts = shift_xy(np.array(letter_F.verts),-.3,-2)

print(letter_F.verts)

letter_F.draw()
#make_canvas([-3,3],size=4)
#plot_points(E[:-2])
#scatter_points(E[100:101],color='orange')
#scatter_points(E[101:102],color='green')
#
#
#P = reflect_y(rotate(E,1))
#make_canvas([-3,3],size=4)
#plot_points(P[:-2])
#scatter_points(P[100:101],color='orange')
#scatter_points(P[101:102],color='green')