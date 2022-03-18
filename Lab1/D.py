#Problem D

n = int(input())
s = input()

if s == "k":
    t = int(input())
    k = n / 1024
    k = round(k, t)
    print(k)

if s == "b":
    n = n * 1024
    print(n)
