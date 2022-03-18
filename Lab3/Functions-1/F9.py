from cmath import pi


#Find volume of a sphere

def sphere(r, s):
    if r == 0 and s != 0:
        r = (s / 4 * pi) ** 0.5
        v = (4 * pi * (r ** 2)) / 3
        print(v)
    elif r == 0 and s == 0:
        print("Sorry, it is impossible")
    else:
        v = (4 * pi * (r ** 2)) / 3
        print(v)
    
r, s = map(float, input().split())

sphere(r, s)