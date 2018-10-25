#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math

def bisection(function,a , b): 
    start = a
    end = b
    if function(a) == 0:
        return a
    elif function(b) == 0:
        return b
    elif function(a) * function(b) > 0:
        print("couldn't find root in [a,b]")
        return
    else:
        mid = (start + end) /2
