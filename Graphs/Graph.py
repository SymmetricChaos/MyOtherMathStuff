import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance

class Graph:
    def __init__(self,xlims=[-3,3],ylims=[-3,3],size=[7,7],
                 rdef=.5,tscaledef=30,coldef=(.53, .81, .94)):

        ## Setup the plot area
        self.fig = plt.figure()
        self.fig.set_size_inches(size[0], size[1])
        self.ax = plt.axes(xlim=xlims, ylim=ylims)
        self.ax.axis('off')
        
        # Set a few default characteristics
        self.rdef = rdef
        self.tscaledef = tscaledef
        self.coldef = coldef
        
        # Prepare a list of nodes
        self.Nodes = []
        
        # Prepare a matrix of connections
        self.Mat = [0]
    
    def addNode(self,xy=[0,0],r=None,col=[None],text="",tscale=None,z=1):
        if r == None:
            r = self.rdef
        if tscale == None:
            tscale = self.tscaledef
        if any(i == None for i in col):
            col = self.coldef
        self.Nodes.append(Node(xy,r,col,text,tscale,z))

        t = np.zeros((len(self.Nodes),len(self.Nodes)))
        t[:-1,:-1] = self.Mat
        self.Mat = t
        
    def addEdge(self,A,B,d=1):
        self.Mat[A,B] = d
        
    def addEdges(self,A,B,D=[None]):
        if any(i == None for i in D):
            D = [1]*len(A)
        self.Mat[A,B] = D

    def QuickDraw(self):
        for i in self.Nodes:
            self.ax.add_patch(i.circ)
            plt.text(i.xy[0],i.xy[1],i.text,size=i.r*i.tscale,
                 ha='center',va='center',zorder=i.z)
        for i in np.argwhere(self.Mat != 0):
            ter = distpt(self.Nodes[i[0]],self.Nodes[i[1]],.32)
            plt.plot([self.Nodes[i[0]].x,ter[0]],[self.Nodes[i[0]].y,ter[1]],
                     color="black",lw=2,zorder=0)

    def drawNodes(self):
        for i in self.Nodes:
            self.ax.add_patch(i.circ)
    
    def drawText(self):
        for i in self.Nodes:
            plt.text(i.xy[0],i.xy[1],i.text,size=i.r*i.tscale,
                 ha='center',va='center',zorder=i.z)
    
    def drawArrows(self,col="black",wd=1,hwd=.1,hln=.2):
        for i in np.argwhere(self.Mat != 0):
            ter = distpt(self.Nodes[i[0]],self.Nodes[i[1]],.32)
            connectArrPts(self.Nodes[i[0]].x,self.Nodes[i[0]].y,ter[0],ter[1],
                          width=wd,headwidth=hwd,headlength=hln,zorder=0,color=col)
            
    def drawLines(self,col="black",wd=1):
        for i in np.argwhere(self.Mat != 0):
            ter = distpt(self.Nodes[i[0]],self.Nodes[i[1]],.32)
            plt.plot([self.Nodes[i[0]].x,ter[0]],[self.Nodes[i[0]].y,ter[1]],
                     color=col,lw=wd,zorder=0)
            
class Node:
    def __init__(self,xy=[0,0],r=.5,col=(.53, .81, .94),text="",tscale=30,z=1):
        self.xy = xy
        self.x = xy[0]
        self.y = xy[1]
        self.r = r
        self.col = col
        self.z = z
        self.text = text
        self.tscale = tscale
        self.circ = plt.Circle(self.xy,radius = self.r, fc = self.col,zorder=self.z)

    def update(self,xy=None,r=None,col=[None],text=None,tscale=None,z=None):
        if xy != None:
            self.xy = xy
            self.x = xy[0]
            self.y = xy[1]
        if r != None:
            self.r = r
        if any(i == None for i in col):
            pass
        else:
            self.col = col
        if z != None:
            self.z = z
        if text != None:
            self.text = text
        if tscale != None:
            self.tscale = tscale

        self.circ = plt.Circle(self.xy,radius = self.r, fc = self.col,zorder=self.z)
    

# Draw straight line connections between nodes
def connect(A,B,col="black",width=1,z=0):
    plt.plot([A.x,B.x],[A.y,B.y],color=col,lw=width,zorder=z)

def connectArr(A,B,col="black",width=1,headwidth=.2,headlength=.2,z=0):
    plt.arrow(A.x,A.y,B.x-A.x,B.y-A.y,color=col,lw=width,zorder=z,
              head_width=headwidth, head_length=headlength,
              length_includes_head=True)

# Same functionality between points arbitrary points

def connectPts(x1,y1,x2,y2,col="black",width=1,z=0):
    plt.plot([x1,x2],[y1,y2],color=col,lw=width,zorder=z)
    
def connectArrPts(x1,y1,x2,y2,col="black",width=1,headwidth=.2,headlength=.2,z=0):
    plt.arrow(x1,y1,x2-x1,y2-y1,color=col,lw=width,zorder=z,
          head_width=headwidth, head_length=headlength,
          length_includes_head=True)

def CircThruPoints(A,B,r,inv=False):
    if A.xy == B.xy:
        raise ValueError('identical positions')
    d = dist(A,B)
    dx, dy = A.x-B.x, A.y-B.y
    md = np.sqrt((r**2)-(d/2)**2)
    if d > r:
        raise ValueError('separation of points > diameter')
    x3,y3 = midpt(A,B)
    if inv == False:
        X = x3 - md*dy/d
        Y = y3 + md*dx/d
    else: 
        X = x3 + md*dy/d
        Y = y3 - md*dx/d
    return X,Y

def connectArc(A,B,r,inv=False):
    x,y = CircThruPoints(A,B,r,inv)
    
    dx0 = A.x-x
    dx1 = B.x-x
    
    if inv == False:
        th0 = np.arccos(dx0/r)
        th1 = np.arccos(dx1/r)
    else:
        th0 = -np.arccos(dx0/r)
        th1 = -np.arccos(dx1/r)
    
    xy = arcXY([x,y],r,[th0,th1],100)

    plt.plot(xy[0],xy[1],color="black",lw=2,zorder=0)

# Miscelaneous functions        
def arc(xy,r,th,n):
    x = np.cos(np.linspace(0,th,n+1))*r+xy[0]
    y = np.sin(np.linspace(0,th,n+1))*r+xy[1]
    x = x[:n]
    y = y[:n]
    return [(a,b) for (a,b) in zip(x,y)]

def arcXY(xy,r,th=[0,np.pi],n=100):
    x = np.cos(np.linspace(th[0],th[1],n+1))*r+xy[0]
    y = np.sin(np.linspace(th[0],th[1],n+1))*r+xy[1]
    x = x[:n]
    y = y[:n]
    return [x,y]

def dist(A,B):
    p1 = (A.x-B.x)**2
    p2 = (A.y-B.y)**2
    return np.sqrt(p1+p2)

def distMat(L):
    ps = [(i.x,i.y) for i in L]
    return distance.squareform(np.round(distance.pdist(ps),3))


# Find midpoints in two dimensions or in one
def midpt(A,B):
    x = (A.x + B.x)/2
    y = (A.y + B.y)/2
    return [x,y]

def midX(A,B):
    return (A.xy[0] + B.xy[0])/2

def midY(A,B):
    return (A.xy[1] + B.xy[1])/2

# Find the point that is some percentage of the way between A and B
# 0 is at the centerof A, 1 is at the center of B
def perpt(A,B,p):
    x = (A.x)*(1-p) + (B.x)*(p)
    y = (A.y)*(1-p) + (B.y)*(p)
    return [x,y]

# Find the point that is some distance from B along the line between A and B
def distpt(A,B,d):
    dd = dist(A,B)
    if dd == 0:
        return A.xy
    p = (dd-d)/(dd)
    return perpt(A,B,p)


# Find the minimum and maximum of a list
def minmax(L):
    return [min(L),max(L)]

def test():

    G = Graph([-3,3],[-3,3],[7,7],rdef=.3)
    G.addNode()
    print(G.Mat)
    G.addNode([-2,0],text="Hello")
    print(G.Mat)
    
    G.addNode([1,-1])
    print(G.Mat)
    G.addEdge(0,1)
    G.addEdge(1,2)
    print(G.Mat)
    G.QuickDraw()
    
    connectArc(G.Nodes[0],G.Nodes[1],2.5)
    #connectArc(G.Nodes[0],G.Nodes[1],5)
#test()
