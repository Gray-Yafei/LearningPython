# -*- coding: utf-8 -*-
# @Time : 2024/9/16 9:16
# @Author : Gray

# https://www.bilibili.com/video/BV1MH48esE2X/?p=6&vd_source=b50ae0ac5f19d4afb46473cc893246a2
'''1.汉诺塔递归'''


def hanoi(n, a, b, c):
    if n == 1:
        print(f"{a} -> {c}")
    else:
        hanoi(n - 1, a, c, b)
        # print(f"{a} -> {b}")
        hanoi(1, a, b, c)
        hanoi(n - 1, b, a, c)


'''2.查找'''


# 2.1 顺序查找
def linearSearch(l, element):
    for i in range(len(l)):
        if element == l[i]:
            return i
    return -1


def binarySearch(l, element):
    left = 0
    right = len(l) - 1
    mid = (left + right) // 2
    while left <= right:
        if element == l[mid]:
            return mid
        elif element > l[mid]:
            left = mid + 1
            mid = (left + right) // 2
        else:
            right = mid - 1
            mid = (left + right) // 2
    return -1


'''3.排序'''
# 3.1 冒泡排序

def bubbleSort(l):
    for i in range(len(l)-1):
        isflag = False
        for j in range(len(l)-1-i):
            if l[j+1] < l[j]:
                isflag = True
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
        print(l)
        if not isflag:
            break
    return l
# 3.2 选择排序

def selectionSort_v1(l):
    l_new = []
    for i in range(len(l)):
        minelement = min(l)
        l_new.append(minelement)
        l.remove(minelement)
    return l_new

def selectionSort_v2(l):
    for i in range(len(l)-1):
        minindex = i
        for j in range(i+1,len(l)):
            if l[j] < l[minindex]:
                minindex = j
        temp = l[minindex]
        l[minindex] = l[i]
        l[i] = temp
    return l

def insertionSort(l):
    for i in range(1,len(l)):

if __name__ == '__main__':
    # hanoi(2, 'A', 'B', 'C')
    # result = linearSearch([1,2,3,4,5],6)
    # print(result)
    # result = binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
    # print(result)
    # l = [2,5,8,3,6,0,1,7,4,9]
    # bubbleSort(l)
    # print(bubbleSort(l))
    l = [2, 5, 8, 3, 6, 0, 1, 7, 4, 9]
    print(selectionSort_v2(l))
