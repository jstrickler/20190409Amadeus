#!/usr/bin/env python
a_lines = []
b_lines = []

with open('DATA/alt.txt') as alt_in:
    for line in alt_in:
        if line.startswith('a'):
            a_lines.append(line)
        elif line.startswith('b'):
            b_lines.append(line)

with open('a_sorted', 'w') as a_sorted_in:
    a_sorted_in.writelines(sorted(a_lines))
    # for line in sorted(a_lines):
    #     a_sorted_in.write(line)

with open('b_sorted', 'w') as  b_sorted_in:
    b_sorted_in.writelines(sorted(b_lines, reverse=True))
