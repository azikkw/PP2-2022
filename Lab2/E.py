#Problem E

n, x = map(int, input().split())
k = 0

for i in range(n):
    i = x + 2 * i
    k ^= i

print(k)