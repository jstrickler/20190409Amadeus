#!/usr/bin/env python

with open("../DATA/presidents.txt", "r") as pres_in:
    all_pres = (line.rstrip().split(':') for line in pres_in)

    pres_gen = (p for p in all_pres if p[-1] == 'Republican' if p[6] == 'Ohio')

    SORT_ONE = -3
    SORT_TWO = 2

# sort by lname, fname
    for fields in sorted(pres_gen, key=lambda e: (SORT_ONE, SORT_TWO)):
        print(fields[2], fields[1], fields[6])
