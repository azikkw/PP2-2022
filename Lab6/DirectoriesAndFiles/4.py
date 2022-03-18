#Program to count the number of lines in a text file

with open('F:\Study\Labs\Lab6\DirectoriesAndFiles\ForExamples\Ex4.txt', 'r') as file:
    lines = len(file.readlines())
    
print(lines)