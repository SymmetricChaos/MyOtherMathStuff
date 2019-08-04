from Shapes import Circle, Ellipse
from Utils.Drawing import make_canvas, plot_points, scatter_points
import matplotlib.pyplot as plt
from AffineTransforms import rotate, reflect_y
import numpy as np


c = Circle(2)
make_canvas([-3,3],size=4)
plot_points(c.points())
plt.scatter(c.pos[0],c.pos[1])

e = Ellipse(2.5,2)
E = e.points()
E += e.foci()
E = np.asarray(E)

make_canvas([-3,3],size=4)
plot_points(E[:-2])
scatter_points(E[100:101],color='orange')
scatter_points(E[101:102],color='green')

P = reflect_y(rotate(E,1))
make_canvas([-3,3],size=4)
plot_points(P[:-2])
scatter_points(P[100:101],color='orange')
scatter_points(P[101:102],color='green')