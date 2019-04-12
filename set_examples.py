#!/usr/bin/env python

tingyu_countries = [
    "China", "Japan", "France", "Germany", "Italy"
]

john_countries = [
    'Spain', 'Israel', 'China', 'UK', 'France'
]

tingyu = set(tingyu_countries)
john = set(john_countries)

print("both:", tingyu & john)
print("just one:", tingyu ^ john)
print("either:", tingyu | john)
print("just tingyu:", tingyu - john)
print("just john:", john - tingyu)
