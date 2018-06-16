#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/17 2:48
from functools import reduce
from operator import add

def func(n):
    return 1 if  n<2 else n+func(n-1)

if __name__ == '__main__':
    print(func(100))
    print(sum(range(101)))
    print(reduce(add,range(101)))

    print(sum(func(n) for n in range(5)))
    print(reduce(add,list(func(n) for n in range(5))))
