from Polygons import star_polygon, check_self_intersect
from Utils.Drawing import make_canvas

P = star_polygon(7,2)

print(check_self_intersect(P))
make_canvas([-1,1],size=3)
P.draw()
P.area()