#Program to copy the contents of a file to another file

file = open('F:\Study\Labs\Lab6\DirectoriesAndFiles\ForExamples\Ex4.txt', 'r')
text = file.read()

file.close()
   
with open('F:\Study\Labs\Lab6\DirectoriesAndFiles\ForExamples\Ex5.txt', 'a') as file:
    file.write(f'\n\n{text}')