'''
title: frqVerb.py
date: Feb/21, 2020
author: YiFan Chu
purpose:
    generate the frequent used verbs, their past tense and p.p.

'''
f = open("source/frqVerb.txt")
l = f.read()
l = l.replace("\n"," ")
l = l.split(' ')
l = list(set(l))
l = list(filter(None, l))
l.sort()
l = '\n'.join(l)
fw = open("voc/frqVerb.txt",'w')
fw.write(l)
