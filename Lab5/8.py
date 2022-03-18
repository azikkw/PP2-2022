#Program to split a string at uppercase letters

import re

pattern = r'[A-Z]'
txt = 'HELLO WHORLD'

txt_update1 = re.findall(pattern, txt)
print(txt_update1)

txt_update2 = re.split("([A-Z][^A-Z]*)", txt)
print(txt_update2)