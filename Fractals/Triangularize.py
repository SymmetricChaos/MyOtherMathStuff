import matplotlib.pyplot as plt

def makeCanvas(x=[-3,3],y=[-3,3],size=[7,7]):
    fig = plt.figure()
    fig.set_size_inches(size[0], size[1])
    ax = plt.axes(xlim=x, ylim=y)
    ax.axis('off')
    return fig, ax

def triangularize(x,y,n=1):
    
    if n == 0:
        return None
    centx = sum(x)/len(x)
    centy = sum(y)/len(x)
    
    #plt.plot(centx,centy,'ro',zorder=3)
    for i in range(len(x)):
        x1 = x[i]
        x2 = x[(i+1)%3]
        y1 = y[i]
        y2 = y[(i+1)%3]
        triangularize([centx,x1,x2],[centy,y1,y2],n-1)
        plt.plot([centx,x1],[centy,y1],'black',lw=1)
        #if n == 1:
            
            #subtri = plt.Polygon([i for i in zip([centx,x1,x2],[centy,y1,y2])],
            #                      fc=matplotlib.colors.hsv_to_rgb([random.uniform(0,1),.8,.8]),
            #                      zorder=n,ec='black',lw=2)
            #ax.add_patch(subtri)
            

N = 3
fig, ax = makeCanvas([0,6],[0,6],[12,12])
pts = [[0,1],[6,1],[2,5]]
X = [i[0] for i in pts]
Y = [i[1] for i in pts]
tri = plt.Polygon(pts,ec='black')
ax.add_patch(tri)
triangularize(X,Y,N)
plt.text(0,4,"Depth = {}".format(N),size=20)