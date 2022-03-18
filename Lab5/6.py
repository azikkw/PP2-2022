#Program to replace all occurrences of space, comma, or dot with a colon

import re

txt = input()

txt_update = re.sub("[ ]", ",", txt)
print(re.sub("[.]", ":", txt_update))