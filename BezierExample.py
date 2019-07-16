import matplotlib.pyplot as plt
from Utils import make_canvas
from BezierCurves import bezier

fig,ax = make_canvas([-2.5,2.5],[-2.5,2.5])

begin = [-2,0]
end = [2,0]
control = [[.5,-1],[0,1.5]]

X,Y = bezier(begin,end,control)

plt.plot(X,Y)

for pt in control:
    plt.scatter(pt[0],pt[1],color='k')