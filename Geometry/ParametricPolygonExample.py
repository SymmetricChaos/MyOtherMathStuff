from Utils.Drawing import make_canvas, scatter_points
from ParametricPolygon import parametric_polygon


make_canvas([-1.2,1.2])
scatter_points(parametric_polygon(7))
scatter_points([[0,0]])