#Generator which can iterate the numbers, which are divisible by 3 and 4

def DivBy(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            

n = int(input())
numb = DivBy(n)

for numbers in numb:
    print(numbers, end=" ")