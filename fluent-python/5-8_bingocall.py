#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/17 3:27

import random

class bingoCage:
    def __init__(self,items):
        self._items = list(items)
        random.shuffle(self._items)
        print(self._items)
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick up from empty bingoCage.')
    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    t=bingoCage(range(10))
    print(t.pick())
    print(callable(t))
    print(t())
    print(t())

