#Program to list only directories, files and all directories, files in a specified path

import os

def add_space(space):
    for i in range(space):
        print('', end = ' ')

def show(path, space):
    for target in os.listdir(path):
        target_path = os.path.join(path, target)
        
        if os.path.isfile(target_path):
            add_space(space)
            print(f'FILE: {target_path}')
        else:
            add_space(space)
            print(f'DIR: {target_path}')
            show(target_path, space + 1)
            
            
path = 'F:\Study\Labs\Lab6\DirectoriesAndFiles\Directory'

show(path, 0)