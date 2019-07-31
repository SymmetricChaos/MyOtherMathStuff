import math
import numpy as np

def mandel(n=30,m=30):

    imarr = np.zeros((m*3+1,m*3+1))
    
    r = math.floor(m*1.5)
    xr = [x / float(m) -0.75 for x in range(-r,r+1,1)]
    yr = [x / float(m) for x in range(-r,r+1,1)]
    print(len(xr))

    for x in range(m*3+1):
        for y in range(m*3+1):
            a,b = xr[x],yr[y]
            for i in range(n+1):
                a1 = (a*a)-(b*b) + xr[x]
                b1 = 2*(a*b) + yr[y]
                if(math.sqrt(a1*a1+b1*b1) > 2):
                    imarr[x][y] = i
                    break
                a,b = a1,b1
                if(i == n):
                    imarr[x][y] = n
            
    return(imarr)

a = mandel(n=20,m=100)

import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(15,15)
ax = plt.Axes(fig,[0.,0.,1.,1.])
ax.set_axis_off()
fig.add_axes(ax)
plt.set_cmap("hot")
ax.imshow(a)
#plt.savefig("Mandelbrot.png",dpi=80)

#import csv
#with open("PythonMandel.csv","w",newline="") as csvfile:
#    wtr = csv.writer(csvfile, delimiter = ",")
#    wtr.writerow(a)
