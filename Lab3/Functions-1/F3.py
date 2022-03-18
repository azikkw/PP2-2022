#Сounting chickens and hares

def solve(numheads, numlegs, h, l):
    for i in range(0, a):
        for j in range(0, b):
            if (i * 2) + (j * 4) == b and i + j == a:
                h = i
                l = j
    
    print(h, l)

a, b = map(int, input().split())
h, l = 0, 0

solve(a, b, h, l)