#!/usr/bin/env python3

from vector_drawing import *
import math

def add(*vectors: list):
    v1 = sum([v[0] for v in vectors])
    v2 = sum([v[1] for v in vectors])
    return (v1, v2)

def length(v):
    return sqrt(v[0]**2 + v[1]**2)

def translate(translation: tuple, vectors: list):
    return [add(translation, v) for v in vectors]

#2.9
#v is blue, w is green
def ex29():
    draw(
        Points((2, 3), (-3, -1), add((2, 3), (-3, -1))),
        Arrow((2, 3), (0, 0), color=blue),
        Arrow(add((2, 3), (-3, -1)), (2, 3), color=green),
        Arrow((-3, -1), color=green),
        Arrow(add((2, 3), (-3, -1)), (-3, -1), color=blue)
    )


dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

def hundred_dinos():

    new_dinos = [Polygon(*translate((x*3, x*3), dino_vectors)) for x in 
                range(0, 101)]
    draw(*new_dinos)

def ex216():
    vector = (sqrt(2)*math.pi, sqrt(3)*math.pi)
    print(vector)
    draw(Arrow(vector, color=red),
         Arrow((sqrt(2), sqrt(3)), color=blue))

def scale(s, v):
    return (v[0]*s, v[1]*s)

def ex219():
    summed = []
    u = (-1, 1)
    v = (1, 1)
    u_list = [scale(r, u) for r in range(-3, 4)]
    v_list = [scale(s, v) for s in range(-1, 2)]
    print(u_list)
    print(v_list)
    for x in u_list:
        for y in v_list:
            summed.append(add(x, y))
    draw(Points(*summed)
         )
    return summed

def subtract(v1, v2):
    return add(v1, tuple(-x for x in v2))

def distance(v1, v2):
    return length(subtract(v1, v2))

def perimeter(vectors):
    distances = [distance(vectors[i], vectors[(i+1)%len(vectors)])
                 for i in range(0,len(vectors))]
    return sum(distances)

from math import tan, pi, sin, cos, atan2

def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return (length*cos(angle), length*sin(angle))

def to_polar(vector):
    x, y = vector[0], vector[1]
    angle = atan2(y, x)
    return (length(vector), angle)

def ex235():
    print(f"Radians: {116.57*(pi/180)}")
    print(tan(116.57*(pi/180)))

def ex237():
    polar = [(cos(5*x*pi/500.0), 2*pi*x/1000.0) for x in range(0,1000)]
    vectors = [to_cartesian(point) for point in polar]
    draw(Polygon(*vectors))

rotation_angle = pi/4
dino_polar = [to_polar(v) for v in dino_vectors]
dino_rotated_polar = [(l, angle + rotation_angle) for l,angle in dino_polar]
dino_rotated = [to_cartesian(p) for p in dino_rotated_polar]

def p68():
    draw(Polygon(*dino_vectors, color=gray),
    Polygon(*dino_rotated, color=red))

def rotate(angle, vectors):
    polars = [to_polar(v) for v in vectors]
    return [to_cartesian((l, a+angle)) for l,a in polars]

new_dino = translate((8,8), rotate(5 * pi/3, dino_vectors))

def p70():
    draw(Polygon(*dino_vectors, color=gray),
    Polygon(*new_dino, color=red))

def regular_polygon(n):
    return[to_cartesian((1, 2*pi*k/n)) for k in range (0,n)]