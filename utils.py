import math
import numpy as np

def rad_to_unitvec(radians):
    x = math.cos(radians)
    y = math.sin(radians)
    return np.array([x, y])

def unitvec_to_rad(unitvec):
    return math.atan2(unitvec[1], unitvec[0])

def unit_vector(vector):
    norm = np.linalg.norm(vector)
    if norm == 0: 
        return 0
    return vector / norm

def avg(x):
    if len(x) == 0:
        return 0
    
    avg = [0,0]
    for i in range(0, len(x)):
        avg[0]+= x[i][0]
        avg[1]+= x[i][1]

    avg[0] = avg[0]/len(x)
    avg[1] = avg[1]/len(x)

    return avg