#!/usr/bin/env python

s2 = 'spam\n'
s1 = "spam\n"
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"  # raw string

print("Guido's the man!")
print('Guido is the "leader" of Python')

print("""Guido's the "main" man""")

query = """
select *
from spam
where ham = 'jambon de Paris'
"""


actor = "Chris Hemsworth"

print(actor.upper(), actor.lower())

ch = actor.upper()
print(ch)
print(actor)

print(len(actor))
print(type(actor))

print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))
print(actor.endswith('Pratt'))
print(actor.endswith('Pine'))
print(actor.endswith('Hemsworth'))
print("ems" in actor)
print(actor.replace(' ',''))
print(actor.replace('Hemsworth', 'Pine'))
print(actor.replace(' ','').isalpha())

s = "abccbaaaabbbChris Prattbcaaacccbabac"
print('|' + s.lstrip('abc') + '|')
print('|' + s.rstrip('abc') + '|')
print('|' + s.strip('abc') + '|')
print()

s = "              Chris Pratt            "
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')

chris_names = 'Hemsworth Pratt Pine'

last_names = chris_names.split()
print(last_names)

chris_names = 'Hemsworth;Pratt;Pine'
last_names = chris_names.split(';')
print(last_names)












