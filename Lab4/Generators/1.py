#Generate the squares of numbers up to some number N

class SquareNumber:
    
    def __iter__(self):
        self.x = 1
        return self
    
    def __next__(self):
        x = self.x
        self.x += 1
        return x
    
    
numb = SquareNumber()
n = int(input())

for i in numb:
    i = i ** 2
    if i < n:
        print(i, end=" ")
    else:
        break