#Program to convert a given camel case string to snake case

import re

txt = input()
txt_update = re.sub('(.)([A-Z][a-z]{1,})', r'\1_\2', txt).lower()

print(txt_update)