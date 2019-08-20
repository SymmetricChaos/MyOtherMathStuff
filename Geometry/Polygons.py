import numpy as np
import matplotlib.pyplot as plt
from ConvexHull import convex_hull
from Utils.Drawing import scatter_points
from CheckIntersect import do_intersect
from Shapes import Circle

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
        """Create an identical Polygon"""
        return Polygon(self.verts[:])


    def area(self):
        """Calculate area"""
        return abs(self.signed_area())
    
    
    def signed_area(self):
        """Calculate signed area"""
        area = 0
        X = self.verts_x()
        Y = self.verts_y()
        X += [X[0]]
        Y += [Y[0]]
        for i in range(len(X)-1):
            area += X[i]*Y[i+1] - X[i+1]*Y[i]
        return area/2


    def verts_x(self):
        """x-coordinates of the vertices"""
        return [i[0] for i in self.verts]


    def verts_y(self):
        """y-coordinates of the vertices"""
        return [i[1] for i in self.verts]


    def center(self):
        """Return arithmetic mean of the vertices"""
        return [ np.mean(self.verts_x()), np.mean(self.verts_y())]


    def centroid(self):
        """Return centroid of the polygon"""
        x = 0
        y = 0
        A = self.signed_area()
        X = self.verts_x()
        Y = self.verts_y()
        X += [X[0]]
        Y += [Y[0]]
        for i in range(len(X)-1):
            x += (X[i] + X[i+1]) * (X[i]*Y[i+1] - X[i+1]*Y[i])
            y += (Y[i] + Y[i+1]) * (X[i]*Y[i+1] - X[i+1]*Y[i])
        return [x/(6*A),y/(6*A)]


    def shift_center(self):
        """Center the polygon using arithmetic mean of the vertices"""
        x,y = self.center()
        self.verts = [[i[0]-x,i[1]-y] for i in self.verts]


    def shift_centroid(self):
        """Center the polygon using centroid"""
        x,y = self.centroid()
        self.verts = [[i[0]-x,i[1]-y] for i in self.verts]


    def shift_xy(self,x=0,y=0):
        """Shift position"""
        self.verts = [[i[0]+x,i[1]+y] for i in self.verts]


    def scale(self,s=1):
        """Scale relative to the origin"""
        M = np.array([[s,0],[0,s]])
        self.verts = np.matmul(self.verts,M)
        
        
    def rotate(self,th=0):
        """Rotate by full-turns around the origin"""
        th = np.pi*2*th
        M = np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
        self.verts = np.matmul(self.verts,M)
    
    
    def rotate_center(self,th=0):
        """Rotate by full-turns around the center of the polygon"""
        th = np.pi*2*th
        x,y = self.center()
        self.shift_center()
        M = np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
        self.verts = np.matmul(self.verts,M)
        self.shift_xy(x,y)

    def mirror_x(self):
        """Mirror across the x axis"""
        self.verts = [[-i[0],i[1]] for i in self.verts]


    def mirror_y(self):
        """Mirror across the y axis"""
        self.verts = [[i[0],-i[1]] for i in self.verts]

    
    def simple(self):
        """Check if the polygon is simple"""
        print("method is not reliable")
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