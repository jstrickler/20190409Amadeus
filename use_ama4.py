#!/usr/bin/env python
import sys
from amadeus.misc.amautil import *  # import all unless _*

spam()
ham()

for path in sys.path:
    print(path)
