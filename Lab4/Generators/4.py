#Generator called squares to yield the square of all numbers from (a) to (b)

def SquareNumbers(a, b):
    for i in range(a, b):
        i = i ** 2
        yield i
        

a, b = map(int, input().split())

numb = SquareNumbers(a, b)

for numbers in numb:
    print(numbers)