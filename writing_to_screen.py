#!/usr/bin/env python

actor = "Chris Hemsworth"
city = "Hollywood"

a = 15.3
b = 4.1

print(actor, "lives in", city)
print(a / b)

print("{} lives in {}".format(actor, city))

print("{:.2f}".format(a / b))

print(f"{actor} lives in {city}")
print(f"{a/b:.2f}")

big_number = 23982039582039582039582

print("Number is {:,d}".format(big_number))
print(f"Number is {big_number:,d}")
