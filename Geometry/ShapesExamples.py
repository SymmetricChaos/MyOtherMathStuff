from Shapes import Circle, Ellipse
from Utils.Drawing import make_canvas
from Utils.ListManip import tuples_to_lists
import matplotlib.pyplot as plt
from AffineTransforms import rotate
import numpy as np

make_canvas([-3,3])

e = Ellipse(3,1)
print(e.ecc)
print(e.focal_dist)

c = Circle(2)
x = c.points_x()
y = c.points_y()
plt.plot(x,y)
plt.scatter(c.pos[0],c.pos[1])

make_canvas([-3,3])
e = Ellipse(2.5,2)
x = e.points_x()
y = e.points_y()
plt.plot(x,y)
plt.scatter(e.focal_dist,0,color='orange')
plt.scatter(-e.focal_dist,0,color='orange')


E = e.points()
E += e.foci()
E = np.asarray(E)
P = rotate(E,1)

x,y = tuples_to_lists(P)

make_canvas([-3,3])
plt.plot(x[:-2],y[:-2])
plt.scatter(x[-2:],y[-2:],color='orange')