#!/usr/bin/env python

value = 150
name = 'Bob'

if value > 100:
    print("wombat")
    print("wallaby")
    if value > 127:
        print("kangaroo")
elif value > 75:
    print("crocodile")
elif value > 50:
    print("blue-ringed octopus")
else:
    print("kookaburra")
    print("platypus")

print("Done")

# FALSE
#  0 0.0 False None
#  ""  []  ()  {} set()

# TRUE
#  True  "True" "False" "Wombat" " "
#  [1]  [0]

def foo(x):
    print("string:>{}<".format(x))
    print("bool:", bool(x))

foo('hello')
foo('')
foo(None)

#  == != > < >= <= is

x = 5
y = 10
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x is y)

#  and  or  not











