#!/usr/bin/env python
from copy import deepcopy

person = 'Bill', 'Gates', 'Microsoft', '62'
print(person[0], person[1])
# print(person.count('Gates'))

stuff = ['a', 'b', 'c'], 'x', 'y'

stuff[0].append(5)
print(stuff)

colors = ['red', 'green', 'blue']
c2 = colors  # DOES NOT MAKE A COPY!
c2.append('brown')
print(colors)
print(colors is c2)
c3 = colors[::] # MAKES A COPY
c4 = list(colors) # MAKES A COPY
print(colors is c3)
print(colors is c4, '\n')
c5 = deepcopy(colors)
x1 = 5,
x2 = '',
x3 = x2
x4 = tuple(x2)
for t in x1, x2, x3, x4:
    print(t, id(t))

person = 'Bill', 'Gates', 'Microsoft', '62'

first_name, last_name, product, age = person

x, y, z = 'Bob'
print(x, y, z, '\n')

values = 'a', 'b', 'c', 'd', 'e', 'f'

x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)

x = 5
y = 10
x, y = y, x
print(x, y)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'Next', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
]

print(type(people))
print(type(people[0]))
print(type(people[0][0]))
print(type(people[0][0][0]))

for first_name, last_name, *_, dob in people:
    print(first_name, last_name, dob)
print('-' * 60)

x = [
    (5,),
    (6,),
    (7,),
    (8,),
]
print(x)
print(x[0])

for thing, in x:
    print(thing)

print(len(people))
print(min(people))
print(max(people))
print(sorted(people))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
print(sorted(nums))
print(list(reversed(nums)))
print(sorted(nums, reverse=True))
print(min(nums), max(nums), sum(nums))
print()

print(colors)
for i, color in enumerate(colors):
    print(i, color)
print()

for i, color in enumerate(colors, 1):
    print(i, color)
print()

a1 = ['wombat', 'KOALA', 'wallaby']
a2 = ['Wombat', 'koala', 'platypus']

print(a1[0].lower() == a2[0].lower())
print()

print(all(x.lower() == y.lower() for x, y in zip(a1, a2)))

print(any(x.lower() == y.lower() for x, y in zip(a1, a2)))

print([x.lower() == y.lower() for x, y in zip(a1, a2)])

w = "Wombat"
print(w * 10)

flags = [True] * 10
print(flags)
print(True * 10)

print(['a', 'b', 'c'] * 5)
