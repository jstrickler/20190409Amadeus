#!/usr/bin/env python
"""
Provide a demo abstract base class

MAX_TRIES -- we quit after this
"""
from abc import ABCMeta, abstractmethod


MAX_TRIES = 50

class MyBase(metaclass=ABCMeta):
    """
    Generic abstract base class
    """

    @abstractmethod
    def spam(self):
        """
        Sample abstract method

        :return:
        """
        pass

    @abstractmethod
    def ham(self):
        pass

    def eggs(self):
        print("SCRAMBLED!")

class Thing(MyBase):
    def spam(self):
        pass

    def ham(self):
        pass

t = Thing()

print(MyBase.__doc__)
