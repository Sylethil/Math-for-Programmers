#!/usr/bin/env python3

from vector_drawing import *

def add(*vectors: list):
    v1 = sum([v[0] for v in vectors])
    v2 = sum([v[1] for v in vectors])
    return (v1, v2)

from math import sqrt
def length(v):
    return sqrt(v[0]**2 + v[1]**2)

def translate(translation: tuple, vectors: list):
    return [add(translation, v) for v in vectors]
print(translate((1,1), [(0,0), (0,1), (-3,-3)]))