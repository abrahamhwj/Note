#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/15 20:43

dial_codes = {(86,'China'),(91,'India'),(1,'US'),(55,'Brazil'),(81,'Japan')}

d1 = dict(dial_codes)
print(d1)

d2=dict(sorted(dial_codes))
print(d2)

d3= dict(sorted(dial_codes,key=lambda x:x[1]))
print(d3)