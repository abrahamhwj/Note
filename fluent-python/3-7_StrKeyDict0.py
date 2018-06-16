#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/14 22:51


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self,key):
        return key in self.keys() or str(key) in self.keys()


if __name__ == '__main__':
    d={'f1':134,'f2':'test',1:'this'}
    t=StrKeyDict0(d)
    print(t['f1'])
    print(t[1])
    t[34]='hello'
    print(t)