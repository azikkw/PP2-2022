#Uppercase letter followed by lower case letters

import re

pattern = r'\b\w{0,}[a]{1}\w{0,}[b]{1}\b'
txt = input()

print(re.findall(pattern, txt))