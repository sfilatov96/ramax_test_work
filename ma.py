# -*- coding: utf-8 -*-


class MyError(Exception):
    pass


class Parent(object):
    def __init__(self, i=None):
        self.i = i or 3

    def fnc(self, x=None, y=None):
        if x == 7:
            raise MyError("Error text")

        y = y or x
        return x * y * self.i

    def isFirst(self):
        return 1 if isinstance(self, First) else 0

    @property
    def isSecond(self):
        return 1 if isinstance(self, Second) else 0


class First(Parent):
    pass


class Second(Parent):
    pass


class A(First):
    pass
