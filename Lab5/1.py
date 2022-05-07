#'a' followed by {0, ...} 'b'

import re

"""pattern = r'[a]{1}\w{0,}'
txt = input()

print(re.findall(pattern, txt))"""

#pattern = r'\W[+]{1}\d[7]{1}\W[(]\d{0,3}\W[)]\d{0,7}'
pattern = r'\d[7]'
#pattern = r'\d{0,11}'
txt = input()

print(re.findall(pattern, txt))
"""if re.findall(pattern, txt):
    print("yes")
else:
    print("no")"""