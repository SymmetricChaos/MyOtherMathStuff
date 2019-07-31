from Graphs.Graph import *

L = [2,3,5,10,15,30]

## Relational diagram is set to 1 if i divides j and zero otherwise
R = np.zeros((len(L),len(L)))
for x,i in enumerate(L):
    for y,j in enumerate(L):
        if i != j and i % j == 0:
            R[x,y] = 1


            
def connectogram(L,R):
    #print(R)
    fig,ax = makeCanvas(size=[10,10])
    n = len(L)
    xy = arc((0,0),2.5,np.pi*2,n)
    xy[:n]
    G = []
    
    for i,pos in enumerate(xy):
        G.append(Graph(pos,text=str([L[i]][0]),r=.3,tscale=70,z=2))
        
    drawNodes(G,ax)
    
    for i in np.argwhere(R==1):
        ter = distpt(G[i[1]],G[i[0]],.32)
        connectArrPts(G[i[1]].x,G[i[1]].y,ter[0],ter[1],width=1.5,headwidth=.1,headlength=.2)


connectogram(L,R)