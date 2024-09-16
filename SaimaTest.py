# -*- coding: utf-8 -*-
# @Time : 2024/9/8 14:31
# @Author : Gray
''''''
# 02基本算法
# 1.读取未给出行列数的矩阵
# l = []
# while True:
#     s = input()
#     if s == '':
#         break
#     l.append(list(map(int, s.split())))
# l = [list(row) for row in zip(*l)]
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(l[i][j], end=' ')
#     print()

'''动态规划'''
nums = [1, 5, 2, 4, 3]
count = 0

for i in range(len(nums)):
    num = nums[i]
    if



'''2.打字'''
# print(chr(97))
# def isCaps(alpha):
#     if ord(alpha) >= 97 and ord(alpha) <= 122:
#         return False
#     elif ord(alpha) >= 65 and ord(alpha) <= 90:
#         return True
# T = int(input())  # 循环次数
# result = []
# for i in range(T):
#     isflag = True  # 记录键盘大小写状态，True表示小写
#     count = 0  # 记录此次循环按键的次数
#     s = input()
#     for j in range(len(s)):
#         if isCaps(s[j]):
#             if isflag:
#                 count += 1
#             else:
#                 count += 2
#             isflag = True
#         else:
#             if isflag:
#                 count += 2
#             else:
#                 count += 1
#             isflag = False

