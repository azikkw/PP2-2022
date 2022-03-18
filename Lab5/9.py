#Program to split a string at uppercase letters

import re

txt = 'HelloWorldMeAzat'

txt_update = re.sub(r"(\w)([A-Z])", r"\1 \2", txt)
print(txt_update)