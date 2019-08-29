from Utils.Drawing import make_canvas, scatter_points
from ParametricPolygon import parametric_polygon


make_canvas([-3,3])
scatter_points(parametric_polygon(7))
scatter_points([[0,0]])