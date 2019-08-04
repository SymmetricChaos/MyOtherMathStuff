import numpy as np

def rotate(P,th):
    assert type(P) == np.ndarray
    M = np.array([[np.cos(th),np.sin(th)],[-np.sin(th),np.cos(th)]])
    return np.matmul(P,M)

def reflect_y(P):
    assert type(P) == np.ndarray
    M = np.array([[-1,0],[0,1]])
    return np.matmul(P,M)

def reflect_x(P):
    assert type(P) == np.ndarray
    M = np.array([[0,-1],[1,0]])
    return np.matmul(P,M)


def shear(P,x=0,y=0):
    assert type(P) == np.ndarray
    M = np.array([[1,y],[x,1]])
    return np.matmul(P,M)