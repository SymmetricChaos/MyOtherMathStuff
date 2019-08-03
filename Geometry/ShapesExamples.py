from Shapes import Circle, Ellipse
from Utils.Drawing import make_canvas, plot_points, scatter_points
import matplotlib.pyplot as plt
from AffineTransforms import rotate
import numpy as np


c = Circle(2)
make_canvas([-3,3],size=4)
plot_points(c.points())
plt.scatter(c.pos[0],c.pos[1])

e = Ellipse(2.5,2)
make_canvas([-3,3],size=4)
plot_points(e.points())
scatter_points(e.foci(),color='orange')


E = e.points()
E += e.foci()
E = np.asarray(E)
P = rotate(E,1)
make_canvas([-3,3],size=4)
plot_points(P[:-2])
scatter_points(P[-2:],color='orange')