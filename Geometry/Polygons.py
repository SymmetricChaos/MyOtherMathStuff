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
        for i in verts:
            assert len(i) == 2
        self.verts = verts


    def draw(self,facecolor="#00000000",edgecolor="black",**kwargs):
        ax = plt.gca()
        poly = plt.Polygon(self.verts,facecolor=facecolor,edgecolor=edgecolor,**kwargs)
        ax.add_patch(poly)


    def draw_points(self,color="black",**kwargs):
        ax = plt.gca()
        scatter_points(self.verts,color=color,**kwargs)


    def copy(self):
        """Create an identical Polygon"""
        return Polygon(self.verts[:])


    def _area(self):
        """Calculate area"""
        return abs(self.signed_area)
    
    
    # Needs to check for self intersection
    def _signed_area(self):
        """Calculate signed area"""
        area = 0
        X = self.x
        Y = self.y
        X += [X[0]]
        Y += [Y[0]]
        for i in range(len(X)-1):
            area += X[i]*Y[i+1] - X[i+1]*Y[i]
        return area/2


    def _x(self):
        """x-coordinates of the vertices"""
        return [i[0] for i in self.verts]


    def _y(self):
        """y-coordinates of the vertices"""
        return [i[1] for i in self.verts]


    # Simpler and quicker than calculating the centroid but less
    # meaningful mathematically
    def _center(self):
        """Return arithmetic mean of the vertices"""
        return [ np.mean(self.x), np.mean(self.y)]


    def _centroid(self):
        """Return centroid of the polygon"""
        x = 0
        y = 0
        A = self.signed_area
        X = self.x
        Y = self.y
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
        x,y = self.centroid
        self.verts = [[i[0]-x,i[1]-y] for i in self.verts]


    def shift(self,x=0,y=0):
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
        x,y = self.center
        self.shift_center()
        self.rotate(th)
        self.shift(x,y)
        
        
    def rotate_centroid(self,th=0):
        """Rotate by full-turns around the centroid of the polygon"""
        x,y = self.centroid
        self.shift_centroid()
        self.rotate(th)
        self.shift(x,y)


    def mirror(self,axis):
        """Mirror across an axis"""
        if axis == "x" or axis == "X":
            self.verts = [[-i[0],i[1]] for i in self.verts]
        elif axis == "y" or axis == "Y":
            self.verts = [[i[0],-i[1]] for i in self.verts]
        else:
            raise ValueError("Axis must be x or y")


    def mirror_center(self,axis):
        """Mirror across center"""
        x,y = self.center
        self.shift_center()
        self.mirror(axis)
        self.shift(x,y)


    def mirror_centroid(self,axis):
        """Mirror across centroid"""
        x,y = self.centroid
        self.shift_centroid()
        self.mirror(axis)
        self.shift(x,y)
        
            
    def simple(self):
        """Check if the polygon is simple"""
        print("method is not reliable")
        return not check_self_intersect(self)


    # Properties to make access more intuitive
    area = property(_area)
    signed_area = property(_signed_area)
    center = property(_center)
    centroid = property(_centroid)
    x = property(_x)
    y = property(_y)
    


class PolygonSet:
    def __init__(self,polygons):
        assert type(polygons) == list
        for i in polygons:
            assert type(i) == Polygon
        self.polygons = [p.copy() for p in polygons]


    def __getitem__(self,n):
        return self.polygons[n]


    def draw(self,facecolor="#00000000",edgecolor="black",**kwargs):
        for poly in self.polygons:
            poly.draw(facecolor=facecolor,edgecolor=edgecolor,**kwargs)


    def draw_points(self,color="black",**kwargs):
        for poly in self.polygons:
            poly.draw_points(color,**kwargs)


    def shift(self,x=0,y=0):
        """Shift all polygons in the set"""
        for poly in self.polygons:
            poly.shift(x,y)


    # This doesn't actually calculate the centroid of the set like I thought
    def _centroid(self):
        """Centroid of the set"""
        x,y = 0,0
        for poly in self.polygons:
            xp,yp = poly.centroid
            x += xp
            y += yp
        return [x/len(self.polygons),y/len(self.polygons)]


    def _center(self):
        """Center of the set"""
        X,Y = [],[]
        for poly in self.polygons:
            x,y = poly.x, poly.y
            X += x
            Y += y
        return [np.mean(X), np.mean(Y)]


    def shift_center(self):
        """Put center of the set at the origin"""
        x,y = self.center
        for poly in self.polygons:
            poly.shift(-x,-y)


    def shift_centroid(self):
        """Put centroid of the set at the origin"""
        x,y = self.centroid
        for poly in self.polygons:
            poly.shift(-x,-y)


    def rotate(self,th):
        """Rotate the set around the origin"""
        for poly in self.polygons:
            poly.rotate(th)
            

    def rotate_center(self,th=0):
        """Rotate by full-turns around the center of the set"""
        x,y = self.center
        self.shift_center()
        self.rotate(th)
        self.shift(x,y)
        
        
    def rotate_centroid(self,th=0):
        """Rotate by full-turns around the centroid of the set"""
        x,y = self.centroid
        self.shift_centroid()
        self.rotate(th)
        self.shift(x,y)


    # Properties to make access more intuitive
    center = property(_center)
    centroid = property(_centroid)



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


# This function is not reliable
# It detects intersections that don't exist
#   Known case: some rotations of a simple polygon appear as self intersecting
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