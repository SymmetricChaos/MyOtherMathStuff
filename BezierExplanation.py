from Utils import make_canvas
from BezierCurves import bezier_string_art_quadratic, bezier_string_art_cubic

begin = [-2,-1]
end = [2,-1]
control = [-1,1.5]
fig,ax = make_canvas([-2.5,2.5],[-2.5,2.5])
bezier_string_art_quadratic(begin,end,control,8)

begin = [-2.2,-2]
end = [2.2,-2]
control1 = [-1,1]
control2 = [1.2,2]
fig,ax = make_canvas([-2.5,2.5],[-2.5,2.5],[9,9])
bezier_string_art_cubic(begin,end,control1,control2,20)