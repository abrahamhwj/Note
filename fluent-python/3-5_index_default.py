#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/13 0:26

import sys
import re
import collections

word_re=re.compile(r'\w+')

index=collections.defaultdict(list) #defaultdict(default_factory[, ...]) --> dict with default factory
#defaultdict(<class 'list'>, {})

print(index)

with open(sys.argv[1],encoding='utf-8') as fp:
    for lin_no,line in enumerate(fp,1):
        for match in word_re.finditer(line):
            word=match.group()
            column_no=match.start()+1
            location = (lin_no,column_no)
            index[word].append(location)        #因为是default_dict,如果word不存在，就会返回一个空列表,如果是默认的空字典，则会返回KeyError
            #==index.setdefault(word,[]).append(location)
for word in sorted(index,key=str.upper):
    print(word,index[word])


