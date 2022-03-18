#Program to convert a given snake case string to camel case

import re

txt = 'java_script_coding_first_lesson'
txt_update1 = re.split('_', txt)

txt_update2 = txt_update1[0] + ''.join(i.title() for i in txt_update1[1:])

print(txt_update2)