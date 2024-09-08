# -*- coding: utf-8 -*-
# @Time : 2024/8/31 18:54
# @Author : Gray
# s = input()
# s1 = s.split(" ")
# count = 0
# for i in s1:
#     for j in i:
#         if j in (
#             "A",
#             "B",
#             "C",
#             "D",
#             "E",
#             "F",
#             "G",
#             "H",
#             "I",
#             "J",
#             "K",
#             "L",
#             "M",
#             "N",
#             "O",
#             "P",
#             "Q",
#             "R",
#             "S",
#             "T",
#             "U",
#             "V",
#             "W",
#             "X",
#             "Y",
#             "Z",
#         ):
#             count += 1
#         break
# print(count)



# s = input()
# s = s.split(" ")
# n = int(s[0])  # 工人数
# k = int(s[1])  # 树的最少数量
#
# a = input()
# a = a.split(" ")
# set1 = set()
# for i in a:
#     set1.add(int(i))
# result = 1  # 最终结果
# while True:
#     if len(set1) >= k:
#         break
#     result = result + 1
#     for i in a:
#         for j in range(result-1,result):
#             set1.add(int(i) + j)
# print(result)






s = input()
s = s.split(" ")
n = int(s[0])  # 数组长度
q = int(s[1])  # 询问次数

a = input()
a = a.split(" ")  # 保存n个整数
lst = []
for i in a:
    lst.append(int(i))
maxNum = max(lst)
minNum = min(lst)
print(minNum)
print(maxNum)
for i in range(q):
    a = input()
    a = a.split(" ")
    x = int(a[0])  # 区间上界
    y = int(a[1])  # 区间下界
    if y == maxNum-1 or y == minNum:
        print("lose")
        print(y-x+1)
    else:
        print("win")
        print(5-x)












