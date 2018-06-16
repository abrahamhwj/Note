#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Hao
# datetime:2018/6/12 23:50

import sys
import re

word_re=re.compile(r'\w+')

index={}

print(sys.argv[0])
with open(sys.argv[1],encoding='utf-8') as fp:
    for lin_no,line in enumerate(fp,1):
        for match in word_re.finditer(line):
            word=match.group()
            column_no=match.start()+1
            location=(lin_no,column_no)
            # occurrences=index.get(word,[])
            # occurrences.append(location)

            # occurrences = index.get(word, []).append(location)
            # index[word]=index.get(word, []).append(location)
            index.setdefault(word,[]).append(location)  #D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

for word in sorted(index,key=str.upper):
    print(word,index[word])
