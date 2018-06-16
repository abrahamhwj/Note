#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/11 22:54
class Descriptor:
    def __init__(self,name=None,**opts):
        self.name = name
        for k,v in opts.items():
            setattr(self,k,v)

    def __set__(self, instance, value):
        instance.__dict__[self.name]=value

class Typed(Descriptor):
    expected_type = type(None)
    def __set__(self, instance, value):
        if not isinstance(value,self.expected_type):
            raise TypeError('expected '+str(self.expected_type))
        super().__set__(instance,value)

class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >=0')
        super().__set__(instance,value)

class MaxSized(Descriptor):
    def __init__(self,name=None,**opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name,**opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be <'+str(self.size))
        super().__set__(instance,value)

class Integer(Typed):
    expected_type = int

class UnsignedInteger(Integer,Unsigned):
    pass

class Float(Typed):
    expected_type = float

class UnsignedFloat(Float,Unsigned):
    pass

class String(Typed):
    expected_type = str

class SizedString(String,MaxSized):
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
    # name = SizedString('name',size=8)
    # shares = UnsignedInteger('shares')
    # price = UnsignedFloat('price')
    def __init__(self,name,shares,price):
        self.name=name
        self.shares=shares
        self.price=price

class CheckMeta(type):
    def __new__(cls, name, bases,attrs):
        for key,val in attrs.items():
            if isinstance(val,Descriptor):
                val.name=key
        return type.__new__(cls,name,bases,attrs)

class Stock2(metaclass=CheckMeta):
    name=SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()

    def __init__(self,name,shares,price):
        self.name=name
        self.shares=shares
        self.price = price
        self.t=shares*price


if __name__ == '__main__':
    t=Stock('SINA',75,44.3)
    t.name='ACE'
    t.shares=123
    print(t.__dict__)
    t2=Stock2('SINA',75,44.3)
    t2.name='aaa'
    t2.shares=123

    t2.price=1.1
    print(t2.__dict__)