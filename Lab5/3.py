#Program to find sequences of lowercase letters joined with a underscore

import re

pattern = r'[a-z]+_[a-z]+'
txt = input()

for i in re.finditer(pattern, txt):
    print(i[0])