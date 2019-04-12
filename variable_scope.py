#!/usr/bin/env python
"""
Demonstration of Python scope
"""
x = 100 # GLOBAL variable

def main():
    """
    Program entry point

    :return: None
    """
    spam()

def spam():
    """
    Silly function.

    :return: None
    """
    y = 42  # LOCAL variable
    print("in spam() -- x is", x)

if __name__ == '__main__':
    main()
