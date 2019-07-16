import matplotlib.pyplot as plt
from Utils import make_canvas, tuples_to_lists
from BezierCurves import bezier

fig,ax = make_canvas([-2.5,2.5],[-2.5,2.5])

begin = [-2,0]
end = [2,0]
control = [[-1,1],[0,1],[1,1]]

X,Y = bezier(begin,end,control)

plt.plot(X,Y,zorder=0)


plt.scatter(begin[0],begin[1],color='r')
plt.scatter(end[0],end[1],color='r')
for pt in control:
    plt.scatter(pt[0],pt[1],color='k')
    

a = tuples_to_lists([begin]+control+[end]+[begin])
plt.plot(a[0],a[1],zorder=-1,color='gray')