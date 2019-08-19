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
