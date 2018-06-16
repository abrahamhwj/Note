#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/10 19:14

class Person:
    def __init__(self):
        self.ability=1

    def eat(self):
        print(f"Eat={self.ability}")

    def sleep(self):
        print(f"Sleep={self.ability}")

    def save_life(self):
        print(f"Save={self.ability}")

class Wang(Person):
    def eat(self):
        print(f"Eat={self.ability*2}")

class Zhang(Person):
    def sleep(self):
        print(f"Sleep={self.ability*2}")

class Jiang(Person):
    def save_life(self):
        print(f"Save={self.ability*2}")

class Mixture(type):
    def __new__(cls, *args, **kwargs):
        name,bases,attr=args[:3]            #name=生成类名，bases=父类名，attr=生成类的属性
        p1,p2,p3=bases

        def eat(cls):
            p1.eat(cls)

        def sleep(cls):
            p2.sleep(cls)

        def save_life(cls):
            p3.save_life(cls)

        attr['eat']=eat
        attr['sleep']=sleep
        attr['save_life']=save_life

        return type(name,bases,attr)            #生成类name，他的父类是p1,p2,p3，包含属性eat（继承p1.eat）,sleep(继承p2.sleep),save_life(继承p3.save_life)
class newPerson(Wang,Jiang,Zhang,metaclass=Mixture):
    pass

if __name__ == '__main__':
    t=newPerson()
    t.eat()
