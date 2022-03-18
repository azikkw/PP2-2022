#Problem B

s = input()
k = 0

for i in s:
    k += ord(i)

if k > 300:
    print("It is tasty!")
else:
    print("Oh, no!")