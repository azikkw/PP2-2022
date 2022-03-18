from math import tan, pi

#Calculate the area of regular polygon

def AreaPol(n, a):
    S = (n * pow(a, 2)) / (4 * tan(pi / n))
    return S

print(AreaPol(4, 25))