import numpy as np

def lineside(A,B,P):
    d = ( (P[0]-A[0])*(B[1]-A[1]) ) - ( (P[1]-A[1])*(B[0]-A[0]) )
    if d > 0:
        return True
    return False

def convex_hull(polygon):
    
    V = polygon.verts
    
    # Find the leftmost point and start from there
    xs = [i[0] for i in V]
    cur = V[np.argmin(xs)]
    
    # Keep track of positions
    P = []
    while True:
        # Put the current point on the list
        P.append(cur)
        end = V[0]
        
        # Any point could be next so we check that by going through them one
        # by one. If that point is to the left of the line (as seen from the
        # current point) then our current guess is wrong so we make that point
        # the next point and continue.
        for j in range(len(V)):
            
            if cur == end or lineside(cur,end,V[j]):
                end = V[j]
                
        # Once that is done we have our new current point
        cur = end
        
        
        # Check if we've reached the place where we started
        if end == P[0]:
            P.append(cur)
            break

    
    return P