from teapot import *
from vectors import *
from draw_model import *

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

draw_model(polygon_map(scale_then_translate, original_triangles))


