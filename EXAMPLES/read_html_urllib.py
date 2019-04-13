#!/usr/bin/env python

import urllib.request

u = urllib.request.urlopen("https://amadeus.com")

print(u.info())  # <1>
print()

print(u.read(5000).decode())   # <2>
