import numpy as np
import matplotlib.pyplot as plt

class Circle:
    def __init__(self,r,pos=[0,0]):
        self.r = r
        self.pos = pos
    
    
    def draw(self,facecolor="white",edgecolor="black",linewidth=1,linestyle="-"):
        ax = plt.gca()
        circ = plt.Circle(self.pos,radius = self.r,
                          edgecolor = edgecolor, facecolor = facecolor,
                          linewidth = linewidth, linestyle = linestyle)
        ax.add_patch(circ)
        
        
    def points(self,n=100):
        th = np.linspace(0,2*np.pi,n)
        return [[x*self.r+self.pos[0],y*self.r+self.pos[1]] for x,y in zip(np.sin(th),np.cos(th))]
      
        
    def points_x(self,n=100):
        th = np.linspace(0,2*np.pi,n)
        return np.sin(th)*self.r+self.pos[0]
    
    
    def points_y(self,n=100):
        th = np.linspace(0,2*np.pi,n)
        return np.cos(th)*self.r+self.pos[1]
    
    
    def area(self):
        return self.r*self.r*np.pi


    def shift_center(self):
        self.pos = [0,0]


    def shift_xy(self,x=0,y=0):
        self.pos = [self.pos[0]+x, self.pos[1]+y]


           
        
class Ellipse:
    def __init__(self,a,b,pos=[0,0]):
        # Silently orient the ellipse so that a is always the semimajor axis
        if b > a:
            a,b = b,a
        self.a = a
        self.b = b
        self.pos = pos


    def draw(self,facecolor="white",edgecolor="black",linewidth=1,linestyle="-"):
        ax = plt.gca()
        circ = plt.Ellipse(self.pos, width = self.a, height = self.b,
                          edgecolor = edgecolor, facecolor = facecolor,
                          linewidth = linewidth, linestyle = linestyle)
        ax.add_patch(circ)


    def points(self,n=100):
        th = np.linspace(0,2*np.pi,n)
        return [[x*self.a+self.pos[0],y*self.b+self.pos[0]] for x,y in zip(np.sin(th),np.cos(th))]
      
        
    def points_x(self,n=100):
        th = np.linspace(0,2*np.pi,n)
        return np.sin(th)*self.a+self.pos[0]
    
    
    def points_y(self,n=100):
        th = np.linspace(0,2*np.pi,n)
        return np.cos(th)*self.b+self.pos[1]
        
    
    def foci(self):
        return [[-self.focal_dist(),self.pos[1]],[self.focal_dist(),self.pos[1]]]


    def area(self):
        return np.pi*self.a*self.b
    
    
    def ecc(self):
        return np.sqrt(1-((self.b**2)/(self.a**2)))
    
    
    def focal_dist(self):
        return self.ecc()*self.a
    
    
    def shift_center(self):
        self.pos = [0,0]


    def shift_xy(self,x=0,y=0):
        self.pos = [self.pos[0]+x, self.pos[1]+y]



class Polygon:
    def __init__(self,verts):
        self.verts = verts


    def draw(self,facecolor="white",edgecolor="black",linewidth=1,linestyle="-"):
        ax = plt.gca()
        circ = plt.Polygon(self.verts,
                          edgecolor = edgecolor, facecolor = facecolor,
                          linewidth = linewidth, linestyle = linestyle)
        ax.add_patch(circ)


    def area(self):
        # Needs to check for self intersection
        area = 0
        for i in range(len(self.verts)-1):
            area += self.verts[i][0]*self.verts[i+1][1] - self.verts[i+1][0]*self.verts[i][1]
        return abs(area/2)
    

    def verts_x(self):
        return [i[0] for i in self.verts]


    def verts_y(self):
        return [i[1] for i in self.verts]


    def center(self):
        return [ np.mean(self.verts_x()), np.mean(self.verts_y())]


    def centroid(self):
        x = 0
        y = 0
        A = self.area()
        X = self.verts_x()
        Y = self.verts_y()
        for i in range(len(self.verts)-1):
            x += (X[i]+X[i+1])*(X[i]*Y[i+1]-X[i+1]*Y[i])
            y += (Y[i]+Y[i+1])*(X[i]*Y[i+1]-X[i+1]*Y[i])
        return [x/6*A,y/6*A]


    def shift_center(self):
        x,y = self.center()
        self.verts = [[i[0]-x,i[1]-y] for i in self.verts]


    def shift_centroid(self):
        x,y = self.centroid()
        self.verts = [[i[0]-x,i[1]-y] for i in self.verts]


    def shift_xy(self,x=0,y=0):
        self.verts = [[i[0]+x,i[1]+y] for i in self.verts]


    def scale(self,s):
        M = np.array([[s,0],[0,s]])
        self.verts = np.matmul(self.verts,M)
    

def regular_polygon(n,r=1,pos=[0,0]):
    c = Circle(r=r,pos=pos)
    return Polygon(c.points(n+1)[0:-1])


def star_polygon(p,q,r=1,pos=[0,0]):
    V = regular_polygon(p,r=r,pos=pos).verts
    star = []
    pos = 0
    for i in range(p*q):
        star.append(V[pos])
        pos = (pos+q)%p
    return Polygon(star)


#def polygon_intersection(polygon):
#   """Check if a polygon is self intersecting"""
#    v = polygon.verts

#def polygon_hull(polygon):