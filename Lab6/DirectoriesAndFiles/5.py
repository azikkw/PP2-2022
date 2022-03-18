#Program to write a list to a file

list_for_write = ['red', 'blue', 'black', 'yellow', 'orange']

with open('F:\Study\Labs\Lab6\DirectoriesAndFiles\ForExamples\Ex5.txt', 'a') as file:
    for add in list_for_write:
        file.write(f'{add}\n')