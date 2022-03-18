#Generator to print the even numbers between 0 and n

def EvenNumber(n):
    for i in range(2, n):
        if i % 2 == 0:
            yield i


n = int(input())
a = []

numb = EvenNumber(n)

for numbers in numb:
    a.append(numbers)
    
print(a)