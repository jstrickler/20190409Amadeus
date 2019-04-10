#!/usr/bin/env python

list1 = list()
# x = list(any-iterable)

list2 = ["red", 5, 8.9, None]

list3 = []

colors = 'red blue green purple'.split()

actors = ['Brad Pitt', 'Chris Hemsworth',
          'Angelina Jolie', 'Tom Hanks',
          'Humphrey Bogart']

actors.append('Jason Stathham')
print(actors, '\n')
actors.insert(0, 'Sean Connery')
print(actors, '\n')
actors.insert(5, 'Gal Gadot')
print(actors, '\n')

more_james_bonds = ['Roger Moore', 'Timothy Dalton', 'Pierce Brosnan', 'David Niven',
                    'Daniel Craig']

actors.extend(more_james_bonds)
print(actors, '\n')

del actors[8]
print(actors, '\n')

dc = actors.pop()
print(dc)
print(actors, '\n')

aj = actors.pop(3)
print(aj)
print(actors, '\n')

# x = actors.pop(99)
# print(x)
# print(actors, '\n')

actors.remove('Tom Hanks')

if 'Humphrey Bogart' in actors:
    print("Bogey!")


actors = ['Brad Pitt', 'Chris Hemsworth',
          'Angelina Jolie', 'Tom Hanks',
          'Humphrey Bogart']

actors.append('Jason Stathham')
print(actors, '\n')
actors.insert(0, 'Sean Connery')
print(actors, '\n')
actors.insert(5, 'Gal Gadot')
print(actors, '\n')

more_james_bonds = ['Roger Moore', 'Timothy Dalton', 'Pierce Brosnan', 'David Niven',
                    'Daniel Craig']
