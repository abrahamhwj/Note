#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/12 22:22

class Descriptor:
    def __init__(self,name=None,**opts):
        self.name=name
        for key,val in opts.items():
            setattr(self,key,val)

    def __set__(self, instance, value):
        instance.__dict__[self.name]=value

def Typed(expected_type,cls=None):
    if cls is None:
        return lambda cls:Typed(expected_type,cls)
    super_set=cls.__set__

    def __set__(self,instance,value):
        if not isinstance(value,expected_type):
            raise TypeError('expected '+str(expected_type))
        super_set(self,instance,value)
    cls.__set__=__set__
    return cls

@Typed(int)
class Integer(Descriptor):
    pass

if __name__ == '__main__':
    c=Typed(int,Integer)
