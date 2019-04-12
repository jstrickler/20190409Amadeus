#!/usr/bin/env python
from sample_class import Foo

f = Foo()

f.blech(1, 2)

print(f.__doc__)
print(f.blech.__doc__)
