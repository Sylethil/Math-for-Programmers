from draw3d import *
from math import *
import numpy as np

def ex3_2():
    vectors = [(x,y,z) for x in [-1, 1] for y in [-1, 1] for z in [-1, 1]]
    segments = [(vector1, vector2) for vector1 in vectors for vector2 in
                vectors if (vector1 < vector2) 
                and ((vector1[0] == vector2[0] and vector1[1] == vector2[1]) 
                or (vector1[1] == vector2[1] and vector1[2] == vector2[2]) 
                or (vector1[0] == vector2[0] and vector1[2] == vector2[2])
                )]
    draw3d(Points3D(*vectors),
           *[Segment3D(*segment) for segment in segments])
    
def add(vectors):
    return tuple(sum(vector[i] for vector in vectors) for i in range(3))

def their_add(vectors):
    by_coordinate = zip(*vectors)
    coordinate_sums = [sum(coords) for coords in by_coordinate]
    return tuple(coordinate_sums)

def length(v):
    return sqrt(sum(coord ** 2 for coord in v))

def ex3_3(vectors):
    print(f"Vector sum: {add(vectors)}")
    draw3d(Arrow3D(vectors[0]),
           Arrow3D(vectors[1]),
           Arrow3D(add(vectors), vectors[1]),
           Arrow3D(add(vectors), vectors[0]),
           Arrow3D(add(vectors)))

def ex3_5():
    vs = [(sin(pi*t/6), cos(pi*t/6), 1.0/3) for t in range(0,24)]
    print(f"Sum: {add(vs)}")
    running_sum = (0,0,0) #<1>
    arrows = []
    for v in vs:
        next_sum = add([running_sum, v]) #2
        arrows.append(Arrow3D(next_sum, running_sum)) 
        running_sum = next_sum
    print(running_sum)
    draw3d(*arrows)

def scale(scalar, vector):
    return tuple([scalar*v for v in vector])

def ex3_9():
    x, y, z = 0, 0, 0
    while True:
        vector = (x, y, z)
        current_length = length(vector)

        if current_length.is_integer():
           print(f"Found solution: {vector} with length {current_length}")
        
        x += 1

        vector = (x, y, z)  # Need to update vector after changing x
        current_length = length(vector)  # Need to recalculate length

        if current_length.is_integer():
           print(f"Found solution: {vector} with length {current_length}")

        y += 1

        vector = (x, y, z)  # Need to update vector after changing x
        current_length = length(vector)  # Need to recalculate length

        if current_length.is_integer():
            print(f"Found solution: {vector} with length {current_length}")

        z += 1

        if z == 1000:
            break

    return None

def ex3_10():
    vector = (-1,-1,2)
    s = 1/length(vector)
    print(scale(s, vector))
    print(length(scale(s,vector)))