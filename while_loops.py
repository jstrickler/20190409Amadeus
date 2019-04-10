#!/usr/bin/env python

while True:
    name = input("Enter your name: ")
    if name == 'q':
        break
    if name == '':
        continue

    if name == "Fred":
        print("What a special name!")
    print("Hello,", name)
