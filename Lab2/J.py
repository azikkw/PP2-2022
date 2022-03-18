#Problem J

n = int(input())
k = []

for i in range(n):
    t = input()
    if t >= 'A' and t <= 'Z':
        k.append(t)
    elif t >= '0' and t <= '9':
        k.append(t)
    elif t >= 'a' and t <= 'z':
        k.append(t)

print(*k)