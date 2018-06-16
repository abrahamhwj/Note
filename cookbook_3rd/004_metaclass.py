#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/10 19:46

#cls=当前准备创建的类的对象；name=类的名字；base=类继承的父类集合；attr=类的方法集合。

class UpperAttrMetaclass(type):
    def __new__(cls, *args, **kwargs):
        name,bases,attrs=args[:3]
        upper_attr={}
        for name,val in attrs.items():
            if not name.startswith('__'):
                upper_attr[name.upper()]=val
            else:
                upper_attr[name]=val
        return type.__new__(cls,name,bases,upper_attr)


#__metaclass__ = UpperAttrMetaclass         #global metaclass for module ,only work before py3.5

class new(metaclass=UpperAttrMetaclass):
    # __metaclass__ = UpperAttrMetaclass        #error
    bar = 'yes'
    def big(self):
        pass

class foo(metaclass=UpperAttrMetaclass):
    # __metaclass__ = UpperAttrMetaclass
    foo='yes'

if __name__ == '__main__':
    t=new()
    print(dir(t))
    print(t.__dict__)
    print(t)
    print(hasattr(t,'bar'))
    print(hasattr(t,'BAR'))
    print(hasattr(t,'BIG'))

    print('-------------------------------')
    t1=foo()
    print(hasattr(t1,'foo'))
    print(hasattr(t1,'FOO'))