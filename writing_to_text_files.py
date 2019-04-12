#!/usr/bin/env python
import os
from zipfile import ZipFile

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruitinfo.txt', 'w') as fruitinfo_out:
    for fruit in fruits:
        length = len(fruit)
        record = '{}\t{}\n'.format(fruit, length)
        fruitinfo_out.write(record)

#  use "c:/temp"  not "C:\temp"

with open('DATA/words.txt') as words_in:
    with open('bigwords.txt', 'w') as big_words_out:
        with open('capwords.txt', 'w') as cap_words_out:
            for word in words_in:
                if 'e' not in word:
                    big_words_out.write(word.upper())
                cap_words_out.write(word.capitalize())

# x = ZipFile('myzip.zip')
# x.append('myotherfile.txt')
# x.close()


for item in os.scandir('DATA'):
    if item.is_file():
        print("(FILE)", item.name)
    if item.is_dir():
        print("(DIR)", item.name)

curr_dir = os.getcwd()
os.chdir('DATA')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('/tmp')
print(os.getcwd())
os.chdir(curr_dir)
print(os.getcwd())
