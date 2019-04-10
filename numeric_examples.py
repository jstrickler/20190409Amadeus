#!/usr/bin/env python

i1 = 100
i2 = 0x100
i3 = 0b100
i4 = 0o100

print(i1, i2, i3, i4)
print()

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.23456e5

x = 27
y = 13

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x ** y)
print(x % y)

# x = 5
# y = x++
# z = ++x
# print(x, y, z)

x = 5
m = ++++++++++++++++++x

print(m)

print(---------x)
print(----------x)


x = 5
x += 15  # x = x + 15
x /= 4
x *= 10
print(x)

x = 123
print(str(x))

m = "567"

i = int(m)
print(i, type(i), type(m))

m = "DeadBeef"

print(int(m, 16))

flag = '01011101'

print(int(flag, 2))
print(bool(5))
print(bool('wombat'))
print(bool(5 - 5))

x = "123.456"

print(float(x))

print(int("103"))

