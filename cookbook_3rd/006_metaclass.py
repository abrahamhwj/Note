#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/10 22:10




class Field(object):
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type

    def __str__(self):
        return f"<{self.__class__.__name__} {self.name}>"

class IntegerFiled(Field):
    def __init__(self,name):
        super(IntegerFiled,self).__init__(name,'bigint')

class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class ModelMetaclass(type):
    def __new__(cls, name,bases,attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        mappings=dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print(f'Found mapping:{k}=={v}')
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__table__'] = name
        attrs['__mappings__']= mappings
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
    # __metaclass__ = ModelMetaclass
    def __init__(self,**kwargs):
        super(Model,self).__init__(**kwargs)            #==super().__init__(**kwargs)
        print('***************',self)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(f"Model object has no attribute {item}")

    def __setattr__(self, key, value):
        self[key]=value

    def save(self):
        fields=[]
        params=[]
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
            print('***************',k,v)
        sql= f"Insert into {self.__table__} ({','.join(fields)}) value {','.join(params)}"
        print(f'SQL: {sql}')
        print(f"ARGS: {str(args)}")

class User(Model):
    id=IntegerFiled('id')
    name=StringField('username')
    email=StringField('email')
    password = StringField('password')



if __name__ == '__main__':
    U=User(id=12345,name='Model',email='test@org.com',password="my_pwd",test='te')
    print(U.__dict__)
    U.save()