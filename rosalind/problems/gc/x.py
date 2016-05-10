#!/usr/bin/python
# URL that generated this code:
# http://www.txt2re.com/index-python.php3?s=%3ERosalind_8362&-22&1

import re

txt='xRosalind_8362'

re1='(>)'	# Any Single Character 1
re2='((?:[a-z][a-z0-9_]*))'	# Variable Name 1

rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    c1=m.group(1)
    var1=m.group(2)
    print "("+c1+")"+"("+var1+")"+"\n"