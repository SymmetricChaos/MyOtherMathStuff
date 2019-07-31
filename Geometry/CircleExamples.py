from Utils.Drawing import make_canvas
from Geometry.Shapes import Circle
from Geometry.CircleIntersection import circle_intersect


make_canvas([-3,3])
circs = [Circle(1.8,[0,.5]),
         Circle(.9,[2,0]),
         Circle(.7,[1.5,1])]

for C in circs:
    C.draw()

for i in range(3):
    circle_intersect(circs[i].pos,circs[i].r,circs[(i+1)%3].pos,circs[(i+1)%3].r,dots=True)

