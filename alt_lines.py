#!/usr/bin/env python

with open('DATA/alt.txt') as alt_in, open('a.txt', 'w') as a_out, open('b.txt', 'w') as b_out:
    for line in alt_in:
        if line.lower().startswith('a'):
        # if line[0] == 'a':
                a_out.write(line)
        elif line.lower().startswith('b'):
            b_out.write(line)

