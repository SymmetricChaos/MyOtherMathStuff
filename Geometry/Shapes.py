import numpy as np
import matplotlib.pyplot as plt
from ConvexHull import convex_hull
from Utils.Drawing import scatter_points, plot_points
from CheckIntersect import do_intersect

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
        if len(verts) < 3:
            raise Exception("Not a polygon.")
        self.verts = verts


    def draw(self,facecolor="#00000000",edgecolor="black",**kwargs):
        ax = plt.gca()
        poly = plt.Polygon(self.verts,facecolor=facecolor,edgecolor=edgecolor,**kwargs)
        ax.add_patch(poly)


    def draw_points(self,color="black",**kwargs):
        scatter_points(self.verts,color=color,**kwargs)


    def copy(self):
        return Polygon(self.verts[:])


    def area(self):
        return abs(self.signed_area())
    
    
    def signed_area(self):
        if self.simple():
            area = 0
            v = self.verts.copy()
            v += [v[0]]
            for i in range(len(v)-1):
                area += v[i][0]*v[i+1][1] - v[i+1][0]*v[i][1]
            return area/2
        else:
            raise Exception("Area not uniquely defined by self-intersecting polygons.")


    def verts_x(self):
        return [i[0] for i in self.verts]


    def verts_y(self):
        return [i[1] for i in self.verts]


    def center(self):
        return [ np.mean(self.verts_x()), np.mean(self.verts_y())]


    def centroid(self):
        print("centroid does not calculate correctly")
        x = 0
        y = 0
        A = self.area()
        X = self.verts_x()
        Y = self.verts_y()
        X += [X[0]]
        Y += [Y[0]]
        for i in range(len(X)-1):
            x += (X[i] + X[i+1]) * (X[i]*Y[i+1] - X[i+1]*Y[i])
            y += (Y[i] + Y[i+1]) * (X[i]*Y[i+1] - X[i+1]*Y[i])
        return [x/(6*A),y/(6*A)]


    def shift_center(self):
        x,y = self.center()
        self.verts = [[i[0]-x,i[1]-y] for i in self.verts]


    def shift_centroid(self):
        x,y = self.centroid()
        self.verts = [[i[0]-x,i[1]-y] for i in self.verts]


    def shift_xy(self,x=0,y=0):
        self.verts = [[i[0]+x,i[1]+y] for i in self.verts]


    def scale(self,s=1):
        M = np.array([[s,0],[0,s]])
        self.verts = np.matmul(self.verts,M)
        
        
    def rotate(self,th=0):
        """Rotate by full-turns around the origin"""
        th = np.pi*2*th
        M = np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
        self.verts = np.matmul(self.verts,M)


    def mirror_x(self):
        self.verts = [[-i[0],i[1]] for i in self.verts]


    def mirror_y(self):
        self.verts = [[i[0],-i[1]] for i in self.verts]

    
    def simple(self):
        return not check_self_intersect(self)



class PolygonSet:
    def __init__(self,polygons):
        assert type(polygons) == list
        for i in polygons:
            assert type(i) == Polygon
        self.polygons = polygons


    def draw(self,facecolor="white",edgecolor="black",linewidth=1,linestyle="-"):
        for poly in self.polygons:
            poly.draw(facecolor,edgecolor,linewidth,linestyle)


    def shift_xy(self,x=0,y=0):
        for poly in self.polygons:
            poly.shift_xy(x,y)



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


def polygon_hull(polygon):
    """Return to convex hull of a polygon"""
    return Polygon(convex_hull(polygon))


def check_self_intersect(polygon):
    """Crude slow way to check for self intersection"""
    V = polygon.verts.copy()
    m = len(V)
    for i in range(m):
        for j in range(m):
            if (i+1)%m == j or (i-1)%m == j or i == j:
                pass
            else:
                if do_intersect(V[i%m],V[(i+1)%m],V[j%m],V[(j+1)%m]):
                    return True
                


    