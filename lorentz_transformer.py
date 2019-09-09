import math
import time

c = 3e8

start = time.time()

def t():
    return time.time() - start

def transform(rect, v, t):
    x, y, w, h = rect
    return [x, y, x_(w, v, t), h]

def gamma(v):
    return 1 / math.sqrt(1 - v**2 / c ** 2)

def x_(x, v, t):
    return gamma(v) * x #(x - v * t)

def t_(x, v, t):
    return gamma(v) * (t - v * x / c ** 2)