#!/usr/bin/env python

d1 = dict()
d2 = {}
d3 = dict(MA="Boston", DE="Dover")  # dict.__init__
st_caps = [('NC', 'Raleigh'), ('SC', 'Columbia')]
d4 = dict(st_caps)

state_capitals = {
    'MA': 'Boston',
    'DE': 'Dover',
    'NH': 'Concord',
    'VT': 'Montpelier',
    'NY': 'Albany',
}
print(state_capitals['MA'])
state_capitals['NJ'] = 'Trenton'
state_capitals['MA'] = 'Waltham'
print(state_capitals, '\n')
print(state_capitals.get('RI'))
print(state_capitals.get('RI', 'NOT FOUND'))
print(state_capitals.setdefault('RI', 'Providence'))
print()
print(state_capitals, '\n')
print(state_capitals.keys())
print(state_capitals.values())
print()

for state, capital in state_capitals.items():
    print(state, capital)
print()

for state in 'MA', 'NC', 'RI', 'VT':
    print(state, state in state_capitals)
print()

del state_capitals['RI']
print(state_capitals, '\n')

more_caps = dict([('NC', 'Raleigh'), ('SC', 'Columbia'),('MA', 'Boston')])

state_capitals.update(more_caps)
print(state_capitals)

