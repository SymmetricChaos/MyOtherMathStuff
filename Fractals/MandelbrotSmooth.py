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
            ## Check if the point is within the main bulb
            p = math.sqrt((a-0.25)*(a-0.25)+b*b)
            if(x < p-2*p*p+0.25):
                imarr[x][y] = 0
                continue
            ## If its not then start calculating
            for i in range(n+1):
                a1 = (a*a)-(b*b) + xr[x]
                b1 = 2*(a*b) + yr[y]
                d = math.sqrt(a1*a1+b1*b1)
                if(d > 10000):
                    imarr[x][y] = i-np.log2(np.log(d)/20000)
                    break
                a,b = a1,b1
                if(i == n):
                    imarr[x][y] = 0
            
    return(imarr)

a = mandel(n=20,m=100)

import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(31,31)
ax = plt.Axes(fig,[0.,0.,1.,1.])
ax.set_axis_off()
fig.add_axes(ax)
plt.set_cmap("hot")
ax.imshow(a)
plt.savefig("TEST1.png",dpi=100)
