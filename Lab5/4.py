#Uppercase letter followed by lower case letters

import re

pattern = r'\b[A-Z]{1}[a-z]{0,}\b'
txt = input()

print(re.findall(pattern, txt))