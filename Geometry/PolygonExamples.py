from Shapes import Polygon, regular_polygon, star_polygon
from Utils.Drawing import make_canvas, plot_points, scatter_points
import matplotlib.pyplot as plt
from AffineTransforms import rotate, reflect_y, shift_xy
import numpy as np


letter_F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],[1.5,2],[.5,2],[.5,2.5],[2,2.5],[2,3],[0,3]])

make_canvas([-3,3],size=5)

letter_F.verts = rotate(np.array(letter_F.verts),1)
#letter_F.verts = shift_xy(np.array(letter_F.verts),-.3,-2)
letter_F.shift_center()
letter_F.draw()

scatter_points([letter_F.center()],color='red',zorder=3)
scatter_points([letter_F.centroid()],color='blue',zorder=3)

#pent = regular_polygon(5)
#hexa = regular_polygon(6,.8,[0,.9])
#make_canvas([-3,3],size=4)
#hexa.draw()
#pent.draw()

#star = star_polygon(7,3,pos=[0,-1.5])
#star.draw()