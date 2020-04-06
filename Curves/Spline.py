import matplotlib.pyplot as plt
import numpy as np


def spline(parts,polys):
    
    end_points = []
    for lo,hi in zip(parts[:-1],parts[1:]):
        if lo >= hi:
            raise Exception("List of parts must be strictly increases")
        else:
            end_points.append((lo,hi))
            
    
    print(end_points)






if __name__ == '__main__':
    spline([0,.5,1,2,2.3],0)