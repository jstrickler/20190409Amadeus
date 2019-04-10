#!/usr/bin/env python

actors = ['Brad Pitt', 'Chris Hemsworth',
          'Angelina Jolie', 'Tom Hanks',
          'Humphrey Bogart']

actors.append('Jason Stathham')
actors.insert(0, 'Sean Connery')
actors.insert(5, 'Gal Gadot')

more_james_bonds = ['Roger Moore', 'Timothy Dalton', 'Pierce Brosnan', 'David Niven',
                    'Daniel Craig']

print(actors, '\n')

print(actors[0])
print(actors[7])
print(actors[len(actors)-1])
print(actors[-1])
print(actors[3], actors[-3])

# SEQ[START:STOP:STEP]
# START is INclusive  STOP is EXclusive
print(actors[0:4])
print(actors[-2:len(actors)])
print(actors[:4])
print(actors[-2:])
print(actors[2:6])

h = 'Humphrey Bogart'
print(h[:4], h[9:12], h[-3:])

print(h[12:9:-1])
print(h[::-1])
print(h[:])
print(h[::])
print(h[::2])
print(h[1::2])

print(actors, '\n')

for i, actor in enumerate(actors):
    print(i, actor)
print()

name = 'Bob'
x = name.split()


# for VAR ... in ITERABLE:
   # VAR ... = next(ITERABLE)
   # ....
    # VAR ... = next(ITERABLE)
    # ....
    # VAR ... = next(ITERABLE)
    # ....

for c in actors[3]:
    print(c)
print()

