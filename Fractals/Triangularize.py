import matplotlib.pyplot as plt
from Utils.Drawing import make_canvas

# Recursive inner function
def triangularize_recur(x,y,n=1):
    
    if n == 0:
        return None
    centx = sum(x)/len(x)
    centy = sum(y)/len(x)
    
    plt.plot(centx,centy,'ro',zorder=3)
    for i in range(len(x)):
        x1 = x[i]
        x2 = x[(i+1)%3]
        y1 = y[i]
        y2 = y[(i+1)%3]
        triangularize_recur([centx,x1,x2],[centy,y1,y2],n-1)
        plt.plot([centx,x1],[centy,y1],'black',lw=1)
#        Code for coloring each smallest subtriangle
#        if n == 1:     
#            subtri = plt.Polygon([i for i in zip([centx,x1,x2],[centy,y1,y2])],
#                                  fc=matplotlib.colors.hsv_to_rgb([random.uniform(0,1),.8,.8]),
#                                  zorder=n,ec='black',lw=2)
#            ax.add_patch(subtri)

def triangularize(pts,depth=1):

    fig, ax = make_canvas([0,6],[0,6],[12,12])
    X = [i[0] for i in pts]
    Y = [i[1] for i in pts]
    tri = plt.Polygon(pts,ec='black')
    ax.add_patch(tri)
    triangularize_recur(X,Y,depth)
    plt.text(0,4,"Depth = {}".format(depth),size=20)
    
triangularize([[.5,1],[5.5,1],[3,5]],depth=2)