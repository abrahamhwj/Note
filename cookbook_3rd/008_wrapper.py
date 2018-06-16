#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/12 0:16
class Descriptor:
    def __init__(self,name=None,**opts):
        self.name = name
        for k,v in opts.items():
            setattr(self,k,v)

    def __set__(self, instance, value):
        instance.__dict__[self.name]=value

def Typed(expected_type,cls=None):
    if cls is None:
        return lambda cls:Typed(expected_type,cls)
    super_set=cls.__set__

    def __set__(self,instance,val):
        if not isinstance(val,expected_type):
            raise TypeError('expected '+str(expected_type))
        super_set(self,instance,val)
    cls.__set__=__set__
    return cls

def Unsigned(cls):
    super_set=cls.__set__

    def __set__(self,instance,value):
        if value<0:
            raise ValueError('expected >=0')
        super_set(self,instance,value)
    cls.__set__=__set__
    return cls

def MaxSized(cls):
    super_init=cls.__init__
    def __init__(self,name=None,**opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super_init(self,name,**opts)
    cls.__init__ = __init__

    super_set=cls.__set__
    def __set__(self,instance,val):
        if len(val)>=self.size:
            raise ValueError('size must be < '+str(self.size))
        super_set(self,instance,val)

    cls.__set__=__set__
    return cls

@Typed(int)
class Integer(Descriptor):
    pass

@Unsigned
class UnsignedInteger(Integer):
    pass


@Typed(float)
class Float(Descriptor):
    pass


@Unsigned
class UnsignedFloat(Float):
    pass


@Typed(str)
class String(Descriptor):
    pass


@MaxSized
class SizedString(String):
    pass

def check_attributes(**kwargs):
    def decorate(cls):
        for k,v in kwargs.items():
            if isinstance(v,Descriptor):
                v.name=k
                setattr(cls,k,v)
            else:
                setattr(cls,k,v(k))
        return cls
    return decorate


@check_attributes(name=SizedString(size=8),shares=UnsignedInteger,price=UnsignedFloat)
class Stock:
    def __init__(self,name,shares,price):
        self.name=name
        self.shares=shares
        self.price=price

if __name__ == '__main__':
    t=Stock('haowen',44,23.1)
    print(t.__dict__)