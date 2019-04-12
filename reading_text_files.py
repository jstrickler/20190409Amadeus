#!/usr/bin/env python

#  file_obj = open('file_name', 'r')

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
    # mary_in.close()

print('-' * 60)
with open('DATA/mary.txt') as mary_in:
    whole_file = mary_in.read()
    print(str(whole_file))
    print()
    print(repr(whole_file))
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    lines_with_nl = mary_in.readlines()
    print(lines_with_nl)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    lines_without_nl = [line.rstrip() for line in mary_in]
    print(lines_without_nl)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    lines_without_nl = (line.rstrip() for line in mary_in)
    print(lines_without_nl)
print('-' * 60)

with open('DATA/words.txt') as words_in:
    for line in words_in:
        if line.startswith('x'):
            print(line.rstrip())
print('-' * 60)


