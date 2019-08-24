from Polygons import Polygon, PolygonSet
from Utils.Drawing import make_canvas
import matplotlib.pyplot as plt

F = Polygon([[0,0],[.5,0],[.5,1.5],[1.5,1.5],
             [1.5,2],[.5,2],[.5,2.5],[2,2.5],
             [2,3],[0,3]])
F.scale(.4)
F.shift_center()


S1 = PolygonSet([F,F])

S1[0].shift(0,.5)

S1[1].rotate(.5)
S1[1].shift(y=-.5)

S1.shift(-3.5,-.2)



S2 = PolygonSet([F,F])

S2[1].mirror("x")
S2[1].shift(1)

S2.shift(-3.5)




S3 = PolygonSet([F,F])

S3[1].mirror("y")
S3[1].shift(.4,-1)
S3.shift_center()
S3.shift(-3.4)



S4 = PolygonSet([F,F])

S4[0].shift(y=-.6)

S4[1].mirror("y")
S4[1].shift(y=.6)

S4.shift(-3.5)



S5 = PolygonSet([F,F,F,F])
S5[0].shift(.6,-.6)

S5[1].mirror("y")
S5[1].shift(.6,.6)

S5[2].mirror("x")
S5[2].shift(-.3,-.6)

S5[3].mirror("x")
S5[3].mirror("y")
S5[3].shift(-.3,.6)

S5.shift(-3.2)



F.shift_centroid()
F.shift(-3.6)


ax,fig = make_canvas([-4,4],[-1.5,1.5])
for i in range(8):
    F.draw(linewidth=3)
    F.shift(1)
plt.title("Frieze Group p1",fontsize=20)

ax,fig = make_canvas([-4,4],[-1.5,1.5])
for i in range(8):
    S1.draw(linewidth=3)
    S1.shift(1)
plt.title("Frieze Group p2",fontsize=20)

ax,fig = make_canvas([-4,4],[-1.5,1.5])
for i in range(4):
    S2.draw(linewidth=3)
    S2.shift(2)
plt.title("Frieze Group p1m1",fontsize=20)

ax,fig = make_canvas([-4,4],[-1.5,1.5])
for i in range(8):
    S3.draw(linewidth=3)
    S3.shift(1)
plt.title("Frieze Group p11g",fontsize=20)

ax,fig = make_canvas([-4,4],[-1.5,1.5])
for i in range(8):
    S4.draw(linewidth=3)
    S4.shift(1)
plt.title("Frieze Group p11m",fontsize=20)

ax,fig = make_canvas([-4,4],[-1.5,1.5])
for i in range(8):
    S5.draw(linewidth=3)
    S5.shift(2)
plt.title("Frieze Group p2mm",fontsize=20)
