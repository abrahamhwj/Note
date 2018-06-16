#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/10 1:35

class Quantity:     #描述符类，无需创建子类
    def __init__(self,storage_name):
        self.storage_name=storage_name      #托管类实例中存储属性的名称

    def __set__(self, instance, value):     #为托管实例属性赋值会调用__set__，self是描述符实例，instance是托管类实例，value是要赋的值
        if value > 0:
            instance.__dict__[self.storage_name]=value          #托管属性和存储属性名字一样，所以不能使用setattr,会再次调用__set__,造成无限循环
        else:
            raise ValueError('value must be > 0')

class LineItem:             #被描述类，托管类
    weight=Quantity('weight')           #第一个描述符，绑定给weight属性,'weight'=self.storage_name,描述符实例：LineItem.weight,托管类属性，同时也是描述符实例
    price=Quantity('price')             #第二个描述符，绑定给price属性,'price'=self.storage_name，描述符实例：LineItem.price，托管类属性，同时也是描述符实例

    def __init__(self,description,weight,price):
        self.description=description
        self.weight=weight
        self.price=price

    def subtotal(self):
        return self.weight * self.price

if __name__ == '__main__':
    t1=LineItem('APPLE',100,10)             #托管实例t1
    print(t1.subtotal())
    try:
        t1.weight=0
    except Exception as e:
        print(e)
        t1.weight=10
    print(t1.weight)

'''
LineItem同一时间内可能有众多实例，但是描述符实例，始终只有LineItem.weight/LineItem.price
'''