#!/usr/bin/env python
"""
This has only the Foo class.
"""

class Foo:
    """
    This is a sample class for demo purposes
    """
    def __init__(self):
        pass

    def blech(self, foo, bar):
        """
        Some useful method.

        :param foo: the foo parameter
        :param bar: the bar parameter must be a list
        :return: float
        """
        print(foo, bar)
if __name__ == '__main__':
    f = Foo()
    f.blech(1, 2)
