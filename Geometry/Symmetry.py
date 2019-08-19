from Polygons import Polygon
from Utils.Drawing import make_canvas

letter_F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])

ax,fig = make_canvas([-4,4],[-1.5,1.5],show_axes=False)
letter_F.scale(.5)
letter_F.shift_center()
letter_F.rotate(.5)
letter_F.shift_xy(x=-4,y=-.6)
for i in range(6):
    letter_F.draw(linewidth=3)
    letter_F.shift_xy(x=1.5)

letter_F.shift_center()
letter_F.rotate(.5)
letter_F.shift_xy(x=-3.8,y=.6)
for i in range(6):
    letter_F.draw(linewidth=3,edgecolor='red')
    letter_F.shift_xy(x=1.5)