#Program to check for access to a specified path

import os

path = 'F:\Study\Labs\Lab6\DirectoriesAndFiles\Directory\Dir2\Dir2_1\Dir2_1_1'

if os.path.exists(path):
    print(f'\nYES, YOU HAVE ACCESS TO THIS PASS')
    
    for target in os.listdir(path):
        target_path = os.path.join(path, target)
        
        if os.path.isfile(target_path):
            print(f'FILE NAME: {target}')
            
        print(f'DIRECTORY PORTION: {path}\n')