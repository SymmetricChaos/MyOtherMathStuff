import matplotlib.pyplot as plt
from Utils.Drawing import make_canvas
from BezierCurves import bezier

fig,ax = make_canvas([-2.5,2.5],[-2.5,2.5])

begin = [-2,0]
end = [2,0]
control = [[.5,-1],[1,2]]

X,Y = bezier(begin,end,control)

plt.plot(X,Y,zorder=0)

plt.scatter(begin[0],begin[1],color='r')
plt.scatter(end[0],end[1],color='r')
for pt in control:
    plt.scatter(pt[0],pt[1],color='k')