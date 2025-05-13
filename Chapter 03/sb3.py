from draw2d import *
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
        next_sum = add(running_sum, v) #2
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

def dot(u,v):
    return sum([coord1 * coord2 for coord1,coord2 in zip(u,v)])

def angle_between(v1,v2):
    return acos(
        dot(v1,v2) /
        (length(v1)) * (length(v2))
    )

octahedron = [
    [(1,0,0), (0,1,0), (0,0,1)],
    [(1,0,0), (0,0,-1), (0,1,0)],
    [(1,0,0), (0,0,1), (0,-1,0)],
    [(1,0,0), (0,-1,0), (0,0,-1)],
    [(-1,0,0), (0,0,1), (0,1,0)],
    [(-1,0,0), (0,1,0), (0,0,-1)],
    [(-1,0,0), (0,-1,0), (0,0,1)],
    [(-1,0,0), (0,0,-1), (0,-1,0)],
]

def vertices(faces):
    return list(set([vertex for face in faces for vertex in face]))

def component(v,direction):
    return (dot(v,direction) / length(direction))

def vector_to_2d(v):
    return (component(v,(1,0,0)), component(v,(0,1,0)))

def face_to_2d(face):
    return [vector_to_2d(vertex) for vertex in face]

blues = matplotlib.cm.get_cmap('Blues')

def unit(v):
    return scale(1./length(v), v)

def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

from vectors import *
from draw2d import *

def render(faces, light=(1,2,3), color_map=blues, lines=None):
    polygons = []
    for face in faces:
        unit_normal = unit(normal(face)) #1
        if unit_normal[2] > 0: #2
            c = color_map(1 - dot(unit(normal(face)), unit(light))) #3
            p = Polygon2D(*face_to_2d(face), fill=c, color=lines) #4
            polygons.append(p)
    draw2d(*polygons,axes=False, origin=False, grid=None)

def ex3_27():
    top = (0,0,1)
    bottom = (0,0,-1)
    xy_plane = [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0)]
    edges = [Segment3D(top,p) for p in xy_plane] +\
            [Segment3D(bottom, p) for p in xy_plane] +\
            [Segment3D(xy_plane[i],xy_plane[(i+1)%4 ]) for i in range(0,4)] 
    draw3d(*edges)

ex3_27()