#'a' followed by 2 or 3 'b'

import re

pattern = r'[a]{1}\w{2,3}'
txt = input()

print(re.findall(pattern, txt))

for i in re.finditer(pattern, txt):
    print(i[0])