#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print("s0: {}\n".format(f0))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
n0 = sorted(nums)
print("n0: {}\n".format(n0))

def ignore_case(s):
    return s.lower()

f1 = sorted(fruits, key=ignore_case)   #
print("f1: {}\n".format(f1))

f2 = sorted(fruits, key=str.lower)   #
print("f2: {}\n".format(f2))

# for i, fruit in enumerate(sorted(...)):
f3 = sorted(fruits, key=len)
print("f3: {}\n".format(f3))

def custom1(e):
    return len(e), e.lower()

f4 = sorted(fruits, key=custom1)
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

for first_name, last_name, _, _ in sorted(people):
    print(first_name, last_name)
print('-' * 60)

def by_birth_date(person):
    return person[0], person[1]

for first_name, last_name, _, birth_date in sorted(people, key=by_birth_date):
    print(first_name, last_name, birth_date)
print('-' * 60)

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print('-' * 60)

def by_value(airport):
    return airport[1], airport[0]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print('-' * 60)

def foo(f):
    return f.lower()

print(sorted(nums, reverse=True), '\n')
print(sorted(fruits, reverse=True, key=lambda f: f.lower()))


