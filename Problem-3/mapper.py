#!/usr/bin/env python
"""mapper.py"""

import sys

for i in sys.stdin:
    
    i = i.strip()
    word = i.split(", ")
    word[0] = word[0].strip("[")
    word[0] = word[0].strip("\"")
    print '%s\t%s' % (word[0], 1)
