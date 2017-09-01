# This program contains functions that evaluate formulas used in geometry.
#
# Gavin Bernard
# August 22, 2014

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

print("")

def area_parralelo(h,w):
    return h * w

def trapezoid(b1,b2,h):
    return (1/2) * (b1+b2) * h

def rect_prism(b,h,w):
    return b * h * w

def cone(r,h):
    return math.pi * (r*r) * (h/3)

def sphere(r):
    return(4/3) * math.pi * (r*r*r)

def rect_prism2(b,h,w):
    return (b*w) + (h*w) + (b*w)

def sphere2(r):
    return 4 * math.pi * (r*r)

def hypotenuse(h,w):
    c = h*h + w*w
    return math.sqrt(c)

def heron(a,b,c):
    s = (a + b + c)/2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

print(heron(5,10,15))
print(heron(3,8,12))

#Attempting to obtain the area of a triangle with those inputs results in an error or 0.
#It is impossible for a triangle to have those lengths.
