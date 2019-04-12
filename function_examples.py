#!/usr/bin/env python

def get_message():
    return "Hello, world"

m = get_message()

print(m)

print(get_message())

def print_message():
    m = get_message()
    print(m)

print_message()

#                        parameter
def print_message_upper(message="hello"):
    print(message.upper())

#                     argument
print_message_upper("Hello, world")
print_message_upper("wombats!")
# print_message_upper("a", "b")  BAD
print_message_upper() # BAD?

def make_string(s, size=10):
    return s * size

x = make_string('*', 20)
print(x)
print(make_string('&'))

def spam(a, b):
    pass

spam(5, 10)

def lookup(iata, *states):
    print(iata, len(states), states)
    for state in states:
        print(state)
    print('---')


lookup('BOS', 'VA', 'MA', 'IL')
lookup('ATL', 'GA', 'AK')
lookup('PVD')

def mean(*values):
    if values:
        return sum(values) / len(values)
    return 0

print(mean(5, 18, 95))
print(mean(5))
print(mean(4, 5, 22, -100))
print(mean())

def spam1(*, foo=100, bar='abc'):
    print("foo is {} bar is {}".format(foo, bar))

def spam2(*blech, foo=100, bar='abc'):
    print("foo is {} bar is {}".format(foo, bar))


spam1(foo=1, bar=2)
spam1(bar=2, foo=1)

spam1()
spam1(foo=12)
spam1(bar=35)

def config(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
    print()







def f1(x):
    pass

f1(5)
f1(x=5)

def f2(*m):
    pass

f2(1, 2, 3)
f2()
f2('a', 'b', 'c', 'd' 'e', 'f')

def f3(x, *y):
    pass

f3(1, 2, 3)
f3('a', 'b', 'c', 'd' 'e', 'f')

def f4(x, *y, m, n):
    pass

f4('a', 'b', 'c', 'd', m=5, n=10)

def f5(x, *, m, n):
    pass

f5('a', m=5, n=10)

def f6(x, *y, m, n, **stuff):
    print(stuff)

f6(99, 1, 2, 3, n='a', m='y', animal='wombat',
   city='Waltham', color='purple')





def f7(x, *, m, n, **stuff):
    pass


def read_csv(
        file_path,
        *,  # what follows are required named params
        sep=',',
        delimiter=None,
        header='infer',
        names=None,
        # ...
):
    print(sep, delimiter)


def foo(a, b=1, c=2, d=3):
    print(a, b, c, d)

foo(5)
foo(5, d=6, c=7)



def config(animal='wombat', **values):
    print(values)

config(animal='wallaby', tree='eucalyptus')




