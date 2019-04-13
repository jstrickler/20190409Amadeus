#!/usr/bin/env python

import requests

response = requests.get(
    "https://amadeus.com",
    # proxy={},
    # auth=('name', 'secret'),
    # headers={'header_name': 'header_value'},
    # data={'k':'v'},
    # params={'k': 'v'},

)  # <1>

for header, value in sorted(response.headers.items()): # <2>
    print(header, value)
print()

print(response.content[:200].decode())   # <3>
print('...')
print(response.content[-200:].decode())   # <4>
