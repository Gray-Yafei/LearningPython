# -*- coding: utf-8 -*-
# @Time : 2024/9/7 13:30
# @Author : Gray
'''字符消除'''
s = input()
s = s.split(" ")
n = int(s[0])
k = int(s[1])
# 得到n和k
l = []  # 保存数列
for i in range(k):
    s = input()
    s = s.split(" ")
    l.append(s)

s = input()  # 记录字符串
sum1 = 0  # 当前最大
result = 0  # 记录所有最大
record_i = 0
record_j = 0


while True:
    if len(s) == 0:
        break
    for i in range(1,len(s)):
        j = i-1
        if int(l[ord(s[j])-97][ord(s[i])-97]) > sum1:
            sum1 = int(l[ord(s[j])-97][ord(s[i])-97])
            record_i = i
            record_j = j
    result += sum1
    sum1 = 0
    s = s.removeprefix(s[record_j])
    s = s.removesuffix(s[record_j])

print(result)
# print(ord('a')-97)  # 将字母a转化为0
#
# s = input()
# i = 'a'
# s = s.removeprefix(i)
# print(s)


'''对比之美'''
# T = int(input())
# l = []
# for i in range(T):
#     s = input()
#     s = s.split(" ")
#     n = int(s[0])  # 格子数量
#     m = int(s[1])  # 收藏品数量
#     if n == 1:
#         l.append(0)
#     elif n == 2:
#         l.append(m)
#     else:
#         l.append(2*m)
#
# for i in l:
#     print(i,end=' ')