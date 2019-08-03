from Shapes import Circle, Ellipse
from Utils.Drawing import make_canvas
import matplotlib.pyplot as plt

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