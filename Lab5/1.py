#'a' followed by {0, ...} 'b'

import re

pattern = r'[a]{1}\w{0,}'
txt = input()

print(re.findall(pattern, txt))