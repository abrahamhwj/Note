#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/14 23:14


import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, item):
        return str(item) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)]=value


if __name__ == '__main__':
    d={'f1':134,'f2':'test',1:'this'}
    t=StrKeyDict(d)
    print(t['f1'])
    print(t[1])
    t[34]='hello'
    print(t)