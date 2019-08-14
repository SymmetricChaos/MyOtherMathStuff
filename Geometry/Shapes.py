import numpy as np
import matplotlib.pyplot as plt

class Circle:
    def __init__(self,r,pos=[0,0]):
        self.r = r
        self.cur = 1/r
        self.area = r*r*np.pi
        self.pos = pos
    
    def draw(self,facecolor="white",edgecolor="black",linewidth=1,linestyle="-"):
        ax = plt.gca()
        circ = plt.Circle(self.pos,radius = self.r,
                          edgecolor = edgecolor, facecolor = facecolor,
                          linewidth = linewidth, linestyle = linestyle)
        ax.add_patch(circ)
        
    def points(self,n=100):
        th = np.linspace(0,2*np.pi,n)
        return [[x*self.r,y*self.r] for x,y in zip(np.sin(th),np.cos(th))]
      
    def points_x(self,n=100):
        th = np.linspace(0,2*np.pi,n)
        return np.sin(th)*self.r
    
    def points_y(self,n=100):
        th = np.linspace(0,2*np.pi,n)
        return np.cos(th)*self.r
           
        
class Ellipse:
    def __init__(self,a,b,pos=[0,0]):
        # Silently orient the ellipse so that a is always the semimajor axis
        if b > a:
            a,b = b,a
        self.a = a
        self.b = b
        self.area = np.pi*a*b
        self.ecc = np.sqrt(1-((b*b)/(a*a)))
        self.focal_dist = self.ecc*a

    def draw(self,facecolor="white",edgecolor="black",linewidth=1,linestyle="-"):
        ax = plt.gca()
        circ = plt.Ellipse(self.pos, width = self.a, height = self.b,
                          edgecolor = edgecolor, facecolor = facecolor,
                          linewidth = linewidth, linestyle = linestyle)
        ax.add_patch(circ)

    def points(self,n=100):
        th = np.linspace(0,2*np.pi,n)
        return [[x*self.a,y*self.b] for x,y in zip(np.sin(th),np.cos(th))]
      
    def points_x(self,n=100):
        th = np.linspace(0,2*np.pi,n)
        return np.sin(th)*self.a
    
    def points_y(self,n=100):
        th = np.linspace(0,2*np.pi,n)
        return np.cos(th)*self.b
        
    def foci(self):
        return [[-self.focal_dist,0],[self.focal_dist,0]]


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
        area = 0
        for i in range(len(self.verts)-1):
            area += self.verts[i][0]*self.verts[i+1][1] - self.verts[i+1][0]*self.verts[i][1]
        return area/2
    
    def verts_x(self):
        return [i[0] for i in self.verts]
    
    def verts_y(self):
        return [i[1] for i in self.verts]

#def star_polygon(p,q):