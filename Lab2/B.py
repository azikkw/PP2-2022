#Problem B

n = int(input())
a = list(map(int, input().split()))

b = a[0]
c = a[1]

for i in range(0, n):
    for j in range(i + 1, n):
        if a[i] * a[j] > b * c:
            b = a[i]
            c = a[j]
            
print(b * c)