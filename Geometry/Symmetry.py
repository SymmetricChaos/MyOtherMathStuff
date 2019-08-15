from Shapes import Polygon
from Utils.Drawing import make_canvas


letter_F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])

make_canvas([-4,4])
letter_F.shift_center()
letter_F.shift_xy(y=1)
letter_F.draw(linewidth=3)