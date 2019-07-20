from Utils import make_canvas
from BezierCurves import bezier_string_art

begin = [-2,-1]
end = [2,-1]
control = [-1,1.5]
fig,ax = make_canvas([-2.5,2.5],[-2.5,2.5])
bezier_string_art(begin,end,control,8)