from teapot import *
from vectors import *
from draw_model import *


def scale2(v):
    return scale(2.0, v)

original_triangles = load_triangles()

def translate1left(v):
    return add((-1,0,0), v)

def compose(f1, f2):
    def new_function(input):
        return f1(f2(input))
    return new_function

scale_then_translate = compose(translate1left, scale2)

scaled_translated_triangles = [
    [scale_then_translate(vertex) for vertex in triangle]
    for triangle in original_triangles
]

draw_model(scaled_translated_triangles)

