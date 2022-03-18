import math

#Calculate the area of a trapezoid

def Trapezoid(a, b, h):
    s = 0.5 * (a + b) * h
    return s

print(Trapezoid(5, 6, 5))