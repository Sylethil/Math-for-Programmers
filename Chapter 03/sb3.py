from draw3d import *

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
    
def add(*vectors):
    by_coordinate = zip(*vectors)
    coordinate_sums = [sum(coords) for coords in by_coordinate]
    return tuple(coordinate_sums)


