#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math

def intersection(funcion ,x0, x1):
    x_n = x0
    x_n1 = x1
    while True:
        x_n2 = x_n1-(function(x_n1) / ((function(x_n1)-function(x_n)) / (x_n1-x_n)))
        if abs(x_n2 - x_n1) < 0.0001 :
            return x_n2
        x_n = x_n1
        x_n1 = x_n2

def f(x):
    return math.pow(x, 3) - 2 * x - 5

print(intersection(f, 3, 3.5))

