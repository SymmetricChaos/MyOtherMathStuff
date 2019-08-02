import numpy as np
import matplotlib.pyplot as plt

class Circle:
    def __init__(self,r,pos=[0,0]):
        self.r = r
        self.cur = 1/r
        self.area = r*r*np.pi
        self.pos = pos
    
    def draw(self,color="black"):
        ax = plt.gca()
        circ = plt.Circle(self.pos,radius = self.r, fc = "#00000000", ec = color)
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

    def draw(self,color="black"):
        ax = plt.gca()
        circ = plt.Ellipse(self.pos, width = self.a, height = self.b, fc = "#00000000", ec = color)
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
        

#e = Ellipse(3,1)
#print(e.ecc)
#print(e.focal_dist)
#
#c = Circle(3)
#x = c.points_x()
#y = c.points_y()
#plt.scatter(x,y)
        
#e = Ellipse(3,1)
#x = e.points_x()
#y = e.points_y()
#plt.scatter(x,y)