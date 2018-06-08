#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/9 2:53

class First(object):
    def __init__(self):
        print(type(self).mro())
        print ("first")

class Second(object):
    def __init__(self):
        super(Second,self).__init__()
        print(type(self).mro())
        print("2.that's it")

class Third(Second,First):
    def __init__(self):
        super(Third, self).__init__()
        print(type(self).mro())
        print ("3.that's it")

class Forth(Third):
    def __init__(self):
        super(Forth,self).__init__()
        print(type(self).mro())
        print("4.that's it")

if __name__ == '__main__':
    print(Forth())
    print("---------------")
    print(First())