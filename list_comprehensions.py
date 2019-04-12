#!/usr/bin/env python
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

#  NEW_LIST = [EXPRESSION for VAR ... in ITERABLE if CONDITION ...]
f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

f3 = [f for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

f4 = [(f.capitalize(), len(f)) for f in fruits]
print("f4: {}\n".format(f4))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print("last_names: {}\n".format(last_names))

print(enumerate(fruits))
print(reversed(fruits))

e = enumerate(fruits)

for i, fruit in e:
    if i == 5:
        break
    print(i, fruit)
print()

for i, fruit in e:
    if i == 5:
        break
    print(i, fruit)
print()


for f in reversed(fruits):
    print(f)
print()

fgen = (f.upper() for f in fruits)
fruits.append('durian')

print("fgen: {}\n".format(fgen))
for fruit in fgen:
    print(fruit)
print()

a1 = ['wombat', 'KOALA', 'wallaby']
a2 = ['Wombat', 'koala', 'platypus']

z = zip(a1, a2)
print(z)
print(list(zip(a1, a2)))

bools = [x[0].lower() == y[0].lower() for x, y in z]
print(bools)
print(any(bools))
print(all(bools))


clean_fruits = [..... fruits]
print(clean_fruits)
