# -*- coding: utf-8 -*-
# @Time : 2024/9/13 8:27
# @Author : Gray


set1 = set()
s = input()
l = s.split(',')


for i in range(len(l)):
    if i == 0:
        print(l[i],end='')
        set1.add(l[i])
    if l[i] in set1:

        continue
    else:
        set1.add(l[i])
        print(',',end='')
        print(l[i],end='')
