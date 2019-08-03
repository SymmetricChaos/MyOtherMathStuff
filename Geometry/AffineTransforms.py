import numpy as np

def rot_mat(th):
    return np.array([[np.cos(th),np.sin(th)],[-np.sin(th),np.cos(th)]])


def rotate(P,th):
    assert type(P) == np.ndarray
    return np.matmul(P,rot_mat(th))