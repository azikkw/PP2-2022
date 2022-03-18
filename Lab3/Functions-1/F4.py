#Find Prime Number

def filter_prime(a, n):
    for i in range(2, n + 1):
        k = 0
        for j in a:
            if i % j == 0:
                k = 1
        if k == 0:
            a.append(i)
            
    print(a)
    print(len(a))

a = []    
n = int(input())

filter_prime(a, n)