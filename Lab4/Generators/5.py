#Generator that returns all numbers from (n) down to 0

def ReverseNumber(n):
    for i in range(n, 0, -1):
        yield i


n = int(input())

numb = ReverseNumber(n)

for numbers in numb:
    print(numbers, end=" ")