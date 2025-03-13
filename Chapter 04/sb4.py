from teapot import *
from vectors import *
from draw_model import *
from math import *

original_triangles = load_triangles()

def scale_by(scalar):
    def new_function(v):
        return scale(scalar, v)
    return new_function

def translate_by(vector):
    def new_function(v):
        return add(vector, v)
    return new_function

def compose(f1, f2):
    def new_function(input):
        return f1(f2(input))
    return new_function

scale_then_translate = compose(translate_by((-1,0,0)), scale_by(2))

def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]

def rotate2d(angle, vector):
    l, a = to_polar(vector)
    return to_cartesian((l, a+angle))

def rotate_z(angle, vector):
    x,y,z = vector
    new_x, new_y = rotate2d(angle, (x,y))
    return new_x, new_y, z

def rotate_z_by(angle):
    def new_function(v):
        return rotate_z(angle, v)
    return new_function

def rotate_x(angle, vector):
    x,y,z = vector
    new_y, new_z = rotate2d(angle, (y,z))
    return x, new_y, new_z

def rotate_x_by(angle):
    def new_function(v):
        return rotate_x(angle,v)
    return new_function




