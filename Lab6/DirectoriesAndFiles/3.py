#Program to test whether a given path exists or not

import os

path = 'F:\Study\Labs\Lab6\DirectoriesAndFiles\Directory\Dir3'

if os.path.exists(path):
    for target in os.listdir(path):
        target_path = os.path.join(path, target)
        
        if os.path.isfile(target_path):
            print(f'FILE NAME: {target}')
            
        print(f'DIRECTORY PORTION: {path}')