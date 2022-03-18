#Program to delete file by specified path

import os

path = 'F:\Study\Labs\Lab6\DirectoriesAndFiles\ForExamples\ForExample8\Ex8'

if os.path.exists(path):
    os.remove(path)
    print('File have deleted!')
else:
    print('No such file in directory!')