#!/usr/bin/env python

counts = {}

with open('DATA/words.txt') as words_in:
    for raw_line in words_in:
        letter = raw_line[0]
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1
        # counts[letter] = counts[letter] + 1

print(counts)
