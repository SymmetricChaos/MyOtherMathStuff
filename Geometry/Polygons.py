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
        scatter_points(self.verts,color=color,**kwargs)
        

    def copy(self):
        """Create an identical Polygon"""
        return Polygon(self.verts[:])


    def __str__(self):
        out = ""
        for v in self.verts:
            out += f"({round(v[0],2)} , {round(v[1],2)})\n"
        return out

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


    def shift_center(self,x=0,y=0):
        """Center the polygon using arithmetic mean of the vertices"""
        oldx,oldy = self.center
        self.verts = [[i[0]-oldx+x,i[1]-oldy+y] for i in self.verts]


    def shift_centroid(self,x=0,y=0):
        """Center the polygon using centroid"""
        oldx,oldy= self.centroid
        self.verts = [[i[0]-oldx+x,i[1]-oldy+y] for i in self.verts]


    def shift(self,x=0,y=0):
        """Shift position"""
        self.verts = [[i[0]+x,i[1]+y] for i in self.verts]


    def scale(self,s=1,pos=None):
        """Scale relative to the some point"""
        
        if pos:
            xold,yold = pos
        else:
            xold,yold = self.center
        
        self.shift(-xold,-yold)
        
        M = np.array([[s,0],[0,s]])
        self.verts = np.matmul(self.verts,M)
        
        self.shift(xold,yold)
        
        
    def rotate(self,th=0,pos=None):
        """Rotate by full-turns around some point"""
        
        if pos:
            xold,yold = pos
        else:
            xold,yold = self.center
        
        self.shift(-xold,-yold)
        
        th = np.pi*2*th
        M = np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
        self.verts = np.matmul(self.verts,M)
    
        self.shift(xold,yold)


    def mirror(self,axis,pos=None):
        """Mirror across an axis"""
        if pos:
            xold,yold = pos
        else:
            xold,yold = self.center
            
        self.shift(-xold,-yold)
        
        if axis in "Xx":
            self.verts = [[-i[0],i[1]] for i in self.verts]
        elif axis in "Yy":
            self.verts = [[i[0],-i[1]] for i in self.verts]
        else:
            raise ValueError("Axis must be x or y")
        
        self.shift(xold,yold)
        

    def stretch(self,x=1,y=1,pos=None):
        """Stretch relative to some point"""
        if pos:
            xold,yold = pos
        else:
            xold,yold = self.center

        self.shift(-xold,-yold)
        
        M = np.array([[x,0],[0,y]])
        self.verts = np.matmul(self.verts,M)
        
        self.shift(xold,yold)

            
    def affine(self,a,b,c,d):
        """Abitrary affine transformation relative to the origin"""
        M = np.array([[a,b],[c,d]])
        self.verts = np.matmul(self.verts,M)

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
    
    
    def __add__(self,other):
        assert type(other) == PolygonSet
        L = self.polygons + other.polygons
        return PolygonSet(L)
            

    def copy(self):
        return PolygonSet(self.polygons[:])


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


    def shift_center(self,x=0,y=0):
        """Put center of the set at a given point"""
        oldx,oldy = self.center
        for poly in self.polygons:
            poly.shift(-oldx+x,-oldy+y)


    def shift_centroid(self,x=0,y=0):
        """Put centroid of the set at a given point"""
        oldx,oldy = self.centroid
        for poly in self.polygons:
            poly.shift(-oldx+x,-oldy+y)


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
        
    def mirror(self,axis,pos=None):
        """Mirror across an axis"""
        if pos:
            xold,yold = pos
        else:
            xold,yold = self.center
            
        self.shift(-xold,-yold)
        
        if axis in "XxYy":
            for poly in self.polygons:
                poly.mirror(axis,pos=[xold,yold])
        else:
            raise ValueError("Axis must be x or y")
        
        self.shift(xold,yold)


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
    return Polygon(convex_hull(polygon)[:-1])


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