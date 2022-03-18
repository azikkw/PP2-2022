#Problem E

a, b = map(int, input().split())
prime = True

if a > 1:
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            prime = False
            break

if a < 500 and b % 2 == 0 and prime:
    print("Good job!")
else:
    print("Try next time!")